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
tf_record_file="/data/Naresh_Learning/scripts/patches1/tfrecord.txt"
train_eval="/data/projects/breast/raw_data/BACH/Test_data/"
train_eval_label="/data/projects/breast/raw_data/BACH/Test_data/labels.txt"
train_In_situ="/data/projects/breast/raw_data/BACH/Training_data/In Situ"
train_Invasive="/data/projects/breast/raw_data/BACH/Training_data/Invasive"
train_Benign="/data/projects/breast/raw_data/BACH/Training_data/Benign"
train_Normal="/data/projects/breast/raw_data/BACH/Training_data/Normal"
BreaKHis_v1_malignant="/data/Naresh_Learning/scripts/patches1/BreaKHis_v1_malignant.txt"
BreaKHis_v1_benign="/data/Naresh_Learning/scripts/patches1/BreaKHis_v1_benign.txt"
size = 512, 512

#def Create_patch_new(img_path,img_name,bin_name,bin_type):
def Create_patch_new(img_path,img_name,tf_record_type,image_hist,tiss_path,tum_class):
	image_format='png'
	height=512
	width=512
	# print("image_path"+' '+img_path)
	# print("image_name"+' '+img_name)
	# print("image_format"+' '+image_format)
	# print("height"+' '+str(height))
	# print("width"+' '+str(width))
	# print("tf_record_type"+' '+tf_record_type)
	# print("histological"+' '+str(image_hist))
	# print("tissue path"+' '+str(tiss_path))
	# print("Tumor class"+' '+str(tum_class))
	# sys.exit(0)
	myfile = open(tf_record_file, mode='a')
	patch_sub_size=512
	#print(img_path+' '+img_name+' '+bin_name+' '+str(bin_type))
	ann_Img_tmp = Image.open(img_path)
	try:
		#ann_Img_tmp.thumbnail(size, Image.ANTIALIAS)
		#ann_Img_tmp = ImageOps.fit(ann_Img_tmp, size, Image.ANTIALIAS)
		ann_Img_tmp = ann_Img_tmp.resize((height, width), Image.ANTIALIAS)
	except IOError:
		print('cannot create thumbnail for '+img_path)
		sys.exit(1)
	timg_name=output_ori_sub_dir+'/'+img_name
	timg_name_tf=img_name.replace('.png', '')
	M = np.array(ann_Img_tmp)	
	im_sub = Image.fromarray(M)
	im_sub.save(timg_name, "png")
	myfile.write(timg_name+"\t"+image_format+"\t"+str(height)+"\t"+str(width)+"\t"+tf_record_type+"\t"+timg_name_tf+"\t"+str(image_hist)+"\t"+str(tiss_path)+"\t"+str(tum_class)+"\n")
	myfile.close()
	
			
