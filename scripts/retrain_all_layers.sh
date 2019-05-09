set -x
SCRIPTS=/data/Naresh_Learning/scripts/tcga-breast/scripts
cd $SCRIPTS
source retrain_models.cfg

IFS=$'\n'
for i in `cat $SCRIPTS/retrain_all_layers.txt|tail -2`
do
	CHECK_POINT_PATH=`echo $i|cut -f1`
	MODELNAME=`echo $i|cut -f2`
	SCOPE=`echo $i|cut -f3`
	CH_SCOPE=`echo $i|cut -f4`
	TRAIN_LOGDIR=$LOGDIR"/"$MODELNAME"_FineTune_no_tr_scope_learn_rate_1e_3/train"
	EVAL_LOGDIR=$LOGDIR"/"$MODELNAME"_FineTune_no_tr_scope_learn_rate_1e_3/eval"
	mkdir -p $LOGDIR"/"$MODELNAME
<<<<<<< HEAD
	for ((step=100000;step<=100000;step=step+10000)); 
=======
	for ((step=10000;step<=100000;step=step+10000)); 
>>>>>>> 51eda72cfb38934ba277cf5c08b6862b5d13ff7a
	do
		echo $CHECK_POINT_PATH $MODELNAME $SCOPE $TRAIN_LOGDIR $EVAL_LOGDIR $step
		python $SLIM_SCRIPTS/train_image_classifier.py \
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
		 --checkpoint_exclude_scopes=${CH_SCOPE} \
		 --preprocessing_name bh_bach \
		 --optimizer rmsprop \
		 --learning_rate 0.001 \
         --train_image_size 512  
		ret=$?
		if [ $ret -ne 0 ]; then
			echo "training step failed"
			exit 1
		fi
		
		python $SLIM_SCRIPTS/eval_image_classifier.py \
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
