# Copyright 2016 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Contains utilities for downloading and converting datasets."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import sys
import tarfile

import tensorflow as tf

_LABELS_FILENAME = 'labels.txt'
_PREFIX = 'AnyGene_Mutations'

def int64_feature(values):
  """Returns a TF-Feature of int64s.

  Args:
    values: A scalar or list of values.

  Returns:
    A TF-Feature.
  """
  if not isinstance(values, (tuple, list)):
    values = [values]
  return tf.train.Feature(int64_list=tf.train.Int64List(value=values))


def bytes_feature(values):
  """Returns a TF-Feature of bytes.

  Args:
    values: A string.

  Returns:
    A TF-Feature.
  """
  return tf.train.Feature(bytes_list=tf.train.BytesList(value=[values]))


def float_feature(values):
  """Returns a TF-Feature of floats.

  Args:
    values: A scalar of list of values.

  Returns:
    A TF-Feature.
  """
  if not isinstance(values, (tuple, list)):
    values = [values]
  return tf.train.Feature(float_list=tf.train.FloatList(value=values))


def image_to_tfexample(image_data, image_format, height, width, image_name,
			race=None,
			ajcc_pathologic_tumor_stage=None,
			pam50_mRNA=None,
			histological_type=None,
			tissue_pathology=None,
			tumor_class=None,
			tumor_status=None,
			DeadInFiveYrs=None,
			ER_Status=None,
			PR_Status=None,
			HER2_Status=None,
			Metastasis_Coded=None,
			ATM_Mutations=0,
			BRCA1_Mutations=0,
			BRCA2_Mutations=0,
			CDH1_Mutations=0,
			CDKN2A_Mutations=0,
			PTEN_Mutations=0,
			TP53_Mutations=0,
			AnyGene_Mutations=0
			):
  return tf.train.Example(features=tf.train.Features(feature={
      'image/encoded': bytes_feature(image_data),
      'image/format': bytes_feature(image_format),
      'image/name': bytes_feature(image_name),
      'image/height': int64_feature(height),
      'image/width': int64_feature(width),
      'phenotype/race': int64_feature(race),
      'phenotype/ajcc_pathologic_tumor_stage': int64_feature(ajcc_pathologic_tumor_stage),
      'phenotype/pam50_mRNA': int64_feature(pam50mRNA),
      'phenotype/histological_type': int64_feature(histological_type),
      'phenotype/tissue_pathology': int64_feature(tissue_pathology),
      'phenotype/tumor_class': int64_feature(tumor_class),
      'phenotype/tumor_status': int64_feature(tumor_status),
      'phenotype/DeadInFiveYrs': int64_feature(DeadInFiveYrs),
      'phenotype/ER_Status': int64_feature(ER_Status),
      'phenotype/PR_Status': int64_feature(PR_Status),
      'phenotype/HER2_Status': int64_feature(HER2_Status),
      'phenotype/Metastasis_Coded': int64_feature(Metastasis_Coded),
      'phenotype/ATM_Mutations': int64_feature(ATM_Mutations),
      'phenotype/BRCA1_Mutations': int64_feature(BRCA1_Mutations),
      'phenotype/BRCA2_Mutations': int64_feature(BRCA2_Mutations),
      'phenotype/CDH1_Mutations': int64_feature(CDH1_Mutations),
      'phenotype/CDKN2A_Mutations': int64_feature(CDKN2A_Mutations),
      'phenotype/PTEN_Mutations': int64_feature(PTEN_Mutations),
      'phenotype/TP53_Mutations': int64_feature(TP53_Mutations),
      'phenotype/AnyGene_Mutations': int64_feature(AnyGene_Mutations),

  }))


def image_to_tfexample_step1(image_data, image_format, height, width, image_name,
                        histological_type=None,
                        tissue_pathology=None,
                        tumor_class=None
                                                ):
  return tf.train.Example(features=tf.train.Features(feature={
      'image/encoded': bytes_feature(image_data),
<<<<<<< HEAD
      'image/format': bytes_feature(image_format.encode('utf8')),
      'image/name': bytes_feature(image_name.encode('utf8')),
=======
      'image/format': bytes_feature(image_format),
      'image/name': bytes_feature(image_name),
>>>>>>> upstream/master
      'image/height': int64_feature(height),
      'image/width': int64_feature(width),
      'phenotype/histological_type': int64_feature(histological_type),
      'phenotype/tissue_pathology': int64_feature(tissue_pathology),
      'phenotype/tumor_class': int64_feature(tumor_class)

  }))
<<<<<<< HEAD
def read_label_file(dataset_dir, filename):
=======


 read_label_file(dataset_dir, filename=LABELS_FILENAME):
>>>>>>> upstream/master
  """Reads the labels file and returns a mapping from ID to class name.

  Args:
    dataset_dir: The directory in which the labels file is found.
    filename: The filename where the class names are written.

  Returns:
    A map from a label (integer) to class name.
  """
  labels_filename = os.path.join(dataset_dir, filename)
  with tf.gfile.Open(labels_filename, 'rb') as f:
    lines = f.read().decode()
  lines = lines.split('\n')
  lines = filter(None, lines)

  labels_to_class_names = {}
  for line in lines:
    index = line.index(':')
    labels_to_class_names[int(line[:index])] = line[index+1:]
  return labels_to_class_names
