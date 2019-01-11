set -x
cd /data/Naresh_Learning/scripts/tcga-breast/scripts
#python3 XML_annotations_shapely_BACH_BreakHIS_create_tf.py
#export PYTHONPATH=$PYTHONPATH:/data/Naresh_Learning/scripts/models/research/slim:/data/Naresh_Learning/scripts/models/research/
DIR=/data/Naresh_Learning/scripts/patches1/
TRAIN_LOGDIR=$DIR/exp/train_on_train_set/train
EVAL_LOGDIR=$DIR/exp/train_on_train_set/eval
VIS_LOGDIR=$DIR/exp/train_on_train_set/vis
DATASET_DIR=$DIR/tfrecord/
IMAGE_SIZE=512
DATASET_NAME=bh_bach
CHECK_POINT_PATH=/data/Naresh_Learning/scripts/models/research/slim/checkpoints/inception_v4.ckpt
step=50000

# python /data/Naresh_Learning/scripts/models/research/slim/train_image_classifier.py \
	# --train_dir=${TRAIN_LOGDIR} \
	# --dataset_name=bh_bach \
	# --dataset_split_name=train\
	# --dataset_dir=${DATASET_DIR} \
	# --model_name=inception_v4 \
	# --log_every_n_steps 100 \
	# --num_clones 4 \
	# --max_number_of_steps ${step} \
	# --batch_size 32 \
	# --checkpoint_path $CHECK_POINT_PATH \
	# --checkpoint_exclude_scopes=InceptionV4/Logits,InceptionV4/AuxLogits \
	# --trainable_scopes=InceptionV4/Logits,InceptionV4/AuxLogits \
	# --preprocessing_name bh_bach \
	# --optimizer rmsprop \
	# --learning_rate 0.01 

python /data/Naresh_Learning/scripts/models/research/slim/eval_image_classifier.py \
    --checkpoint_path ${TRAIN_LOGDIR} \
	--eval_dir ${EVAL_LOGDIR} \
	--dataset_name=bh_bach \
	--dataset_split_name=val \
	--dataset_dir=${DATASET_DIR} \
	--model_name=inception_v4 \
	--batch_size 32 \
	--preprocessing_name bh_bach
exit
INITIAL_CHECKPOINT=/data/Naresh_Learning/scripts/patches/deeplabv3_xception_ade20k_train/model.ckpt

set -x
IFS=$'\n'
for i in `cat file_steps.txt`
do
echo "step $i"

python3 /data/Naresh_Learning/scripts/models/research/deeplab/train.py --logtostderr  \
	 --model_variant "xception_65"  \
	 --dataset ${DATASET_NAME} \
	 --tf_initial_checkpoint=${INITIAL_CHECKPOINT} \
	 --train_logdir ${TRAIN_LOGDIR} \
	 --dataset_dir ${DATASET_DIR}   \
	 --training_number_of_steps=$i \
	 --log_steps=100  \
	 --atrous_rates=6 \
	 --atrous_rates=12 \
	 --atrous_rates=18 \
	 --output_stride=16 \
	 --decoder_output_stride=4 \
	 --train_batch_size=12  \
	 --num_clones 4 \
	 --train_crop_size=${IMAGE_SIZE}  --train_crop_size=${IMAGE_SIZE} --min_scale_factor 1.0 --save_summaries_images --last_layers_contain_logits_only=True --initialize_last_layer=False

python3 /data/Naresh_Learning/scripts/models/research/deeplab/eval.py --logtostderr  \
	 --dataset ${DATASET_NAME} \
	 --checkpoint_dir ${TRAIN_LOGDIR} \
	 --dataset_dir ${DATASET_DIR}   \
	 --log_steps=100  \
	 --atrous_rates=6 \
	 --atrous_rates=12 \
	 --atrous_rates=18 \
	 --output_stride=16 \
	 --decoder_output_stride=4 \
	 --eval_batch_size=12  \
	 --eval_logdir ${EVAL_LOGDIR} \
	 --eval_split="val" \
	 --model_variant="xception_65"
done
