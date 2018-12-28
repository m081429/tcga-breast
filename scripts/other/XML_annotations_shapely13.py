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
from scipy import stats
import xml.etree.ElementTree as ET
from xml.dom import minidom
import pickle
import numpy as np
#from openslide import open_slide
import  openslide
from openslide.deepzoom import DeepZoomGenerator
from glob import glob
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

def input_file_validity(file):
	'''Validates the input files'''
	if os.path.exists(file)==False:
		raise argparse.ArgumentTypeError( '\nERROR:Path:\n'+file+':Does not exist')
	if os.path.isfile(file)==False:
		raise argparse.ArgumentTypeError( '\nERROR:File expected:\n'+file+':is not a file')
	if os.access(file,os.R_OK)==False:
		raise argparse.ArgumentTypeError( '\nERROR:File:\n'+file+':no read access ')
	return file

def argument_parse():
	'''Parses the command line arguments'''
	parser=argparse.ArgumentParser(description='')
	parser.add_argument("-i","--input_file",help="input xml annotation file",required="True",type=input_file_validity)
	parser.add_argument("-o","--output_file",help="output file")
	parser.add_argument("-s","--svs_file",help="input svs file",required="True")
	parser.add_argument("-p","--patch_dir",help="output patch directory",required="True")
	parser.add_argument("-n","--tcgaid",help="TCGA Sample ID",required="True")
	return parser

def save_object(obj, filename):
	with open(filename, 'wb') as output:  # Overwrites any existing file.
		pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)

