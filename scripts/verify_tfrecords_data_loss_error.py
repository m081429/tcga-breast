# tfrecord='./tfrecord/train-00000-of-00004.tfrecord'

import tensorflow as tf
import io
from PIL import Image
import numpy as np
import sys

def test():
	k=1
	# for example in tf.python_io.tf_record_iterator(tfrecord):
		# result = tf.train.Example.FromString(example)
		# for k,v in result.features.feature.items():
			# if k == 'image/encoded':
				# print(k, "Skipping...")
			# elif k == 'image/segmentation/class/encoded':
				# stream=io.BytesIO(v.bytes_list.value[0])
				# img = Image.open(stream)
				# res = np.unique(np.asarray(img), return_counts=True)
				# print(k, res)
			# else:
				# try:
					# print(k, v.bytes_list.value[0])
				# except:
					# print(k, v.int64_list.value[0])
		# break

	# record_iterator = tf.python_io.tf_record_iterator(path=data_path)
	# for string_record in record_iterator:
		# example = tf.train.Example()
		# example.ParseFromString(string_record)
		# height = int(example.features.feature['image/height'].int64_list.value[0])
		# width = int(example.features.feature['image/width'].int64_list.value[0])
		# img_name = example.features.feature['image/filename'].bytes_list.value[0]
		# img_string = example.features.feature['image/encoded'].bytes_list.value[0]
		# label_text = example.features.feature['image/object/class/text'].bytes_list.value[0]
		# xmin_list = example.features.feature['image/object/bbox/xmin'].float_list.value
		# xmax_list = example.features.feature['image/object/bbox/xmax'].float_list.value
		# ymin_list = example.features.feature['image/object/bbox/ymin'].float_list.value
		# ymax_list = example.features.feature['image/object/bbox/ymax'].float_list.value
		# recovered_img = tf.image.decode_jpeg(img_string, channels=0)
		# with tf.Session() as sess:
			# coord = tf.train.Coordinator()
			# threads = tf.train.start_queue_runners(coord=coord)
			# image = sess.run(recovered_img)
			# coord.request_stop()
			# coord.join(threads)
		# print(img_name)
		# # img = Image.fromarray(image, mode="RGB")
		# # img.save("test.jpg")
		# plt.imshow(image)
		# plt.show()
	

def _parse_function_for_train(example_proto):
	features = {'image': tf.FixedLenFeature((), tf.string, default_value=""),
	'label': tf.FixedLenFeature((), tf.string, default_value="")}
	parsed_features = tf.parse_single_example(example_proto, features)
	image_raw_out = parsed_features['image']
	label_raw_out = parsed_features['label']
	image_out = tf.decode_raw(image_raw_out, tf.uint8)
	label_out = tf.decode_raw(label_raw_out, tf.float32)
	image_out = tf.reshape(image_out, [512, 512, 3])
	label_out = tf.reshape(label_out, [512, 512, 1])
	return image_out, label_out

def CreateTrainDataset():
	train_image_label_tfrecord_list = ["./tfrecord/train-00000-of-00004.tfrecord","./tfrecord/train-00001-of-00004.tfrecord","./tfrecord/train-00002-of-00004.tfrecord","./tfrecord/train-00003-of-00004.tfrecord","./tfrecord/trainval-00000-of-00004.tfrecord","./tfrecord/trainval-00001-of-00004.tfrecord","./tfrecord/trainval-00002-of-00004.tfrecord","./tfrecord/trainval-00003-of-00004.tfrecord","./tfrecord/val-00000-of-00004.tfrecord","./tfrecord/val-00001-of-00004.tfrecord","./tfrecord/val-00002-of-00004.tfrecord","./tfrecord/val-00003-of-00004.tfrecord"]
	train_dataset = tf.contrib.data.TFRecordDataset(train_image_label_tfrecord_list)
	train_dataset = train_dataset.map(_parse_function_for_train)
	batched_train_dataset = train_dataset.batch(512)
	return batched_train_dataset
	
def test():
	batched_train_dataset = CreateTrainDataset()
	iterator = batched_train_dataset.make_initializable_iterator()
	batch_image, batch_label = iterator.get_next()
	with tf.Session() as sess:
		sess.run(iterator.initializer)

def validate_dataset(filenames, reader_opts=None):
	"""
	Attempt to iterate over every record in the supplied iterable of TFRecord filenames
	:param filenames: iterable of filenames to read
	:param reader_opts: (optional) tf.python_io.TFRecordOptions to use when constructing the record iterator
	"""
	for fname in filenames:
		print('validating ', fname)
		record_iterator = tf.python_io.tf_record_iterator(path=fname, options=reader_opts)
		img_name=""
		try:
			for string_record in record_iterator:
				example = tf.train.Example()
				example.ParseFromString(string_record)
				img_name = example.features.feature['image/name'].bytes_list.value[0]
		except Exception as e:
			print('error in {} at record {}'.format(fname, img_name))
			print(e)		

def main():
	#train_image_label_tfrecord_list = ["./tfrecord/train-00000-of-00004.tfrecord","./tfrecord/train-00001-of-00004.tfrecord","./tfrecord/train-00002-of-00004.tfrecord","./tfrecord/train-00003-of-00004.tfrecord","./tfrecord/trainval-00000-of-00004.tfrecord","./tfrecord/trainval-00001-of-00004.tfrecord","./tfrecord/trainval-00002-of-00004.tfrecord","./tfrecord/trainval-00003-of-00004.tfrecord","./tfrecord/val-00000-of-00004.tfrecord","./tfrecord/val-00001-of-00004.tfrecord","./tfrecord/val-00002-of-00004.tfrecord","./tfrecord/val-00003-of-00004.tfrecord"]
	train_image_label_tfrecord_list = []
	fobj = open("tfrecord.txt")
	for file in fobj:
		file=file.strip()
		train_image_label_tfrecord_list.append(file)
	fobj.close()
	#print(train_image_label_tfrecord_list)
	#sys.exit(1)
	validate_dataset(train_image_label_tfrecord_list)
		
if __name__ == "__main__":
	main()