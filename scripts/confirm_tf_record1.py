tfrecord_dir='/data/Naresh_Learning/data/BRCA_TCGA/tfrecords/Level2'
import tensorflow as tf
import io
import sys
import os
from PIL import Image
import numpy as np
tf_files=os.listdir(tfrecord_dir)
num_samples = 0
for i in tf_files:
	if 'TCGA' in i:
		num_samples = 0
		tfrecord=tfrecord_dir+'/'+i
		try:
			for example in tf.python_io.tf_record_iterator(tfrecord):
				result = tf.train.Example.FromString(example)
				num_samples =num_samples+1
			print(i+' '+str(num_samples))
		except Exception as e:
			print(i+' '+str(e.__doc__)+' '+str(e.message))
				