def create_patch_overlap_coord():
	'''This part of the code creates the path image with overlapping coordinates'''
	# img = openslide.OpenSlide(arg.svs_file)
	# img_dim = img.level_dimensions[0]
	# patch_size=10000
	# """
	# Determine what the patch size should be, and how many iterations it will take to get through the WSI
	# """
	# #num_x_patches = int(math.floor(img_dim[0]/patch_size))
	# #num_y_patches = int(math.floor(img_dim[1]/patch_size))
	# #print(str(num_x_patches)+" "+str(num_y_patches))
	# print(len(regions))
	# coords1=regions[8]
	# min=np.argmin(coords1, axis = 0)
	# #print(coords1[min[0]][0])
	# #print(coords1[min[1]][1])
	# #coords2=np.sort(coords1, axis = 0)
	# #print(coords2)
	# #sys.exit(1)
	# x1=int(coords1[min[0]][0])-10
	# y1=int(coords1[min[1]][1])-10
	# level=0
	# img_data = img.read_region((x1,y1),level, (patch_size, patch_size))
	# img_data_np = np.array(img_data)
	# img_name="sample.png"
	# im = Image.fromarray(img_data_np)
	# im.save(img_name)
	
	# # Create figure and axes
	# #fig,ax = plt.subplots(1)
	# fig,ax = plt.subplots()
	# # Display the image
	# ax.imshow(img_data_np)
	# #imgdata = plt.imread("sample.png")
	# #ax.imshow(imgdata)
	
	# # Add the patch to the Axes
	# #points = [[2, 1], [8, 1], [8, 4],[50,50],[100,100],[200,200]]
	# #plt.Polygon(points)
	# #poly = Polygon(verts, facecolor='0.9', edgecolor='0.5')
	# coords1_list=[]
	# for i in range(0,len(coords1)):
		# x_cor=int(coords1[i][0])-x1
		# y_cor=int(coords1[i][1])-y1
		# if x_cor >=0 and x_cor <= patch_size and y_cor >=0 and y_cor <=patch_size:
			# tmp=(x_cor,y_cor)
			# coords1_list.append(tmp)
	# #coords1_list.append((100,300))
	# #coords1_list.append((200,200))
	# #coords1_list.append((400,200))
	# #coords1_list.append((500,300))
	# #coords1_list.append((400,400))
	# #coords1_list.append((200,400))
	# print(coords1_list)		
	# polygon = Polygon(coords1_list)
	# patch = PolygonPatch(polygon, facecolor=[0,0,0], edgecolor=[0,0.5,0], alpha=0.7, zorder=2)
	# ax.add_patch(patch)
	# plt.savefig('sample_overlay.png', alpha=True, dpi=300)
	# plt.show()

	patch_size=2000
	OSobj = openslide.OpenSlide(arg.svs_file)
	x1=40000
	y1=37000
	img_patch = OSobj.read_region((x1,y1), 0, (patch_size, patch_size))
	img_data_np = np.array(img_patch)
	#img_name="sample3.png"
	#im = Image.fromarray(img_data_np)
	#im.save(img_name)
	
	
	
	# coords1_list=[]
	# # #for j in range(0,len(regions)):
	# for j in range(0,1):
		# coords1=regions[j]
		# for i in range(0,len(coords1)):
			# x_cor=int(coords1[i][0])-x1
			# y_cor=int(coords1[i][1])-y1
			# # # #print(str(x_cor)+" "+str(y_cor))
			# if x_cor >=0 and x_cor <= patch_size and y_cor >=0 and y_cor <=patch_size:
				# tmp=(x_cor,y_cor)
				# coords1_list.append(tmp)
	# # # print(coords1_list)		
	# polygon = Polygon(coords1_list)
	# # print(polygon)
	# # # # Create figure and axes
	# fig,ax = plt.subplots()
	# # # # Display the image
	# ax.imshow(img_data_np)
	
	# # # # Add the patch to the Axes
	# patch = PolygonPatch(polygon, facecolor=[0,0,0], edgecolor=[0,0.5,0], alpha=0.7, zorder=2)
	# ax.add_patch(patch)
	# plt.savefig('sample_overlay.png', alpha=True, dpi=300)
	# plt.show()
	
	# #ploting Steve's way
	# #plt.style.use('dark_background')
	# f, ax = plt.subplots(frameon=False)
	# #f.set_facecolor('#eafff5')
	# #ax.set_facecolor('#eafff5')
	# f.tight_layout(pad=0, h_pad=0, w_pad=0)
	# ax.set_xlim(0, patch_size)
	# ax.set_ylim(0, patch_size)
	# #img_data_np[np.where((img_data_np != [0,0,0]).all(axis = 2))] = [0,0,0]
	# #ax.imshow(img_data_np)
	# #mask1 = np.zeros(img_data_np.shape, dtype = "uint8")
	# #mask1.fill(0)
	# mask1 = Image.new('RGBA', (patch_size, patch_size), "black")
	# ax.imshow(mask1)
	# #ax.set_axis_bgcolor("black")
	# #patch = PolygonPatch(polygon, facecolor=[0,0,0], edgecolor=[0,0.5,0], alpha=0.7, zorder=2)
	# #patch = PolygonPatch(polygon, facecolor='#FFFFFF', edgecolor='#FFFFFF', alpha=0.7, zorder=2)
	# patch = PolygonPatch(polygon, facecolor='white')
	# ax.add_patch(patch)
	# ax.set_axis_off()
	# DPI = f.get_dpi()
	# plt.subplots_adjust(left=0, bottom=0, right=1, top=1,wspace=0, hspace=0)
	# f.set_size_inches(patch_size / DPI, patch_size / DPI)
	# f.savefig("Mask_tmp.png", pad_inches='tight')
	
	#create a binary mask
	#mask = np.zeros(img_data_np, dtype = "uint8")
	#cv2.rectangle(mask, (x1, y1), (x1+patch_size, y1+patch_size), (255, 255, 255), -1)
	
	#print(img_data_np)
	# flag = np.array([37500,38000, 0,0])
	# #flag = np.array([36000,27000])
	# #img_data_np=img_data_np+flag
	# #mask = np.zeros((700,700))
	# #print(regions[0])
	# a=finalcoords
	# a=np.int64(a)-flag
	# a = a[~np.all(a < 0, axis=1)]
	# a = a[~np.all(a > 10000, axis=1)]
	# #print("sucess")
	# #a2=a1[np.logical_and(a1>=0,a1<700)]
	# print(a)
	# sys.exit(1)
	# poly = Polygon(regions[0])
	# #img = Image.new('L', (700,700), 0)
	# #ImageDraw.Draw(img).polygon(poly, outline=1, fill=1)
	# mask = np.array((700,700))
	# # Create vertex coordinates for each grid cell...
	# # (<0,0> is at the top left of the grid in this system)
	# #x, y = np.meshgrid(np.arange(700), np.arange(700))
	# #x, y = x.flatten(), y.flatten()
	# #points = np.vstack((x,y)).T
	# #grid = points_inside_poly(points, poly)
	# #grid = grid.reshape((ny,nx))
	# print(poly)
	# cv2.fillPoly(mask, poly, 1)
	# mask = mask.astype(bool)
	# plt.imshow(mask)
	#print(Polygon(img_data_np).contains(poly_regions[0]))
	#xmax, ymax = a.max(axis=0)
	#print(img_data_np.shape)
	#a = Polygon(np.array([(0, 0), (1, 1), (1,2), (2,2)]))
	#b = Polygon(np.array([(0, 0), (1, 1), (2,1), (2,2)]))
	# patch_list=[]
	# x_n=300
	# y_n=300
	# size=x_n+y_n+x_n-2+y_n-2
	# list1=[]
	# n=0
	# for x in range(0,x_n):
		# tlist=[0+39000,x+34000]
		# list1.append(tlist)
	# for x in range(0,x_n):
		# tlist=[x_n-1+39000,x+34000]
		# list1.append(tlist)		
	# for x in range(1,y_n-1):
		# tlist=[x+39000,0+34000]
		# list1.append(tlist)
	# for x in range(1,y_n-1):
		# tlist=[x+39000,y_n-1+34000]
		# list1.append(tlist)
	
	path_poly=geo.box(x1, y1, x1+patch_size, y1+patch_size, ccw=True)
	# # path_poly=Polygon(np.array(list1))
	# # #path_poly=Polygon(np.array([[0, 0], [1, 0], [1, 1], [0, 1]]))
	# # print(path_poly)
	# # print(path_poly.is_valid)
	# # print(path_poly.length)
	# #print(poly_regions[0].is_valid)
	#print(len(poly_regions))
	poly_all=[]
	for j in range(0,len(poly_regions)):
		#print(j)
		poly1=path_poly.intersection(poly_regions[j])
		poly1_temp=[]
		if poly1.length > 0:
			for x,y in poly1.exterior.coords:
				x=int(x)-x1
				y=int(y)-y1
				tmp=(x,y)
				poly1_temp.append(tmp)
			poly1 = Polygon(poly1_temp)
			poly_all.append(poly1)
	#multi_poly = MultiPolygon(poly_all)
	#print(len(poly_all))
	#sys.exit(1)
	#ploting Steve's way
	#plt.style.use('dark_background')
	f, ax = plt.subplots(frameon=False)
	#ax.set_facecolor('#eafff5')
	f.tight_layout(pad=0, h_pad=0, w_pad=0)
	ax.set_xlim(0, patch_size)
	ax.set_ylim(0, patch_size)
	mask1 = Image.new('RGBA', (patch_size, patch_size), "black")
	ax.imshow(mask1)
	#patch1 = PolygonPatch(poly1, facecolor="white", edgecolor="white", alpha=0.7, zorder=2)
	for j in range(0,len(poly_all)):
		patch1 = PolygonPatch(poly_all[j], facecolor="white")
		ax.add_patch(patch1)
		
	ax.set_axis_off()
	DPI = f.get_dpi()
	plt.subplots_adjust(left=0, bottom=0, right=1, top=1,wspace=0, hspace=0)
	f.set_size_inches(patch_size / DPI, patch_size / DPI)
	f.savefig("Mask_tmp1.png", pad_inches='tight')
	
	#print(np_img)
	#img_patch = OSobj.read_region((current_x,current_y), level, (patch_size, patch_size))
	#img_data_np = np.array(img_patch)
	#img_name="sample3.png"
	#im = Image.fromarray(img_data_np)
	#im.save(img_name)
	#sys.exit(1)
	#'''itirating through the polygon object'''
	#for i in range(len(poly_regions)):
	#	poly = poly_regions[i]
	
	#obj = WsiSample(wsi_path=arg.svs_file, patch_size=patch_size, level=level)
	#for x,y in obj.get_targets(): # x and y are coordinates to extract from your OpenSlide Object
		#print(str(x)+" "+str(y))
		#img_patch = OSobj.read_region((x,y), level, (patch_size, patch_size))
		#img_data_np = np.array(img_patch)
		#img_name="sample2.png"
		#im = Image.fromarray(img_data_np)
		#im.save(img_name)	
		#sys.exit(0)	
	#sys.exit(1)	
		
