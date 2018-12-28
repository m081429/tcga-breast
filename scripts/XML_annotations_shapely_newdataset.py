#!/usr/local/biotools/python/3.4.3/bin/python3
__author__ = "Naresh Prodduturi"
__email__ = "prodduturi.naresh@mayo.edu"
__status__ = "Dev"

import cv2
import os
import argparse
import sys
import pwd
import time
import subprocess
import re
import shutil
from PIL import Image, ImageDraw
Image.MAX_IMAGE_PIXELS = 2300000000    
#Image.MAX_IMAGE_PIXELS = 5000000000    
from scipy import stats
import xml.etree.ElementTree as ET
from xml.dom import minidom
import pickle
import numpy as np
#from openslide import open_slide
import  openslide
from openslide.deepzoom import DeepZoomGenerator
import glob
from shapely.geometry import Polygon, Point, MultiPoint
from shapely.geometry import geo
import math
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection
import matplotlib.patches as patches
from descartes.patch import PolygonPatch
sys.path.append('/data/Naresh_Learning/wsi-sampler')
from sampler import WsiSample
#import matplotlib.nxutils as mn
import geopandas as gpd

import pyproj    
import shapely
import shapely.ops as ops
from shapely.geometry.polygon import Polygon
from functools import partial

output_ori_sub_dir="/data/Naresh_Learning/scripts/patches1/original_subpatch"
output_bin_sub_dir="/data/Naresh_Learning/scripts/patches1/binary_subpatch"
train_eval="/data/projects/breast/raw_data/BACH/Test_data/"
train_eval_label="/data/projects/breast/raw_data/BACH/Test_data/labels.txt"
train_In_situ="/data/projects/breast/raw_data/BACH/Training_data/In Situ"
train_Invasive="/data/projects/breast/raw_data/BACH/Training_data/Invasive"
train_Benign="/data/projects/breast/raw_data/BACH/Training_data/Benign"
train_Normal="/data/projects/breast/raw_data/BACH/Training_data/Normal"
BreaKHis_v1_malignant="/data/Naresh_Learning/scripts/patches1/BreaKHis_v1_malignant.txt"
BreaKHis_v1_benign="/data/Naresh_Learning/scripts/patches1/BreaKHis_v1_benign.txt"
size = 512, 512

def Create_patch_new(img_path,img_name,bin_name,bin_type):
	patch_sub_size=512
	#print(img_path+' '+img_name+' '+bin_name+' '+str(bin_type))
	ann_Img_tmp = Image.open(img_path)
	try:
		#ann_Img_tmp.thumbnail(size, Image.ANTIALIAS)
		#ann_Img_tmp = ImageOps.fit(ann_Img_tmp, size, Image.ANTIALIAS)
		ann_Img_tmp = ann_Img_tmp.resize((512, 512), Image.ANTIALIAS)
	except IOError:
		print('cannot create thumbnail for '+img_path)
		sys.exit(1)
	timg_name=output_ori_sub_dir+'/'+img_name
	bimg_name=output_bin_sub_dir+'/'+bin_name	
	M = np.array(ann_Img_tmp)	
	M1=np.zeros((M.shape[0], M.shape[1])).astype(np.uint8)
	if bin_type==1:
		M1.fill(1)
	im_sub = Image.fromarray(M1)
	im_sub.save(bimg_name, "png")	
	im_sub = Image.fromarray(M)
	im_sub.save(timg_name, "png")
	#sys.exit(0)
			
def Create_patch(img_path,img_name,bin_name,bin_type):
	#print(img_path+' '+img_name+' '+bin_name+' '+str(bin_type))
	ann_Img_tmp = Image.open(img_path)
	M = np.array(ann_Img_tmp)
	start_x=0
	patch_sub_size=512
	while start_x < M.shape[1]:
		start_y=0
		while start_y < M.shape[0]:
			#print(str(start_x)+' '+str(start_x+patch_sub_size-1)+' '+str(start_y)+' '+str(start_y+patch_sub_size-1))
			t = M[start_y:start_y+patch_sub_size,start_x:start_x+patch_sub_size]
			img_name=img_name.replace('.tif', '')
			bin_name=bin_name.replace('.tif', '')
			timg_name=output_ori_sub_dir+'/'+img_name+'_'+str(start_x)+'_'+str(start_y)+'.png'
			bimg_name=output_bin_sub_dir+'/'+bin_name+'_'+str(start_x)+'_'+str(start_y)+'.png'
			M1=np.zeros((patch_sub_size, patch_sub_size)).astype(np.uint8)
			if bin_type==1:
				M1.fill(1)
			im_sub = Image.fromarray(M1)
			im_sub.save(bimg_name, "png")	
			im_sub = Image.fromarray(t)
			im_sub.save(timg_name, "png")
			start_y	= start_y+patch_sub_size
		start_x = start_x+patch_sub_size
	#sys.exit(0)	

