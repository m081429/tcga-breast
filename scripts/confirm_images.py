#tfrecord='/data/WSI-Classification/records/spitz_train_00000-of-00004.tfrecord'
tfrecord_dir='/data/Naresh_Learning/scripts/patches1/tfrecord.txt'
import tensorflow as tf
import io
import sys
from PIL import Image
import numpy as np

fobj = open(tfrecord_dir)
myfile = open('/data/Naresh_Learning/scripts/patches1/tfrecord_image.txt', mode='wt')
fobj.readline()
for file in fobj:
	file = file.strip()
	p = file.split("\t")
	#myfile.write(p[0]+"\t"+p[1]+"\t"+p[2]+"\t"+p[3]+"\t"+avg+"\n")
	
	ann_Img_tmp = Image.open(p[0])
	M = np.array(ann_Img_tmp)
	
	myfile.write(p[0]+ ' '+str(M.shape[0])+ ' '+str(M.shape[1])+ ' '+str(M.shape[2])+"\n")
	#sys.exit(0)
fobj.close()
myfile.close()
