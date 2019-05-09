#tfrecord='/data/WSI-Classification/records/spitz_train_00000-of-00004.tfrecord'
#tfrecord_dir='/data/Naresh_Learning/data/bh_bach/tfrecords/'
#tfrecord_dir='/data/Naresh_Learning/data/BRCA_TCGA/tfrecords/Train'
tfrecord_dir='/data/Naresh_Learning/data/BRCA_TCGA/tfrecords/Test'
import tensorflow as tf
import io
import sys
from PIL import Image
import numpy as np
#tf_files=['bh_bach_train_bach.tfrecords','bh_bach_train_bh.tfrecords']
#tf_files=['bh_bach_val_bach.tfrecords','bh_bach_val_bh.tfrecords']
#tf_files=['TCGA-A1-A0SK.tfrecords','TCGA-AO-A03M.tfrecords']
tf_files=['TCGA-A2-A0CT.tfrecords']
#tf_files=['bh_bach_val_bach.tfrecords']
fobj=open("k2.txt")
for i in tf_files:
	tfrecord=tfrecord_dir+'/'+i
	#print(tfrecord)
	#sys.exit(0)
	for example in tf.python_io.tf_record_iterator(tfrecord):
		result = tf.train.Example.FromString(example)
		for k,v in result.features.feature.items():
			if k == 'image/encoded':
				line=fobj.readline()
				line=line.strip()
				print(line)
				if line == '[0]':
					print(k, "Skipping...")
					stream=io.BytesIO(v.bytes_list.value[0])
					img = Image.open(stream)
					img.save("sampletf.png", "png")
					res = np.unique(np.asarray(img), return_counts=True)
					print(k, res)
					sys.exit(1)
			elif k == 'image/segmentation/class/encoded':
				stream=io.BytesIO(v.bytes_list.value[0])
				img = Image.open(stream)
				res = np.unique(np.asarray(img), return_counts=True)
				#print(k, res)
			#elif k == 'phenotype/tumor_class':
			#	print(v.bytes_list.value[0])
			else:
				k=1	
				#try:
				#	print(k, v.bytes_list.value[0])
				#except:
				#	print(k, v.int64_list.value[0])
		#break
