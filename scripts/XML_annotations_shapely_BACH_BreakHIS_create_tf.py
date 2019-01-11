#!/usr/local/biotools/python/3.4.3/bin/python3
__author__ = "Naresh Prodduturi"
__email__ = "prodduturi.naresh@mayo.edu"
__status__ = "Dev"

#import cv2
import os
import argparse
import sys
import pwd
import time
import subprocess
#import re
#import shutil
from PIL import Image, ImageDraw
#Image.MAX_IMAGE_PIXELS = 2300000000    
#Image.MAX_IMAGE_PIXELS = 5000000000    
#from scipy import stats
#import xml.etree.ElementTree as ET
#from xml.dom import minidom
#import pickle
import numpy as np
#from openslide import open_slide
#import  openslide
#from openslide.deepzoom import DeepZoomGenerator
#import glob
#from shapely.geometry import Polygon, Point, MultiPoint
#from shapely.geometry import geo
#import math
#import matplotlib
#matplotlib.use('agg')
#import matplotlib.pyplot as plt
#from matplotlib.collections import PatchCollection
#import matplotlib.patches as patches
#from descartes.patch import PolygonPatch
#sys.path.append('/data/Naresh_Learning/wsi-sampler')
#from sampler import WsiSample
#import matplotlib.nxutils as mn
#import geopandas as gpd
import tensorflow as tf
#import pyproj    
#import shapely
#import shapely.ops as ops
#from shapely.geometry.polygon import Polygon
#from functools import partial
import io

tf_record_file="/data/Naresh_Learning/scripts/patches1/tfrecord.txt"
tf_record_dir="/data/Naresh_Learning/scripts/patches1/tfrecord"
#sys.path.insert(0, '/data/projects/breast/scripts/')
from dataset_utils import *
def main():
	#creating the tfrecord writers
	training_writer1=tf.python_io.TFRecordWriter(tf_record_dir+'/bh_bach_train_bach.tfrecords')
	training_writer2=tf.python_io.TFRecordWriter(tf_record_dir+'/bh_bach_train_bh.tfrecords')
	val_writer1=tf.python_io.TFRecordWriter(tf_record_dir+'/bh_bach_val_bach.tfrecords')
	val_writer2=tf.python_io.TFRecordWriter(tf_record_dir+'/bh_bach_val_bh.tfrecords')
	#reading tf record file
	fobj = open(tf_record_file)
	header=fobj.readline()
	for file in fobj:
		file = file.strip()
		p = file.split("\t")
		image_data=p[0]      
		image_format=p[1]    
		height=p[2]
		width=p[3]  
		tf_record_type=p[4]  
		image_name=p[5]      
		histological=p[6]    
		tissue_path=p[7]     
		Tumor_class=p[8]
		# print("image_data"+' '+image_data)
		# print("image_format"+' '+image_format)
		# print("height"+' '+height)
		# print("width"+' '+width)
		# print("tf_record_type"+' '+tf_record_type)
		# print("image_name"+' '+image_name)
		# print("histological"+' '+histological)
		# print("tissue path"+' '+tissue_path)
		# print("Tumor class"+' '+Tumor_class)
		ann_Img_tmp = Image.open(image_data)
		#M = np.array(ann_Img_tmp)
		imgByteArr = io.BytesIO()
		ann_Img_tmp.save(imgByteArr, format='PNG')
		imgByteArr = imgByteArr.getvalue()
		record=image_to_tfexample_step1(imgByteArr,image_format,int(height),int(width),image_name,int(histological),int(tissue_path),int(Tumor_class))
		#sys.exit(0)
		if tf_record_type =="train":
			if '_BH_' in image_name:
				training_writer2.write(record.SerializeToString())
			else:
				training_writer1.write(record.SerializeToString())
		if tf_record_type =="val": 
			if '_BH_' in image_name:
				val_writer2.write(record.SerializeToString())
			else:
				val_writer1.write(record.SerializeToString())
	training_writer1.close()
	training_writer2.close()
	val_writer1.close()	
	val_writer2.close()		
if __name__ == "__main__":
	main()
