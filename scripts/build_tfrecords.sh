#python3 /data/Naresh_Learning/scripts/models/research/deeplab/datasets/build_voc2012_data.py > build_voc2012_data.txt
INITIAL_CHECKPOINT=/data/Naresh_Learning/scripts/patches/deeplabv3_xception_ade20k_train/model.ckpt
PWD=/data/Naresh_Learning/scripts/patches1
DATASET_DIR=/data/Naresh_Learning/scripts/patches1/tfrecord/
TRAIN_LOGDIR=$PWD/exp/train_on_train_set/train
EVAL_LOGDIR=$PWD/exp/train_on_train_set/eval
VIS_LOGDIR=$PWD/exp/train_on_train_set/vis
IMAGE_SIZE=512
DATASET_NAME=tcgs_breast
export PYTHONPATH=$PYTHONPATH:/data/Naresh_Learning/scripts/models/research/slim:/data/Naresh_Learning/scripts/models/research/
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