def main():
	list_train_eval=os.listdir(train_eval)
	list_train_In_situ=os.listdir(train_In_situ)
	list_train_Invasive=os.listdir(train_Invasive)
	list_train_Benign=os.listdir(train_Benign)
	list_train_Normal=os.listdir(train_Normal)
	#ann_Img_tmp = Image.open('/data/Naresh_Learning/scripts/patches1/binary_subpatch/1024_1024_Insitu_t16.tif')
	#M = np.array(ann_Img_tmp)
	#print(np.unique(M.reshape(-1, M.shape[1]), axis=0,return_counts=True))
	#sys.exit(1)
	

	
		
	'''reading Testing data Label'''
	dict_label={}
	fobj = open(train_eval_label)
	for file in fobj:
		file = file.strip()
		p = file.split("\t")
		dict_label[p[0]+'.tif']=p[1]
		
	'''reading Testing data'''
	for i in list_train_eval:
		if i != "labels.txt":
			if i in dict_label and (dict_label[i]=="Normal" or dict_label[i]=="Benign"):
				fn='Train_eval_Benign'+'_'+i
				Create_patch(train_eval+'/'+i,fn,fn,0)
			elif i in dict_label and (dict_label[i]=="In situ" or dict_label[i]=="Invasive"):
				fn='Train_eval_Tumor'+'_'+i
				Create_patch(train_eval+'/'+i,fn,fn,1)
			else:
				print(i)
				sys.exit(1)
			
	'''Reading all the In situ and Invasive images and converting them to binary patches'''
	for i in list_train_In_situ:
		Create_patch(train_In_situ+'/'+i,'Train_Insitu'+'_'+i,'Train_Insitu'+'_'+i,1)
		
	
	for i in list_train_Invasive:
		Create_patch(train_Invasive+'/'+i,'Train_Invasive'+'_'+i,'Train_Invasive'+'_'+i,1)
	
	for i in list_train_Benign:
		if i!="69.tif" and i!="t69.tif":
			Create_patch(train_Benign+'/'+i,'Train_Benign'+'_'+i,'Train_Benign'+'_'+i,0)
			
	for i in list_train_Normal:
		Create_patch(train_Normal+'/'+i,'Train_Normal'+'_'+i,'Train_Normal'+'_'+i,0)

	train_eval_benign_dict={}
	train_eval_benign_num=0
	'''Reading BreaKHis_v1_benign'''
	fobj = open(BreaKHis_v1_benign)
	for file in fobj:
		file = file.strip()
		p = file.split("/")
		cond=p[len(p)-6]
		tissue=p[len(p)-4]
		samp_tiss=p[len(p)-3]
		fn=p[len(p)-1]
		if not samp_tiss in train_eval_benign_dict:
			train_eval_benign_num=train_eval_benign_num+1
			train_eval_benign_dict[samp_tiss]=train_eval_benign_num
		if train_eval_benign_dict[samp_tiss] < 4:
			cate="Train_eval_Benign"
		else:
			cate="Train_Benign"
		img_name=cate+'_'+cond+'_'+tissue+'_'+fn	
		#img_name=img_name.replace('png', 'tif')
		Create_patch_new(file,img_name,img_name,0)
	
	
	train_eval_malig_dict={}
	train_eval_malig_num=0
	'''Reading BreaKHis_v1_tumor'''
	fobj = open(BreaKHis_v1_malignant)
	for file in fobj:
		file = file.strip()
		p = file.split("/")
		cond=p[len(p)-6]
		tissue=p[len(p)-4]
		samp_tiss=p[len(p)-3]
		fn=p[len(p)-1]
		if not samp_tiss in train_eval_malig_dict:
			train_eval_malig_num=train_eval_malig_num+1
			train_eval_malig_dict[samp_tiss]=train_eval_malig_num
		if train_eval_malig_dict[samp_tiss] < 7:
			cate="Train_eval_Tumor"
		else:
			cate="Train_Tumor"
		img_name=cate+'_'+cond+'_'+tissue+'_'+fn	
		#img_name=img_name.replace('png', 'tif')
		Create_patch_new(file,img_name,img_name,1)		
		
if __name__ == "__main__":
	main()
