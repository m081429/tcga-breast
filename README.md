# Predicting breast cancer phenotypes from TCGA H&E images

## Objective
The purpose of this repository is to detail the process for preparing, training, and testing the ability of Deep Learning to predict characteristics of breast cancers from H&E slides.

## Process
* Make Segmentation TFRecords
* Train and Test Segmentation
* Freeze Segmentation Model
* Apply model to identify tumor tissue
* Create TFRecords for Classification
* Train and Test on multiple phenotypes

Initially, all analyses will be performed on the highest resolution (Level 0), but I would also like to try Levels 1-3.



### Make Segmentation TFRecords
In thier HASHI algorithm paper, Cruz-Roa et al [(2018)](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0196828) provided XML annotations for 173 tumor regions in the TCGA-Breast study. These annotations were downloaded from the [Dryad database](https://datadryad.org/resource/doi:10.5061/dryad.1g2nt41). Annotations in the XML files are relative to the "Level 0" of the SVS image files. These annotations were used to create binary segmentation masks, and then converted to TFRecords files. Training examples were generated from 132 XML-SVS paris. The remaining 41 slides were used for testing.  This ensures that no patients were used in training and testing.

We also donloaded data from the [BACH challenge](https://arxiv.org/pdf/1808.04277.pdf).
```
https://rdm.inesctec.pt/dataset/604dfdfa-1d37-41c6-8db1-e82683b8335a/resource/df04ea95-36a7-49a8-9b70-605798460c35/download/breasthistology.zip
```


```
# Insert Naresh's logic/code steps here
```

### Train and Test Segmentation
Once training and testing TFRecords were made, chekpoints from a DeepLabV3+ model [(xception65_ade20k_train)](http://download.tensorflow.org/models/deeplabv3_xception_ade20k_train_2018_05_29.tar.gz) pretrained on the ADE20K dataset was used for tranfer learning for XX steps.
```
# Training
```
Once training was completed, accuracy was assessed on the test set.
```
# Testing
```

### Freeze Segmentation Model
Once testing was complete, the model was frozen so that inference could be applied to the remaining 886 TCGA breast cancer slides that were not annotated by Cruz-Roa et al.
```
# From tensorflow/models/research/
# Assume all checkpoint files share the same path prefix `${CHECKPOINT_PATH}`.
python deeplab/export_model.py \
    --checkpoint_path=${CHECKPOINT_PATH} \
    --export_path=${OUTPUT_DIR}/frozen_inference_graph.pb
```

### Apply model to identify tumor tissue

```
# See https://github.com/tensorflow/models/blob/master/research/deeplab/deeplab_demo.ipynb for instructions
# May need to run the following to get the Tensor names
bazel-bin/tensorflow/tools/graph_transforms/summarize_graph \
  --in_graph=${OUTPUT_DIR}/frozen_inference_graph.pb

# infer.py
```
### Create TFRecords for Classification & Regression
There are 2 types of features we are trying to predict: binary and categorical

Categorical & binary features need to be converted into numerical representations before embedding. Need to also write out a *_labels.txt file to map back to original values
```
# create_classTFrecords.py
```

# Train and Test on multiple phenotypes
TFRecords can only be constructed if all variables are present. Using the features below, this leaves XX samples for training and XX samples for testing. 

* Categorical
  *  race
    *  0: White
    *  1: Black
    *  2: Asian
  *  ajcc_pathologic_tumor_stage
    *  0: StageX
    *  1: Stage1
    *  2: Stage2
    *  3: Stage3
    *  4: Stage4
  * PAM50.mRNA
    *  0: Basal
    *  1: HER2
    *  2: LumA
    *  3: LumB
    *  4: Normal-like
  * histological_type
    *  0: Infiltrating Ductal Carcinoma
    *  1: Infiltrating Lobular Carcinoma
    *  2: Other

* Binary
  *  tumor_status
     *  0: TUMOR FREE
     *  1: WITH TUMOR
  * DeadInFiveyrs
    *  0: No
    *  1: Yes
  *  ER.Status
    *  0: Negative
    *  1: Positive
  * PR.Status
    *  0: Negative
    *  1: Positive
  *  HER2.Final.Status
    *  0: Negative
    *  1: Positive
  *  Metastasis.Coded
    * 0: Negative
    * 1: Positive
  * ATM_Mutations
    *  0: Negative
    *  1: Positive
  * BRCA1_Mutations
    *  0: Negative
    *  1: Positive
  *  BRCA2_Mutations
    *  0: Negative
    *  1: Positive
  *  CDH1_Mutations
    *  0: Negative
    *  1: Positive
  * CDKN2A_Mutations
    *  0: Negative
    *  1: Positive
  * PTEN_Mutations
    *  0: Negative
    *  1: Positive
  * TP53_Mutations
    *  0: Negative
    *  1: Positive
  * AnyGene_Mutations
    *  0: Negative
    *  1: Positive

Creating the TFRecords uses the following command
```
# create_classTFrecords.py
```


