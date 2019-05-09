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
	parser.add_argument("-p","--pheno",help="input file",required="True",type=input_file_validity)
	parser.add_argument("-s","--pheno_set",help="Database dir",required="True")
	parser.add_argument("-t","--tcga",help="catalog Name",required="True")
	parser.add_argument("-o","--output_file",help="output_file",required="True")
	return parser

	
def main():	
	abspath=os.path.abspath(__file__)
	words = abspath.split("/")
	'''reading the config filename'''
	parser=argument_parse()
	arg=parser.parse_args()
	'''printing the config param'''
	print("Entered Pheno file "+arg.pheno)
	print("Entered Pheno_set "+arg.pheno_set)
	print("Entered TCGA Filename "+arg.tcga)
	print("Entered Output file "+arg.output_file)
	
	'''Reading phenotype with set file'''
	pheno_Set={}
	fobj = open(arg.pheno_set)
	header = fobj.readline()
	header = header.strip()
	for file in fobj:
		file = file.strip()
		p = file.split(",")
		p[0] = p[0].replace('"','')
		p[29] = p[29].replace('"','')
		pheno_Set[p[0]]=p[29]
	fobj.close()
	
	'''Reading phenotype file'''
	pheno_file={}
	fobj = open(arg.pheno)
	header = fobj.readline()
	header = header.strip()
	p = header.split("\t")
	header_val=str.join("\t",p[1:])
	for file in fobj:
		file = file.strip()
		file = file.replace('"','')
		file = file.replace('\r','')
		p = file.split("\t")
		key=p[0]
		val=str.join("\t",p[1:])
		pheno_file[key]=val
	fobj.close()
	
	'''Reading TCGA file'''
	fobj = open(arg.tcga)
	myfile = open(arg.output_file, mode='wt')
	myfile.write("TCGA_NAME\tSVS_FILE\tSET_NAME\t"+header_val+"\n")
	for file in fobj:
		file = file.strip()
		p = file.split("\t")
		# if not p[0] in pheno_Set:
			# print(p[0]+' '+" no pheno set")
			# sys.exit(1)
		# if not p[0] in pheno_file:
			# print(p[0]+' '+" no pheno file")
			# sys.exit(1)	
		if p[0] in pheno_Set and p[0] in pheno_file:
			myfile.write(p[0]+"\t"+p[1]+"\t"+pheno_Set[p[0]]+"\t"+pheno_file[p[0]]+"\n")
	fobj.close()
	myfile.close()

	
if __name__ == "__main__":
	main()