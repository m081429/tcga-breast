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
import numpy as np
from PIL import Image, ImageDraw
def main():

	'''opening samples'''
	fobj = open("All_subpatch_ori.txt")
	myfile = open("python_check_bin_patches.txt", mode='wt')
	for file in fobj:
		file = file.strip()
		try:
			tmp_png1='./patches/binary_subpatch/'+file
			ann_Img_tmp = Image.open(tmp_png1)
			M = np.array(ann_Img_tmp)
			tmp_png2='./patches/original_subpatch/'+file
			ann_Img_tmp2 = Image.open(tmp_png2)
			M1 = np.array(ann_Img_tmp2)
			myfile.write(file+"\t"+str(M.shape[0])+"\t"+str(M.shape[1])+"\t"+str(M.size)+"\t"+str(M1.shape[0])+"\t"+str(M1.shape[1])+"\t"+str(M1.size)+"\n")
		except:
			myfile.write(file+"\n")
			pass
	fobj.close()
	myfile.close()	
if __name__ == "__main__":
	main()