def Create_patch(img_path,image_name,tf_record_type,image_hist,tiss_path,tum_class):
	myfile = open(tf_record_file, mode='a')
	image_name=image_name.replace('.tif', '')
	image_format='png'
	height=512
	width=512
	# print("image_path"+' '+img_path)
	# print("image_data"+' '+image_data)
	# print("image_format"+' '+image_format)
	# print("height"+' '+str(height))
	# print("width"+' '+str(width))
	# print("tf_record_type"+' '+tf_record_type)
	# print("image_name"+' '+image_name)
	# print("histological"+' '+str(image_hist))
	# print("tissue path"+' '+str(tiss_path))
	# print("Tumor class"+' '+str(tum_class))
	# sys.exit(0)
	ann_Img_tmp = Image.open(img_path)
	M = np.array(ann_Img_tmp)
	start_x=0
	patch_sub_size=512
	while start_x < M.shape[1]:
		start_y=0
		while start_y < M.shape[0]:
			#print(str(start_x)+' '+str(start_x+patch_sub_size-1)+' '+str(start_y)+' '+str(start_y+patch_sub_size-1))
			t = M[start_y:start_y+patch_sub_size,start_x:start_x+patch_sub_size]
			timg_name=output_ori_sub_dir+'/'+image_name+'_'+str(start_x)+'_'+str(start_y)+'.png'
			timg_name_tf=image_name+'_'+str(start_x)+'_'+str(start_y)
			im_sub = Image.fromarray(t)
			im_sub.save(timg_name, "png")
			myfile.write(timg_name+"\t"+image_format+"\t"+str(height)+"\t"+str(width)+"\t"+tf_record_type+"\t"+timg_name_tf+"\t"+str(image_hist)+"\t"+str(tiss_path)+"\t"+str(tum_class)+"\n")	
			start_y	= start_y+patch_sub_size
		start_x = start_x+patch_sub_size
	myfile.close()
	

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
	
	#creating the tf_record_file
	myfile = open(tf_record_file, mode='wt')
	myfile.write("image_data\timage_format\theight\twidth\ttf_record_type\timage_name\thistological\ttissue_path\tTumor_class\n")
	myfile.close()
	#creating dictionary for histology
	hist_dict={}
	hist_dict["adenosis"]=1
	hist_dict["fibroadenoma"]=2
	hist_dict["phyllodes_tumor"]=3
	hist_dict["tubular_adenoma"]=4
	hist_dict["ductal_carcinoma"]=5
	hist_dict["lobular_carcinoma"]=6
	hist_dict["mucinous_carcinoma"]=7
	hist_dict["papillary_carcinoma"]=8
	
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
				fn='Bach_test_'+dict_label[i]+'_'+i
				image_hist=9
				tum_class=0
				tiss_path=1
				if dict_label[i]=="Normal":
					image_hist=0
					tiss_path=0
				Create_patch(train_eval+i,fn,"val",image_hist,tiss_path,tum_class)
			elif i in dict_label and (dict_label[i]=="In situ" or dict_label[i]=="Invasive"):
				fn='Bach_test_'+dict_label[i]+'_'+i
				image_hist=9
				tum_class=1
				tiss_path=2
				if dict_label[i]=="Invasive":
					tiss_path=3
				Create_patch(train_eval+i,fn,"val",image_hist,tiss_path,tum_class)
			else:
				print(i)
				sys.exit(1)
			
	'''Reading all the In situ and Invasive images and converting them to binary patches'''
	for i in list_train_In_situ:
		image_hist=9
		tiss_path=2
		tum_class=1
		Create_patch(train_In_situ+'/'+i,'Train_Insitu'+'_'+i,"train",image_hist,tiss_path,tum_class)
	
	for i in list_train_Invasive:
		image_hist=9
		tiss_path=3
		tum_class=1
		Create_patch(train_Invasive+'/'+i,'Train_Invasive'+'_'+i,"train",image_hist,tiss_path,tum_class)
	
	for i in list_train_Benign:
		if i!="69.tif" and i!="t69.tif":
			image_hist=9
			tiss_path=1
			tum_class=0
			Create_patch(train_Benign+'/'+i,'Train_Benign'+'_'+i,"train",image_hist,tiss_path,tum_class)
			
	for i in list_train_Normal:
		image_hist=0
		tiss_path=0
		tum_class=0
		Create_patch(train_Normal+'/'+i,'Train_Normal'+'_'+i,"train",image_hist,tiss_path,tum_class)

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
		tf_record_type=""	
		if train_eval_benign_dict[samp_tiss] < 5:
			cate="Train_BH_eval_Benign"
			tf_record_type="val"
		else:
			cate="Train_BH_Benign"
			tf_record_type="train"
		img_name=cate+'_'+cond+'_'+tissue+'_'+fn	
		image_hist=9
		if not tissue in hist_dict:
			print("no entry found hist_dict for "+file)
			sys.exit(1)
		image_hist=hist_dict[tissue]
		tiss_path=1
		tum_class=0
		Create_patch_new(file,img_name,tf_record_type,image_hist,tiss_path,tum_class)
	
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
		tf_record_type=""	
		if train_eval_malig_dict[samp_tiss] < 11:
			cate="Train_BH_eval_Tumor"
			tf_record_type="val"
		else:
			cate="Train_BH_Tumor"
			tf_record_type="train"
		img_name=cate+'_'+cond+'_'+tissue+'_'+fn	
		image_hist=9
		if not tissue in hist_dict:
			print("no entry found hist_dict for "+file)
			sys.exit(1)
		image_hist=hist_dict[tissue]
		tiss_path=3
		tum_class=1
		Create_patch_new(file,img_name,tf_record_type,image_hist,tiss_path,tum_class)
		
if __name__ == "__main__":
	main()
