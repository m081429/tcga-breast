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
def Create_patch(img_path,img_name,bin_name,bin_type):
	ann_Img_tmp = Image.open(img_path)
	M = np.array(ann_Img_tmp)
	start_x=0
	patch_sub_size=512
	while start_x < M.shape[0]:
		start_y=0
		while start_y < M.shape[1]:
			print(str(start_x)+' '+str(start_y))
			start_y	= start_y+patch_sub_size
		start_x = start_x+patch_sub_size
	
	im_sub = Image.fromarray(M)
	im_sub.save(, "tiff")	
	sys.exit(1)	
def main():
	list_train_eval=os.listdir(train_eval)
	list_train_In_situ=os.listdir(train_In_situ)
	list_train_Invasive=os.listdir(train_Invasive)
	list_train_Benign=os.listdir(train_Benign)
	list_train_Normal=os.listdir(train_Normal)
	
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
				Create_patch(train_eval+'/'+i,output_ori_sub_dir+'/'+fn,output_bin_sub_dir+'/'+fn,0)
				M1=np.zeros((M.shape[0], M.shape[1])).astype(np.uint8)
				im_sub = Image.fromarray(M1)
				fn='Train_eval_Benign'+'_'+i
				im_sub.save(, "tiff")
			elif i in dict_label and (dict_label[i]=="In situ" or dict_label[i]=="Invasive"):
				M1=np.zeros((M.shape[0], M.shape[1])).astype(np.uint8)
				M1.fill(1)
				im_sub = Image.fromarray(M1)
				fn='Train_eval_Tumor'+'_'+i
				im_sub.save(output_bin_sub_dir+'/'+fn, "tiff")
			else:
				print(i)
				sys.exit(1)
			
	sys.exit(1)		
	'''Reading all the In situ and Invasive images and converting them to binary patches'''
	for i in list_train_In_situ:
		ann_Img_tmp = Image.open(train_In_situ+'/'+i)
		M = np.array(ann_Img_tmp)
		M1=np.zeros((M.shape[0], M.shape[1])).astype(np.uint8)
		M1.fill(1)
		im_sub = Image.fromarray(M1)
		im_sub.save(output_bin_sub_dir+'/Insitu'+'_'+i, "tiff")
		im_sub = Image.fromarray(M)
		im_sub.save(output_ori_sub_dir+'/Insitu'+'_'+i, "tiff")
	
	for i in list_train_Invasive:
		ann_Img_tmp = Image.open(train_Invasive+'/'+i)
		M = np.array(ann_Img_tmp)
		M1=np.zeros((M.shape[0], M.shape[1])).astype(np.uint8)
		M1.fill(1)
		im_sub = Image.fromarray(M1)
		im_sub.save(output_bin_sub_dir+'/Invasive'+'_'+i, "tiff")
		im_sub = Image.fromarray(M)
		im_sub.save(output_ori_sub_dir+'/Invasive'+'_'+i, "tiff")
	
	for i in list_train_Benign:
		if i!="69.tif" and i!="t69.tif":
			ann_Img_tmp = Image.open(train_Benign+'/'+i)
			M = np.array(ann_Img_tmp)
			M1=np.zeros((M.shape[0], M.shape[1])).astype(np.uint8)
			im_sub = Image.fromarray(M1)
			im_sub.save(output_bin_sub_dir+'/Benign'+'_'+i, "tiff")
			im_sub = Image.fromarray(M)
			im_sub.save(output_ori_sub_dir+'/Benign'+'_'+i, "tiff")
	
	for i in list_train_Normal:
		ann_Img_tmp = Image.open(train_Normal+'/'+i)
		M = np.array(ann_Img_tmp)
		M1=np.zeros((M.shape[0], M.shape[1])).astype(np.uint8)
		im_sub = Image.fromarray(M1)
		im_sub.save(output_bin_sub_dir+'/Normal'+'_'+i, "tiff")
		im_sub = Image.fromarray(M)
		im_sub.save(output_ori_sub_dir+'/Normal'+'_'+i, "tiff")
		
if __name__ == "__main__":
	main()
