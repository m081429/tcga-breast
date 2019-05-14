set -x
SCRIPTS=/data/Naresh_Learning/scripts/tcga-breast/scripts
cd $SCRIPTS
source tcga_run_models.cfg

IFS=$'\n'
for i in `cat $SCRIPTS/tcga_run_models.txt|head -6|tail -1`
do
	CHECK_POINT_PATH=`echo $i|cut -f1`
	MODELNAME=`echo $i|cut -f2`
	SCOPE=`echo $i|cut -f3`
	TRAIN_LOGDIR=$LOGDIR"/"$MODELNAME"/train"
	EVAL_LOGDIR=$LOGDIR"/"$MODELNAME"/eval"
	mkdir -p $LOGDIR"/"$MODELNAME
	for ((step=100000;step<=500000;step=step+10000)); 
	do
		for ((try=1;try<=10;try=try+1));
		do	
			echo $CHECK_POINT_PATH $MODELNAME $SCOPE $TRAIN_LOGDIR $EVAL_LOGDIR $step $try
			python $SLIM_SCRIPTS/train_image_classifier.py \
			 --train_dir=${TRAIN_LOGDIR} \
			 --dataset_name=tcga \
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
			 --preprocessing_name tcga \
			 --optimizer rmsprop \
			 --learning_rate 0.01 \
			 --train_image_size 224  
			ret=$?
			if [ $ret -eq 0 ]; then
				try=11
			fi
		done
		if [ $ret -ne 0 ]; then
			echo "training step failed"
			exit 1
		fi
		#exit
		python $SLIM_SCRIPTS/eval_image_classifier.py \
		--checkpoint_path ${TRAIN_LOGDIR} \
		--eval_dir ${EVAL_LOGDIR} \
		--dataset_name=tcga \
		--dataset_split_name=test \
		--dataset_dir=${DATASET_DIR} \
		--model_name=${MODELNAME} \
		--batch_size 32 \
		--preprocessing_name bh_bach  --eval_image_size 224
		ret=$?
		if [ $ret -ne 0 ]; then
			echo "eval step failed"
			exit 1
		fi
	done	
done
