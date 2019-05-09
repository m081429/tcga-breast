#!/usr/local/biotools/python/3.4.3/bin/python3
__author__ = "Naresh Prodduturi"
__email__ = "prodduturi.naresh@mayo.edu"
__status__ = "Dev"

import os
import argparse
import sys
import pwd
import time
import subprocess
import re
import shutil
import glob	
import openslide
import numpy as np
from PIL import Image, ImageDraw
import tensorflow as tf
import io
from dataset_utils import * 
'''function to check if input files exists and valid''' 	
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
	parser.add_argument("-p","--patch_dir",help="Patch dir",required="True")
	parser.add_argument("-i","--input_file",help="input file",required="True")
	parser.add_argument("-o","--tf_output",help="output tf dir",required="True")
	parser.add_argument("-s","--patch_size",help="Patch_size",required="True")
	return parser


  
def create_patch(svs,patch_sub_size,patch_dir,samp,p,tf_output):
	tf_writer=tf.python_io.TFRecordWriter(tf_output+'/'+p[2]+'/'+samp+'.tfrecords')
	threshold=200
	level=0
	OSobj = openslide.OpenSlide(svs)
	minx = 0
	miny = 0
	maxx = OSobj.dimensions[0]
	maxy = OSobj.dimensions[1]
	#print(svs+' '+str(patch_sub_size)+' '+patch_dir+' '+str(maxx))
	start_x=minx	
	'''creating sub patches'''	
	'''Iterating through x coordinate'''	
	current_x=0
	filenames=[]
	while start_x+patch_sub_size < maxx:
		'''Iterating through y coordinate'''
		current_y=0
		start_y=miny
		while start_y+patch_sub_size < maxy:
			img_patch = OSobj.read_region((start_x,start_y), level, (patch_sub_size, patch_sub_size))
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
			if len(idx[0])>0 and len(idx[1])>0 and width==patch_sub_size and height==patch_sub_size:
				'''creating patch name'''
				num_patch=samp+"_X_"+str(start_x)+"_"+str(start_x+patch_sub_size)+"_Y_"+str(start_y)+"_"+str(start_y+patch_sub_size)
				#filenames.append(num_patch)
				#tmp_png=patch_dir+'/'+num_patch+'.png'
				'''saving image'''
				#im_sub.save(tmp_png, "png")
				#sys.exit(1)
				image_format="png"    
				height=224
				width=224  
				image_name=num_patch     
				age_at_initial_pathologic_diagnosis=p[4]
				gender=p[5]
				race=p[6]
				ajcc_pathologic_tumor_stage=p[7]
				histological_type=p[8]
				initial_pathologic_dx_year=p[9]
				menopause_status=p[10]
				birth_days_to=p[11]
				vital_status=p[12]
				tumor_status=p[13]
				last_contact_days_to=p[14]
				death_days_to=p[15]
				new_tumor_event_type=p[16]
				margin_status=p[17]
				OS=p[18]
				OS_time=p[19]
				DSS=p[20]
				DSS_time=p[21]
				DFI=p[22]
				DFI_time=p[23]
				PFI=p[24]
				PFI_time=p[25]
				ER_Status=p[26]
				PR_Status=p[27]
				HER2_Final_Status=p[28]
				Node_Coded=p[29]
				Metastasis_Coded=p[30]
				PAM50_mRNA=p[31]
				SigClust_Unsupervised_mRNA=p[32]
				SigClust_Intrinsic_mRNA=p[33]
				miRNA_Clusters=p[34]
				methylation_Clusters=p[35]
				RPPA_Clusters=p[36]
				CN_Clusters=p[37]
				ATM_Mutations=int(p[38])
				BRCA1_Mutations=int(p[39])
				BRCA2_Mutations=int(p[40])
				BARD1_Mutations=int(p[41])
				BRIP1_Mutations=int(p[42])
				CDH1_Mutations=int(p[43])
				CDKN2A_Mutations=int(p[44])
				CHEK2_Mutations=int(p[45])
				MLH1_Mutations=int(p[46])
				MSH2_Mutations=int(p[47])
				MSH6_Mutations=int(p[48])
				PALB2_Mutations=int(p[49])
				PTEN_Mutations=int(p[50])
				RAD51C_Mutations=int(p[51])
				RAD51D_Mutations=int(p[52])
				TP53_Mutations=int(p[53])
				AnyGene_Mutations=int(p[54])
				GermlineMutation=int(p[55])

				imgByteArr = io.BytesIO()
				im_sub.save(imgByteArr, format='PNG')
				imgByteArr = imgByteArr.getvalue()
				record=image_to_tfexample_tcga(imgByteArr,image_format,int(height),int(width),image_name, \
				age_at_initial_pathologic_diagnosis, \
				gender, \
				race, \
				ajcc_pathologic_tumor_stage, \
				histological_type, \
				initial_pathologic_dx_year, \
				menopause_status, \
				birth_days_to, \
				vital_status, \
				tumor_status, \
				last_contact_days_to, \
				death_days_to, \
				new_tumor_event_type, \
				margin_status, \
				OS, \
				OS_time, \
				DSS, \
				DSS_time, \
				DFI, \
				DFI_time, \
				PFI, \
				PFI_time, \
				ER_Status, \
				PR_Status, \
				HER2_Final_Status, \
				Node_Coded, \
				Metastasis_Coded, \
				PAM50_mRNA, \
				SigClust_Unsupervised_mRNA, \
				SigClust_Intrinsic_mRNA, \
				miRNA_Clusters, \
				methylation_Clusters, \
				RPPA_Clusters, \
				CN_Clusters, \
				ATM_Mutations, \
				BRCA1_Mutations, \
				BRCA2_Mutations, \
				BARD1_Mutations, \
				BRIP1_Mutations, \
				CDH1_Mutations, \
				CDKN2A_Mutations, \
				CHEK2_Mutations, \
				MLH1_Mutations, \
				MSH2_Mutations, \
				MSH6_Mutations, \
				PALB2_Mutations, \
				PTEN_Mutations, \
				RAD51C_Mutations, \
				RAD51D_Mutations, \
				TP53_Mutations, \
				AnyGene_Mutations, \
				GermlineMutation)
				tf_writer.write(record.SerializeToString())
			start_y	= start_y+patch_sub_size
			current_y = current_y+patch_sub_size
		start_x = start_x+patch_sub_size	
		current_x = current_x+patch_sub_size	
	#sys.exit(1)
	tf_writer.close()
	return filenames
	
