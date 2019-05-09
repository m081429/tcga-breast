set -x
SCRIPTS=/research/bsi/projects/PI/tertiary/Sun_Zhifu_zxs01/s4331393.GTEX/processing/naresh/Digital_path/scripts/tcga-breast/scripts/
cd $SCRIPTS

DATASET_DIR=/research/bsi/projects/PI/tertiary/Sun_Zhifu_zxs01/s4331393.GTEX/processing/naresh/Digital_path/tfrecords/bh_bach/tfrecords/
IMAGE_SIZE=512
DATASET_NAME=bh_bach
LOGDIR=/research/bsi/projects/PI/tertiary/Sun_Zhifu_zxs01/s4331393.GTEX/processing/naresh/Digital_path/
SLIM_SCRIPTS=/research/bsi/projects/PI/tertiary/Sun_Zhifu_zxs01/s4331393.GTEX/processing/naresh/Digital_path/models/research/slim
IFS=$'\n'
MODELNAME="resnet_v1_152"
TRAIN_LOGDIR=$LOGDIR"/"$MODELNAME"_FineTune_no_tr_scope_learn_rate_1e_3/train"

echo $MODELNAME $TRAIN_LOGDIR  $IMAGE_SIZE $DATASET_DIR
source /research/bsi/tools/biotools/tensorflow/1.12.0/PKG_PROFILE
source /research/bsi/tools/biotools/openslide/3.4.1/PKG_PROFILE
source /research/bsi/tools/biotools/tensorflow/1.12.0/miniconda/bin/activate tf-gpu-cuda8

 python $SLIM_SCRIPTS/inference.py \
 --checkpoint_path ${TRAIN_LOGDIR} \
 --eval_dir ${EVAL_LOGDIR} \
 --dataset_name=bh_bach \
 --dataset_split_name=val \
 --dataset_dir=${DATASET_DIR} \
 --model_name=${MODELNAME} \
 --batch_size 1 \
 --preprocessing_name bh_bach  --eval_image_size $IMAGE_SIZE

conda deactivate