def main():
	abspath=os.path.abspath(__file__)
	words = abspath.split("/")
	print("You are running XML annotation "+words[len(words) - 2])
	'''reading the config filename'''
	parser=argument_parse()
	arg=parser.parse_args()
	print("Entered Input XML annotation file "+arg.input_file+"\n")
	if not arg.output_file is None:
		print("Entered output file "+arg.output_file+"\n")
	print("Entered svs file "+arg.svs_file+"\n")
	print("Entered patch directory "+arg.patch_dir+"\n")
	print("TCGA Sample ID "+arg.tcgaid+"\n")
	
	xml = minidom.parse(arg.input_file)
	# The first region marked
	regions_ = xml.getElementsByTagName("Region")
	regions, region_labels = [], []
	#finalcoords = np.array([])
	x_cor=1
	for region in regions_:
		vertices = region.getElementsByTagName("Vertex")
		r_label = region.getAttribute('Id')
		region_labels.append(r_label)
		# Store x, y coordinates into a 2D array in format [x1, y1], [x2, y2], ...
		coords = np.zeros((len(vertices), 2))
		for i, vertex in enumerate(vertices):
			coords[i][0] = vertex.attributes['X'].value
			coords[i][1] = vertex.attributes['Y'].value
		#if x_cor==1:
		#	finalcoords=coords	
		#else:
		#	finalcoords= np.concatenate((finalcoords, coords), axis=0)
		regions.append(coords)
		
		
	'''coverting these regions to polygon objects and saving them to pickle'''
	poly_regions = []
	for i in range(len(region_labels)):
		poly = Polygon(regions[i])	
		poly_regions.append(poly)
		
	
	
	if not arg.output_file is None:	
		'''saving these objects to output'''	
		bn=os.path.basename(arg.input_file)
		bn_poly=arg.output_file+'/'+bn.replace('xml','pkl')
		save_object(poly_regions,bn_poly)
		'''saving the region labels'''
		bn_label=arg.output_file+'/'+bn.replace('xml','region.pkl')
		save_object(region_labels, bn_label)
		#with open('company_data.pkl', 'rb') as input:
		#company1 = pickle.load(input)
	
	'''Running the WSI sampler to identify patches with only tissues'''
	#wsi_path='/path/2/wsi.svs'
	patch_size =512
	level = 0
	patch_interval = 0.1
	threshold=200
	
	#patch_spacing = int(patch_size * patch_interval)
	#increment_patch = patch_size - patch_spacing
	OSobj = openslide.OpenSlide(arg.svs_file)
	'''Getting max x coordinate in this level'''
	max_level_0_x=int(OSobj.level_dimensions[0][0])
	'''Getting max y coordinate in this level'''
	max_level_0_y=int(OSobj.level_dimensions[0][1])
				
	'''Create output patch directories 1) original 2) binary'''
	original_patch_dir=arg.patch_dir+'/original'
	os.makedirs(original_patch_dir, exist_ok=True)
	binary_patch_dir=arg.patch_dir+'/binary'
	os.makedirs(binary_patch_dir, exist_ok=True)
	original_patch_dir_subpatch=arg.patch_dir+'/original_subpatch'
	os.makedirs(original_patch_dir_subpatch, exist_ok=True)
	binary_patch_dir_subpatch=arg.patch_dir+'/binary_subpatch'
	os.makedirs(binary_patch_dir_subpatch, exist_ok=True)
	
	
	
	'''Itirating through all the XML polygons'''
	for j in range(0,len(poly_regions)):
		#print(j)
		coords1=regions[j]
		min=np.argmin(coords1, axis = 0)
		max=np.argmax(coords1, axis = 0)
		min_x=int(coords1[min[0]][0])-patch_size
		min_y=int(coords1[min[1]][1])-patch_size
		max_x=int(coords1[max[0]][0])+patch_size
		max_y=int(coords1[max[1]][1])+patch_size
		full_patch_size_x=max_x-min_x
		full_patch_size_y=max_y-min_y
		size=full_patch_size_x*full_patch_size_y
		print("sample"+' '+arg.tcgaid+"_Region_"+str(j+1)+' '+"size"+' '+str(size)+' '+str(min_x)+' '+str(max_x)+' '+str(min_y)+' '+str(max_y)+' '+str(full_patch_size_x)+' '+str(full_patch_size_y))
		#continue
		num_patch="Name_"+arg.tcgaid+"_Region_"+str(j+1)+"_X_"+str(min_x)+"_"+str(max_x)+"_Y_"+str(min_y)+"_"+str(max_y)
		'''Adjustin polygon coordinates according to patch'''
		xml_ann_poly_all=[]
		'''Itirating through all the XML polygons'''
		for s in range(0,len(poly_regions)):
			poly1_temp=[]
			coords=regions[s]
			for i in range(0,len(coords)):
				x_cor=int(coords[i][0])-min_x
				y_cor=int(coords[i][1])-min_y
				if x_cor >=0 and x_cor <= full_patch_size_x and y_cor >=0 and y_cor <=full_patch_size_y:
					tmp=(x_cor,y_cor)
					poly1_temp.append(tmp)
			if len(poly1_temp) > 0:
				try:
					poly2 = Polygon(poly1_temp)
					xml_ann_poly_all.append(poly2)
				except:
					k=1
							
		'''creating binary mask'''				
		f_bin, ax_bin = plt.subplots(frameon=False)
		f_bin.tight_layout(pad=0, h_pad=0, w_pad=0)
		mask_bin = Image.new('RGBA', (full_patch_size_x, full_patch_size_y), "black")
		ax_bin.imshow(mask_bin)
		for i in range(0,len(xml_ann_poly_all)):
			patch1 = PolygonPatch(xml_ann_poly_all[i], facecolor="white")
			ax_bin.add_patch(patch1)
		ax_bin.set_xlim(0, full_patch_size_x)
		ax_bin.set_ylim(full_patch_size_y, 0)
		ax_bin.set_axis_off()
		DPI = f_bin.get_dpi()
		plt.subplots_adjust(left=0, bottom=0, right=1, top=1,wspace=0, hspace=0)
		#full_patch_size_y=300
		#full_patch_size_x=300
		f_bin.set_size_inches(full_patch_size_x / DPI, full_patch_size_y / DPI)
		tmp_png=binary_patch_dir+'/'+num_patch+'.png'
		f_bin.savefig(tmp_png, pad_inches='tight')
		plt.cla()
		plt.close(f_bin)
		#sys.exit(1)
		'''Reading the binary image'''		
		ann_Img_tmp = Image.open(tmp_png)
		M = np.array(ann_Img_tmp)
		print(np.unique(M.reshape(-1, M.shape[2]), axis=0,return_counts=True))
		#print(M.dtype)
		
		print(M.size)
		sys.exit(1)
		start_x=min_x	
		'''creating sub patches'''	
		'''Iterating through x coordinate'''	
		current_x=0
		#while current_x+patch_size < full_patch_size_x:
		while start_x+patch_size < max_x:
			'''Iterating through y coordinate'''
			current_y=0
			start_y=min_y
			#while current_y+patch_size < full_patch_size_y:
			while start_y+patch_size < max_y:
				num_patch="Name_"+arg.tcgaid+"_X_"+str(start_x)+"_"+str(start_x+patch_size)+"_Y_"+str(start_y)+"_"+str(start_y+patch_size)
				#num_patch="Name_"+arg.tcgaid+"_X_"+str(current_x)+"_"+str(current_x+patch_size)+"_Y_"+str(current_y)+"_"+str(current_y+patch_size)
				tmp_png=original_patch_dir_subpatch+'/'+num_patch+'.png'
				img_patch = OSobj.read_region((start_x,start_y), level, (patch_size, patch_size))
				np_img = np.array(img_patch)
				im_sub = Image.fromarray(np_img)
				width, height = im_sub.size
				'''Change to grey scale'''
				grey_img = im_sub.convert('L')
				'''Convert the image into numpy array'''
				np_grey = np.array(grey_img)
				'''Identify patched where there are tissues'''
				'''tuple where first element is rows, second element is columns'''
				idx = np.where(np_grey < threshold)
				'''proceed further only if patch has non empty values'''
				if len(idx[0])>0 and len(idx[1])>0 and width==patch_size and height==patch_size: 
					im_sub.save(tmp_png, "png")
					tmp_png=binary_patch_dir_subpatch+'/'+num_patch+'.png'
					print(str(current_y)+' '+str(current_y+patch_size)+' '+str(current_x)+' '+str(current_x+patch_size))
					t = M[current_y:current_y+patch_size,current_x:current_x+patch_size,:,]
					im_bin = Image.fromarray(t)
					im_bin.save(tmp_png, "png")
				start_y	= start_y+patch_size
				current_y = current_y+patch_size
			start_x = start_x+patch_size	
			current_x = current_x+patch_size
		sys.exit(1)

if __name__ == "__main__":
	main()
