
#set -x

# file=/data/Naresh_Learning/scripts/tcga-breast/scripts/labeltf_new.txt
# for (( SGE_TASK_ID=1; SGE_TASK_ID<=92; SGE_TASK_ID++ )) ; do 
	# #echo $SGE_TASK_ID
	# label=`head -$SGE_TASK_ID $file|tail -1|cut -f1 -d ' '`
	# input_tf=`head -$SGE_TASK_ID $file|tail -1|cut -f2 -d ' '`
	# LABEL_DIR=/data/Naresh_Learning/data/BRCA_TCGA/tfrecords/labeltf 
	# grep -P "\[" $LABEL_DIR/$label|grep -P "^\[0|\[1"|sed -e 's/\[//g'|sed -e 's/\]//g' >  $LABEL_DIR/$label.final
	# OUTPUT_DIR=/data/Naresh_Learning/data/BRCA_TCGA/tfrecords/selected_samples_tumonly
	# echo $LABEL_DIR/$label.final $input_tf $OUTPUT_DIR/$label 
	# python /data/Naresh_Learning/scripts/tcga-breast/scripts/Subset_tumor_only_images_tfrecords.py -l $LABEL_DIR/$label.final -i $input_tf -o $OUTPUT_DIR/$label 
	# #exit
# done
# exit
train_dir=/data/Naresh_Learning/data/BRCA_TCGA/tfrecords/selected_samples_tumonly/train
val_dir=/data/Naresh_Learning/data/BRCA_TCGA/tfrecords/selected_samples_tumonly/trainval
test_dir=/data/Naresh_Learning/data/BRCA_TCGA/tfrecords/selected_samples_tumonly/test
dir=/data/Naresh_Learning/data/BRCA_TCGA/tfrecords/selected_samples_tumonly
# mkdir $train_dir $val_dir $test_dir
# num_non=0
# num_mut=0

# for i in `ls $dir/|grep ".tfrecords"`
# do
	# name=`echo $i|sed -e 's/.tfrecords//g'`
	
	# any_gene=`grep $name /data/Naresh_Learning/scripts/tcga-breast/scripts/TCGA_anygene_mut.txt|uniq|cut -f2`
	# echo $name $any_gene
	# #exit
	# if [ "$any_gene" -eq "0" ]
	# then
		# num_non=$((num_non+1))
		# name1=`echo $i|sed -e 's/.tfrecords/.gene_0.tfrecords/g'`
		# if [ "$num_non" -gt "20" ]
		# then
			# mv $dir/$i $train_dir/$name1
		# elif  [ "$num_non" -gt "15" ]
		# then
			# mv $dir/$i $val_dir/$name1
		# else
			# mv $dir/$i $test_dir/$name1
		# fi	
	# else
		# num_mut=$((num_mut+1))
		# name1=`echo $i|sed -e 's/.tfrecords/.gene_1.tfrecords/g'`
		# if [ "$num_mut" -gt "11" ]
		# then
			# mv $dir/$i $train_dir/$name1
		# elif  [ "$num_mut" -gt "7" ]
		# then
			# mv $dir/$i $val_dir/$name1
		# else
			# mv $dir/$i $test_dir/$name1
		# fi	
	# fi
# done

for i in `ls $test_dir/|grep ".tfrecords"`
do
	name=`echo $i|sed -e 's/.tfrecords/.test.tfrecords/g'`
	file1=$test_dir"/$i"
	file2=$dir"/$name"
	mv  $file1 $file2
done	