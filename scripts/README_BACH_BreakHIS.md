# BACH_BreakHIS Dataset

Image classification on BACH Breakhis dataset

## 0. Datasets
```
BACH Dataset
Data labels
i)	In Situ ( Classified as Tumor) [63 Images]
ii)	Invasive ( Classified as Tumor)[62 Images]
iii)	Benign (Classified as Normal) [ 71 Images]
iv) 	Normal (Classified as Normal) [55 Images]
v)	Test data [Include 4 classes][36 Images]
Image size : 1536 X 2048  (12 512X512 image patches)

BreaKHis Dataset
	Data  labels
	i) Malignant (1232 Images)[58 samples]
	ii) Benign ( 588 Images)[24 samples]
Image size: 700 x 460 (Resize to 512 X 512 Image)

```

## 1. Preprocessing
```
Script to create image patches
image_classification_BACH_BreakHIS_preprocess.py

```

## 2. Create TF Records
```
Script to create TF Records including eval datasets
image_classification_BACH_BreakHIS_create_tfrecord.py

```

## 3. Running all models & check points from models/slim to identify best performing model
```
Downloaded all the models and checkpoints from https://github.com/tensorflow/models/tree/master/research/slim#pre-trained-models

Different models
 cat run_models.txt
/inception_v4_2016_09_09/inception_v4.ckpt        inception_v4    InceptionV4/Logits,InceptionV4/AuxLogits
/inception_v1_2016_08_28/inception_v1.ckpt        inception_v1    InceptionV1/Logits,InceptionV1/AuxLogits
/inception_v2_2016_08_28/inception_v2.ckpt        inception_v2    InceptionV2/Logits,InceptionV2/AuxLogits
/inception_v3_2016_08_28/inception_v3.ckpt        inception_v3    InceptionV3/Logits,InceptionV3/AuxLogits
/inception_resnet_v2_2016_08_30/inception_resnet_v2_2016_08_30.ckpt       inception_resnet_v2     InceptionResnetV2/Logits,InceptionResnetV2/AuxLogits
/resnet_v1_50_2016_08_28/resnet_v1_50.ckpt        resnet_v1_50    resnet_v1_50/logits
/resnet_v1_101_2016_08_28/resnet_v1_101.ckpt      resnet_v1_101   resnet_v1_101/logits
/resnet_v1_152_2016_08_28/resnet_v1_152.ckpt      resnet_v1_152   resnet_v1_152/logits
/resnet_v2_50_2017_04_14/resnet_v2_50.ckpt        resnet_v2_50    resnet_v2_50/logits
/resnet_v2_101_2017_04_14/resnet_v2_101.ckpt      resnet_v2_101   resnet_v2_101/logits
/resnet_v2_152_2017_04_14/resnet_v2_152.ckpt      resnet_v2_152   resnet_v2_152/logits
/mobilenet_v1_1.0_224/mobilenet_v1_1.0_224.ckpt   mobilenet_v1    MobilenetV1/Logits
/mobilenet_v1_0.5_160/mobilenet_v1_0.5_160.ckpt   mobilenet_v1_050        MobilenetV1/Logits
/mobilenet_v1_0.25_128/mobilenet_v1_0.25_128.ckpt mobilenet_v1_025        MobilenetV1/Logits
/mobilenet_v2_1.4_224/mobilenet_v2_1.4_224.ckpt   mobilenet_v2    MobilenetV2/Logits,MobilenetV2/Predictions,MobilenetV2/predics
/mobilenet_v2_1.0_224/mobilenet_v2_1.0_224.ckpt   mobilenet_v2_140        MobilenetV2/Logits,MobilenetV2/Predictions,MobilenetV2/predics
/vgg_16_2016_08_28/vgg_16.ckpt    vgg_16  vgg_16
/vgg_19_2016_08_28/vgg_19.ckpt    vgg_19  vgg_19
/nasnet-a_mobile_04_10_2017/model.ckpt.data-00000-of-00001        nasnet_mobile   aux_logits
/nasnet-a_large_04_10_2017/model.ckpt.data-00000-of-00001 nasnet_large    aux_logits
/pnasnet-5_large_2017_12_13/model.ckpt.data-00000-of-00001        pnasnet_large   aux_logits
/pnasnet-5_mobile_2017_12_13/model.ckpt.data-00000-of-00001       pnasnet_mobile  aux_logits

Specific changes needed to run the models
inception_v4_old : no Changes was needed as initial script was build on this one (Image size 512 X 512)
inception_v1 : image resize was needed to 224 X 224
inception_v2 : image resize was needed to 224 X 224
inception_v3 : image resize was needed to 224 X 224
inception_resnet_v2 : image resize was needed to 299 X 299
resnet_v1_50 : image resize was needed to 224 X 224
resnet_v1_101 : image resize was needed to 224 X 224
resnet_v1_152 : image resize was needed to 224 X 224
resnet_v2_50 : image resize was needed to 224 X 224
resnet_v2_101 : image resize was needed to 224 X 224
resnet_v2_152 : image resize was needed to 224 X 224
mobilenet_v1 : image resize was needed to 224 X 224
mobilenet_v1_050 : image resize was needed to 224 X 224
mobilenet_v1_025 : image resize was needed to 224 X 224
mobilenet_v2 : image resize was needed to 224 X 224 In mobilenet_v2.py, change from depth_multiplier=1 to depth_multiplier=1.4 (https://stackoverflow.com/questions/49680440/tf-slim-fine-tune-mobilenet-v2-on-custom-dataset?rq=1)
mobilenet_v2_140 : image resize was needed to 224 X 224 In mobilenet_v2.py, change from depth_multiplier=1.4 to depth_multiplier=1
vgg_16 : image resize was needed to 224 X 224 
vgg_19 : image resize was needed to 224 X 224
nasnet_mobile:image resize was needed to 224 X 224
nasnet_large:image resize was needed to 331 X 331
pnasnet_large:image resize was needed to 331 X 331
pnasnet_mobile:image resize was needed to 224 X 224
inception_v4 : image resize was needed to 224 X 224 
```

