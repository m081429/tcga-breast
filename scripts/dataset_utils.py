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


def image_to_tfexample_tcga(image_data, image_format, height, width, image_name,
                        age_at_initial_pathologic_diagnosis=None,
                        gender=None,
                        race=None,
                        ajcc_pathologic_tumor_stage=None,
                        histological_type=None,
                        initial_pathologic_dx_year=None,
                        menopause_status=None,
                        birth_days_to=None,
                        vital_status=None,
                        tumor_status=None,
                        last_contact_days_to=None,
                        death_days_to=None,
                        new_tumor_event_type=None,
                        margin_status=None,
                        OS=None,
                        OS_time=None,
                        DSS=None,
                        DSS_time=None,
                        DFI=None,
                        DFI_time=None,
                        PFI=None,
                        PFI_time=None,
                        ER_Status=None,
                        PR_Status=None,
                        HER2_Final_Status=None,
                        Node_Coded=None,
                        Metastasis_Coded=None,
                        PAM50_mRNA=None,
                        SigClust_Unsupervised_mRNA=None,
                        SigClust_Intrinsic_mRNA=None,
                        miRNA_Clusters=None,
                        methylation_Clusters=None,
                        RPPA_Clusters=None,
                        CN_Clusters=None,
                        ATM_Mutations=None,
                        BRCA1_Mutations=None,
                        BRCA2_Mutations=None,
                        BARD1_Mutations=None,
                        BRIP1_Mutations=None,
                        CDH1_Mutations=None,
                        CDKN2A_Mutations=None,
                        CHEK2_Mutations=None,
                        MLH1_Mutations=None,
                        MSH2_Mutations=None,
                        MSH6_Mutations=None,
                        PALB2_Mutations=None,
                        PTEN_Mutations=None,
                        RAD51C_Mutations=None,
                        RAD51D_Mutations=None,
                        TP53_Mutations=None,
                        AnyGene_Mutations=None,
                        GermlineMutation=None
                                                ):
  return tf.train.Example(features=tf.train.Features(feature={
      'image/encoded': bytes_feature(image_data),
      'image/format': bytes_feature(image_format.encode('utf8')),
      'image/name': bytes_feature(image_name.encode('utf8')),
      'image/height': int64_feature(height),
      'image/width': int64_feature(width),
      'phenotype/histological_type': bytes_feature(histological_type.encode('utf8')),
      'phenotype/age_at_initial_pathologic_diagnosis': bytes_feature(age_at_initial_pathologic_diagnosis.encode('utf8')),
      'phenotype/gender': bytes_feature(gender.encode('utf8')),
      'phenotype/race': bytes_feature(race.encode('utf8')),
      'phenotype/ajcc_pathologic_tumor_stage': bytes_feature(ajcc_pathologic_tumor_stage.encode('utf8')),
      'phenotype/histological_type': bytes_feature(histological_type.encode('utf8')),
      'phenotype/initial_pathologic_dx_year': bytes_feature(initial_pathologic_dx_year.encode('utf8')),
      'phenotype/menopause_status': bytes_feature(menopause_status.encode('utf8')),
      'phenotype/birth_days_to': bytes_feature(birth_days_to.encode('utf8')),
      'phenotype/vital_status': bytes_feature(vital_status.encode('utf8')),
      'phenotype/tumor_status': bytes_feature(tumor_status.encode('utf8')),
      'phenotype/last_contact_days_to': bytes_feature(last_contact_days_to.encode('utf8')),
      'phenotype/death_days_to': bytes_feature(death_days_to.encode('utf8')),
      'phenotype/new_tumor_event_type': bytes_feature(new_tumor_event_type.encode('utf8')),
      'phenotype/margin_status': bytes_feature(margin_status.encode('utf8')),
      'phenotype/OS': bytes_feature(OS.encode('utf8')),
      'phenotype/OS_time': bytes_feature(OS_time.encode('utf8')),
      'phenotype/DSS': bytes_feature(DSS.encode('utf8')),
      'phenotype/DSS_time': bytes_feature(DSS_time.encode('utf8')),
      'phenotype/DFI': bytes_feature(DFI.encode('utf8')),
      'phenotype/DFI_time': bytes_feature(DFI_time.encode('utf8')),
      'phenotype/PFI': bytes_feature(PFI.encode('utf8')),
      'phenotype/PFI_time': bytes_feature(PFI_time.encode('utf8')),
      'phenotype/ER_Status': bytes_feature(ER_Status.encode('utf8')),
      'phenotype/PR_Status': bytes_feature(PR_Status.encode('utf8')),
      'phenotype/HER2_Final_Status': bytes_feature(HER2_Final_Status.encode('utf8')),
      'phenotype/Node_Coded': bytes_feature(Node_Coded.encode('utf8')),
      'phenotype/Metastasis_Coded': bytes_feature(Metastasis_Coded.encode('utf8')),
      'phenotype/PAM50_mRNA': bytes_feature(PAM50_mRNA.encode('utf8')),
      'phenotype/SigClust_Unsupervised_mRNA': bytes_feature(SigClust_Unsupervised_mRNA.encode('utf8')),
      'phenotype/SigClust_Intrinsic_mRNA': bytes_feature(SigClust_Intrinsic_mRNA.encode('utf8')),
      'phenotype/miRNA_Clusters': bytes_feature(miRNA_Clusters.encode('utf8')),
      'phenotype/methylation_Clusters': bytes_feature(methylation_Clusters.encode('utf8')),
      'phenotype/RPPA_Clusters': bytes_feature(RPPA_Clusters.encode('utf8')),
      'phenotype/CN_Clusters': bytes_feature(CN_Clusters.encode('utf8')),
      'phenotype/ATM_Mutations': int64_feature(ATM_Mutations),
      'phenotype/BRCA1_Mutations': int64_feature(BRCA1_Mutations),
      'phenotype/BRCA2_Mutations': int64_feature(BRCA2_Mutations),
      'phenotype/BARD1_Mutations': int64_feature(BARD1_Mutations),
      'phenotype/BRIP1_Mutations': int64_feature(BRIP1_Mutations),
      'phenotype/CDH1_Mutations': int64_feature(CDH1_Mutations),
      'phenotype/CDKN2A_Mutations': int64_feature(CDKN2A_Mutations),
      'phenotype/CHEK2_Mutations': int64_feature(CHEK2_Mutations),
      'phenotype/MLH1_Mutations': int64_feature(MLH1_Mutations),
      'phenotype/MSH2_Mutations': int64_feature(MSH2_Mutations),
      'phenotype/MSH6_Mutations': int64_feature(MSH6_Mutations),
      'phenotype/PALB2_Mutations': int64_feature(PALB2_Mutations),
      'phenotype/PTEN_Mutations': int64_feature(PTEN_Mutations),
      'phenotype/RAD51C_Mutations': int64_feature(RAD51C_Mutations),
      'phenotype/RAD51D_Mutations': int64_feature(RAD51D_Mutations),
      'phenotype/TP53_Mutations': int64_feature(TP53_Mutations),
      'phenotype/AnyGene_Mutations': int64_feature(AnyGene_Mutations),
      'phenotype/GermlineMutation': int64_feature(GermlineMutation)

  }))
  
def image_to_tfexample_step1(image_data, image_format, height, width, image_name,
                        histological_type=None,
                        tissue_pathology=None,
                        tumor_class=None
						
                                                ):
  return tf.train.Example(features=tf.train.Features(feature={
      'image/encoded': bytes_feature(image_data),
      'image/format': bytes_feature(image_format.encode('utf8')),
      'image/name': bytes_feature(image_name.encode('utf8')),
      'image/height': int64_feature(height),
      'image/width': int64_feature(width),
      'phenotype/histological_type': int64_feature(histological_type),
      'phenotype/tissue_pathology': int64_feature(tissue_pathology),
      'phenotype/tumor_class': int64_feature(tumor_class)

  }))
  
def read_label_file(dataset_dir, filename):
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
