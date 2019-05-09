#tfrecord='/data/WSI-Classification/records/spitz_train_00000-of-00004.tfrecord'
<<<<<<< HEAD
tfrecord_dir='/data/Naresh_Learning/data/BRCA_TCGA/tfrecords/Level2_selected'
#tfrecord_dir='/data/Naresh_Learning/data/BRCA_TCGA/tfrecords/Train'
#tfrecord_dir='/data/Naresh_Learning/data/BRCA_TCGA/tfrecords/Test'
=======
#tfrecord_dir='/data/Naresh_Learning/data/bh_bach/tfrecords/'
#tfrecord_dir='/data/Naresh_Learning/data/BRCA_TCGA/tfrecords/Train'
tfrecord_dir='/data/Naresh_Learning/data/BRCA_TCGA/tfrecords/Test'
>>>>>>> 51eda72cfb38934ba277cf5c08b6862b5d13ff7a
import tensorflow as tf
import io
import sys
from PIL import Image
import numpy as np
<<<<<<< HEAD
#tf_files=['bh_bach_train_bach.tfrecords','bh_bach_train_bh.tfrecords']
#tf_files=['bh_bach_val_bach.tfrecords','bh_bach_val_bh.tfrecords']
#tf_files=['TCGA-A1-A0SK.tfrecords','TCGA-AO-A03M.tfrecords']
#tf_files=['TCGA-A2-A0CT.tfrecords']
tf_files=['TCGA-BH-A0B1.gene_0.train.tfrecords']
=======
#tf_files=['bh_bach_val_bach.tfrecords','bh_bach_val_bh.tfrecords']
#tf_files=['TCGA-A1-A0SK.tfrecords','TCGA-AO-A03M.tfrecords']
tf_files=['TCGA-A2-A0CT.tfrecords']
>>>>>>> 51eda72cfb38934ba277cf5c08b6862b5d13ff7a
for i in tf_files:
	tfrecord=tfrecord_dir+'/'+i
	#print(tfrecord)
	#sys.exit(0)
	for example in tf.python_io.tf_record_iterator(tfrecord):
		result = tf.train.Example.FromString(example)
		for k,v in result.features.feature.items():
			if k == 'image/encoded':
				print(k, "Skipping...")
				#stream=io.BytesIO(v.bytes_list.value[0])
				#img = Image.open(stream)
				#img.save("sampletf.png", "png")
				#res = np.unique(np.asarray(img), return_counts=True)
				#print(k, res)
			elif k == 'image/segmentation/class/encoded':
				stream=io.BytesIO(v.bytes_list.value[0])
				img = Image.open(stream)
				res = np.unique(np.asarray(img), return_counts=True)
				#print(k, res)
			#elif k == 'phenotype/tumor_class':
			#	print(v.bytes_list.value[0])
			else:
				#k=1	
				try:
					print(k, v.bytes_list.value[0])
				except:
					print(k, v.int64_list.value[0])
		break