## 4. Selecting top 3 performing model and fine tuning last tensors with 1e-6 learning rate
```
	Selecting top 3 performing models
	i)	Resnet v1 152 0.7750 at 100k step
	ii)	Resnet v1 50 0.7750 at 100k step
	iii) Resnet v2 50 0.7535 at 100k step
	
	Used tensor board to select the final tensors for fine tuning
	TensorBoard -> Graphs ->  select Train Run -> double click "model" (resnet_v2_50)
	
	Other way to look at the tensornames in the checkpoint files by using the script "print_tensors_from_ckpt.py"
	
	"print_tensors_from_ckpt.py"
	from tensorflow.python.tools.inspect_checkpoint import print_tensors_in_checkpoint_file
	check_point=sys.argv[1]
	print_tensors_in_checkpoint_file(file_name=check_point, tensor_name='', all_tensors=True, all_tensor_names=True)
	
	Fine tuning script "retrain_models.sh" config "retrain_models.cfg" input params "run_models.txt"
	Output log directories folders with name *"_FineTune"
	Log dir "_FineTune" : both --checkpoint_exclude_scopes and --trainable_scopes as value "resnet_v1_152/block4,resnet_v1_152/logits"
	Log dir "_FineTune_new_tr_scope_new_chk_ex_scope" : both --checkpoint_exclude_scopes and --trainable_scopes as value "resnet_v1_152/block4/unit_1/bottleneck_v1/conv1,resnet_v1_152/block4/unit_1/bottleneck_v1/conv2,resnet_v1_152/block4/unit_1/bottleneck_v1/conv3,resnet_v1_152/block4/unit_1/bottleneck_v1/shortcut,resnet_v1_152/block4/unit_2/bottleneck_v1/conv1,resnet_v1_152/block4/unit_2/bottleneck_v1/conv2,resnet_v1_152/block4/unit_2/bottleneck_v1/conv3,resnet_v1_152/block4/unit_3/bottleneck_v1/conv1,resnet_v1_152/block4/unit_3/bottleneck_v1/conv2,resnet_v1_152/block4/unit_3/bottleneck_v1/conv3,resnet_v1_152/conv1,resnet_v1_152/logits"
	Log dir "_FineTune_new_tr_scope" :  --checkpoint_exclude_scopes as "resnet_v1_152/logits" and --trainable_scopes as value "resnet_v1_152/block4/unit_1/bottleneck_v1/conv1,resnet_v1_152/block4/unit_1/bottleneck_v1/conv2,resnet_v1_152/block4/unit_1/bottleneck_v1/conv3,resnet_v1_152/block4/unit_1/bottleneck_v1/shortcut,resnet_v1_152/block4/unit_2/bottleneck_v1/conv1,resnet_v1_152/block4/unit_2/bottleneck_v1/conv2,resnet_v1_152/block4/unit_2/bottleneck_v1/conv3,resnet_v1_152/block4/unit_3/bottleneck_v1/conv1,resnet_v1_152/block4/unit_3/bottleneck_v1/conv2,resnet_v1_152/block4/unit_3/bottleneck_v1/conv3,resnet_v1_152/conv1,resnet_v1_152/logits"
	Log dir "_FineTune_new_tr_scope_learn_rate_1e-3" :  Learning rate 1e-3, --checkpoint_exclude_scopes as "resnet_v1_152/logits" and --trainable_scopes as value "resnet_v1_152/block4/unit_1/bottleneck_v1/conv1,resnet_v1_152/block4/unit_1/bottleneck_v1/conv2,resnet_v1_152/block4/unit_1/bottleneck_v1/conv3,resnet_v1_152/block4/unit_1/bottleneck_v1/shortcut,resnet_v1_152/block4/unit_2/bottleneck_v1/conv1,resnet_v1_152/block4/unit_2/bottleneck_v1/conv2,resnet_v1_152/block4/unit_2/bottleneck_v1/conv3,resnet_v1_152/block4/unit_3/bottleneck_v1/conv1,resnet_v1_152/block4/unit_3/bottleneck_v1/conv2,resnet_v1_152/block4/unit_3/bottleneck_v1/conv3,resnet_v1_152/conv1,resnet_v1_152/logits"
	Log dir "_FineTune_new_tr_scope_learn_rate_1e-4" :  Learning rate 1e-4, --checkpoint_exclude_scopes as "resnet_v1_152/logits" and --trainable_scopes as value "resnet_v1_152/block4/unit_1/bottleneck_v1/conv1,resnet_v1_152/block4/unit_1/bottleneck_v1/conv2,resnet_v1_152/block4/unit_1/bottleneck_v1/conv3,resnet_v1_152/block4/unit_1/bottleneck_v1/shortcut,resnet_v1_152/block4/unit_2/bottleneck_v1/conv1,resnet_v1_152/block4/unit_2/bottleneck_v1/conv2,resnet_v1_152/block4/unit_2/bottleneck_v1/conv3,resnet_v1_152/block4/unit_3/bottleneck_v1/conv1,resnet_v1_152/block4/unit_3/bottleneck_v1/conv2,resnet_v1_152/block4/unit_3/bottleneck_v1/conv3,resnet_v1_152/conv1,resnet_v1_152/logits"
	Log dir "_FineTune_new_tr_scope_learn_rate_1e-4" :  Learning rate 1e-4, --checkpoint_exclude_scopes as "resnet_v1_152/logits" and --trainable_scopes as value "resnet_v1_152/block4/unit_1/bottleneck_v1/conv1,resnet_v1_152/block4/unit_1/bottleneck_v1/conv2,resnet_v1_152/block4/unit_1/bottleneck_v1/conv3,resnet_v1_152/block4/unit_1/bottleneck_v1/shortcut,resnet_v1_152/block4/unit_2/bottleneck_v1/conv1,resnet_v1_152/block4/unit_2/bottleneck_v1/conv2,resnet_v1_152/block4/unit_2/bottleneck_v1/conv3,resnet_v1_152/block4/unit_3/bottleneck_v1/conv1,resnet_v1_152/block4/unit_3/bottleneck_v1/conv2,resnet_v1_152/block4/unit_3/bottleneck_v1/conv3,resnet_v1_152/conv1,resnet_v1_152/logits"
	Log dir "_FineTune_new_tr_scope_learn_rate_0.0005" : Learning rate 1e-4, --checkpoint_exclude_scopes as "resnet_v1_152/logits" and --trainable_scopes as value	
```