def main():	
	abspath=os.path.abspath(__file__)
	words = abspath.split("/")
	'''reading the config filename'''
	parser=argument_parse()
	arg=parser.parse_args()
	'''printing the config param'''
	print("Entered INPUT Filename "+arg.input_file)
	print("Entered Output Patch Directory "+arg.patch_dir)
	print("Entered Output TF Directory "+arg.tf_output)
	print("Entered Patch size "+arg.patch_size)

	patch_sub_size=int(arg.patch_size)
	patch_dir=arg.patch_dir
	tf_output=arg.tf_output
	'''Reading TCGA file'''
	fobj = open(arg.input_file)
	#myfile = open(arg.output_file, mode='wt')
	#myfile.write("TCGA_NAME\tSVS_FILE\tSET_NAME\t"+header_val+"\n")
	header = fobj.readline()
	for file in fobj:
		file = file.strip()
		p = file.split("\t")
		samp=p[0]
		svs_file=p[1]
		set=p[2]
		filenames=create_patch(svs_file,patch_sub_size,patch_dir,samp,p,tf_output)
		#print(str(len(filenames)))
		sys.exit(1)
		# if not p[0] in pheno_Set:
			# print(p[0]+' '+" no pheno set")
			# sys.exit(1)
		# if not p[0] in pheno_file:
			# print(p[0]+' '+" no pheno file")
			# sys.exit(1)	
		#if p[0] in pheno_Set and p[0] in pheno_file:
		#	myfile.write(p[0]+"\t"+p[1]+"\t"+pheno_Set[p[0]]+"\t"+pheno_file[p[0]]+"\n")
	fobj.close()
	myfile.close()

	
if __name__ == "__main__":
	main()