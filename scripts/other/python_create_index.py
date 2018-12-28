import random
import os
import argparse
import sys
import pwd
import time
import subprocess
import re
import shutil
from scipy import stats

def main():
	'''opening samples'''
	train={}
	trainval={}
	val={}
	fobj = open("sample_names_sorted_num_patch_new.txt")
	ntv=1
	nv=1
	for file in fobj:
		file = file.strip()
		# p = file.split("\t")
		num=random.randint(0,100)
		#print(num)
		if num>80 and nv<18:
			nv=nv+1
			val[file]=1
		elif num>60 and ntv<16:
			trainval[file]=1
			ntv=ntv+1
		else:
			train[file]=1
	fobj.close()	
	print(len(val))
	print(len(trainval))	
	print(len(train))
	fobj = open("All_subpatch_ori_new.txt")
	myfile1 = open("./patches/index/val.txt", mode='wt')
	myfile2 = open("./patches/index/trainval.txt", mode='wt')
	myfile3 = open("./patches/index/train.txt", mode='wt')
	for file in fobj:
		file = file.strip()
		file=file.replace(".png", "")
		p = file.split("_")
		if p[1] in val:
			myfile1.write(file+"\n")
		elif p[1] in trainval:
			myfile2.write(file+"\n")
		elif p[1] in train:
			myfile3.write(file+"\n")
		else:
			print(file)
			sys.exit(1)
	fobj.close()
	myfile1.close()
	myfile2.close()
	myfile3.close()	
if __name__ == "__main__":
	main()
