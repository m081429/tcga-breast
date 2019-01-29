set -x
cd /data/Naresh_Learning/scripts/tcga-breast/scripts
DATASET_DIR=/data/Naresh_Learning/data/bh_bach/tfrecords
IMAGE_SIZE=512
DATASET_NAME=bh_bach
LOGDIR=/data/Naresh_Learning/results/bh_bach
IFS=$'\n'
for i in `cat /data/Naresh_Learning/scripts/tcga-breast/scripts/run_models.txt|tail -3|head -1`
do
	CHECK_POINT_PATH=`echo $i|cut -f1`
	MODELNAME=`echo $i|cut -f2`
	SCOPE=`echo $i|cut -f3`
	TRAIN_LOGDIR=$LOGDIR"/"$MODELNAME"/train"
	EVAL_LOGDIR=$LOGDIR"/"$MODELNAME"/eval"
	mkdir -p $LOGDIR"/"$MODELNAME
	for ((step=10000;step<=100000;step=step+10000)); 
	do
		echo $CHECK_POINT_PATH $MODELNAME $SCOPE $TRAIN_LOGDIR $EVAL_LOGDIR $step
		python /data/Naresh_Learning/scripts/models/research/slim/train_image_classifier.py \
		 --train_dir=${TRAIN_LOGDIR} \
		 --dataset_name=bh_bach \
		 --dataset_split_name=train\
		 --dataset_dir=${DATASET_DIR} \
		 --model_name=${MODELNAME} \
		 --log_every_n_steps 100 \
		 --num_clones 4 \
		 --max_number_of_steps ${step} \
		 --batch_size 32 \
		 --checkpoint_path $CHECK_POINT_PATH \
		 --checkpoint_exclude_scopes=${SCOPE} \
		 --trainable_scopes=${SCOPE} \
		 --preprocessing_name bh_bach \
		 --optimizer rmsprop \
		 --learning_rate 0.01 \
         --train_image_size 512  
		ret=$?
		if [ $ret -ne 0 ]; then
			echo "training step failed"
			exit 1
		fi
		
		python /data/Naresh_Learning/scripts/models/research/slim/eval_image_classifier.py \
		--checkpoint_path ${TRAIN_LOGDIR} \
		--eval_dir ${EVAL_LOGDIR} \
		--dataset_name=bh_bach \
		--dataset_split_name=val \
		--dataset_dir=${DATASET_DIR} \
		--model_name=${MODELNAME} \
		--batch_size 32 \
		--preprocessing_name bh_bach  --eval_image_size 512
		ret=$?
		if [ $ret -ne 0 ]; then
			echo "eval step failed"
			exit 1
		fi
	done	
done