## 5. Selecting best performing model from above step and training all tensor layers with best performing learning rate
```
	i) Best Model selected is Resnet v1 152 with accuracy at  100K step  of "0.8175"
	ii) Best Learning rate selected is 1e-3
	iii) Retraining all tensor layers for Resnet v1 152 with learning rate of 1e-3
	Script: "retrain_all_layers.sh" Model file with Param: "retrain_all_layers.txt"
	Log dir "_FineTune_no_tr_scope_learn_rate_1-3" : Learning rate 1e-3, --checkpoint_exclude_scopes as "resnet_v1_152/logits" and --trainable_scopes as None
```
## 6. Freezing the  best performing model from above step and applying it on the TCGA data
```
	i) Best Model selected is Resnet v1 152 with accuracy at  100K step  of "0.85875"
	Applying this model on the TCGA data
	ii) This script "Unify_TCGA_info.py" will normalize the metadata information in to one file
	python Unify_TCGA_info.py -p $PHENO_DIR -s $PHENO_SET -t $TCGA_SVS_FILE -o $FINAL_COMBINED_FILE
	iii)"FINAL_TCGA_SVS.txt" file has all the metadata information along with path to svs file
	iv) script "Create_TCGA_ImagePatches.py" will read the above file and create the tfrecords(used ncsa cluster to create tfrecords parallely for 392 samples script "NCSA_Create_TCGA_TF.sh")
	v)Tried applying the model on one of the created TCGA tfrecords using "inference.sh"
```

