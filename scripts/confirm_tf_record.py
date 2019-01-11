#tfrecord='/data/WSI-Classification/records/spitz_train_00000-of-00004.tfrecord'
tfrecord_dir='/data/Naresh_Learning/scripts/patches1/tfrecord'
import tensorflow as tf
import io
import sys
from PIL import Image
import numpy as np
tf_files=['bh_bach_train_bach.tfrecords','bh_bach_train_bh.tfrecords','bh_bach_val_bach.tfrecords','bh_bach_val_bh.tfrecords']
for i in tf_files:
	tfrecord=tfrecord_dir+'/'+i
	#print(tfrecord)
	#sys.exit(0)
	for example in tf.python_io.tf_record_iterator(tfrecord):
		result = tf.train.Example.FromString(example)
		for k,v in result.features.feature.items():
			if k == 'image/encoded':
				print(k, "Skipping...")
			elif k == 'image/segmentation/class/encoded':
				stream=io.BytesIO(v.bytes_list.value[0])
				img = Image.open(stream)
				res = np.unique(np.asarray(img), return_counts=True)
				print(k, res)
			else:
				try:
					print(k, v.bytes_list.value[0])
				except:
					print(k, v.int64_list.value[0])
	#break
