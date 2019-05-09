set -x
SCRIPTS=/data/Naresh_Learning/scripts/tcga-breast/scripts
cd $SCRIPTS

DATASET_DIR=/data/Naresh_Learning/data/bh_bach/tfrecords
IMAGE_SIZE=512
DATASET_NAME=bh_bach
LOGDIR=/data/Naresh_Learning/results/bh_bach
SLIM_SCRIPTS=/data/Naresh_Learning/scripts/models/research/slim
IFS=$'\n'
MODELNAME="resnet_v1_152"
TRAIN_LOGDIR=$LOGDIR"/"$MODELNAME"_FineTune_no_tr_scope_learn_rate_1e_3/train"
EVAL_LOGDIR=$LOGDIR"/"$MODELNAME"_FineTune_no_tr_scope_learn_rate_1e_3/eval"
echo $MODELNAME $TRAIN_LOGDIR $EVAL_LOGDIR $IMAGE_SIZE $DATASET_DIR

 #python $SLIM_SCRIPTS/inference2.py \
 #--checkpoint_path ${TRAIN_LOGDIR} \
 #--eval_dir ${EVAL_LOGDIR} \
 #--dataset_name=bh_bach \
 #--dataset_split_name=val_bach \
 #--dataset_dir=${DATASET_DIR} \
 #--model_name=${MODELNAME} \
 #--batch_size 1 \
 #--preprocessing_name bh_bach  --eval_image_size $IMAGE_SIZE
#exit
IMAGE_SIZE=224
DATASET_DIR=/data/Naresh_Learning/data/BRCA_TCGA/tfrecords/Test
python $SLIM_SCRIPTS/inference2.py \
--checkpoint_path ${TRAIN_LOGDIR} \
--eval_dir ${EVAL_LOGDIR} \
--dataset_name=tcga \
--dataset_split_name=- \
--dataset_dir=${DATASET_DIR} \
--model_name=${MODELNAME} \
--batch_size 1 \
--preprocessing_name tcga  --eval_image_size $IMAGE_SIZE

