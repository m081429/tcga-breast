#for i in `ls /data/Naresh_Learning/data/BRCA_TCGA/tfrecords/selected_samples_tumonly1|grep train`
#do
#	echo $i
#	cp /data/Naresh_Learning/data/BRCA_TCGA/tfrecords/selected_samples_tumonly1/$i /data/Naresh_Learning/data/BRCA_TCGA/tfrecords/selected_samples_tumonly/
#	bash tcga_run_models.sh > /data/Naresh_Learning/scripts/tcga-breast/scripts/verify_tf/$i 2>&1
#	rm -rf /data/Naresh_Learning/results/tcga_anygene/*
#	rm /data/Naresh_Learning/data/BRCA_TCGA/tfrecords/selected_samples_tumonly/$i
#done

# #level2
 set -x
 dir="/data/Naresh_Learning/data/BRCA_TCGA/tfrecords/Level2"
 finaldir="/data/Naresh_Learning/data/BRCA_TCGA/tfrecords/Level2_selected_Anygene"
 nomutn=120
 mutn=60
 nn=0
 nm=0
 for i in `ls $dir`
 do
	 sampname=`echo $i|sed -e 's/.tfrecords//g'`
	 mut=`cut -f1,55 /data/Naresh_Learning/scripts/tcga-breast/scripts/FINAL_TCGA_SVS.txt|sort -k1,1|uniq|grep $sampname|cut -f2` 
	# #echo $sampname $mut
	 if [ $mut -eq 1 ]; then
		 (( nm += 1 ))
		 if [ $nm -lt 21 ]; then
			 file="$dir/$i"
			 file1="$finaldir/"`echo $i|sed -e 's/.tfrecords/.gene_1.test.tfrecords/g'`
			 cp $file $file1
		 fi
		 if [ $nm -lt 61 ] && [ $nm -gt 20 ]; then
			 file="$dir/$i"
			 file1="$finaldir/"`echo $i|sed -e 's/.tfrecords/.gene_1.train.tfrecords/g'`
			 cp $file $file1
		 fi
	 fi
	 if [ $mut -eq 0 ]; then
		 (( nn += 1 ))
		 if [ $nn -lt 41 ]; then
			 file="$dir/$i"
			 file1="$finaldir/"`echo $i|sed -e 's/.tfrecords/.gene_0.test.tfrecords/g'`
			 cp $file $file1
		 fi
		 if [ $nn -lt 121 ]  && [ $nn -gt 40 ]; then
			 file="$dir/$i"
			 file1="$finaldir/"`echo $i|sed -e 's/.tfrecords/.gene_0.train.tfrecords/g'`
			 cp $file $file1
		 fi
	 fi
 done
exit
#level2 BRCA
set -x
dir="/data/Naresh_Learning/data/BRCA_TCGA/tfrecords/Level2"
finaldir="/data/Naresh_Learning/data/BRCA_TCGA/tfrecords/Level2_selected"
nomutn=36
mutn=18
nn=0
nm=0
for i in `ls $dir`
do
	sampname=`echo $i|sed -e 's/.tfrecords//g'`
	mut=`cut -f1,40 /data/Naresh_Learning/scripts/tcga-breast/scripts/FINAL_TCGA_SVS.txt|sort -k1,1|uniq|grep $sampname|cut -f2` 
	#echo $sampname $mut
	if [ $mut -eq 1 ]; then
		(( nm += 1 ))
		if [ $nm -lt 7 ]; then
			file="$dir/$i"
			file1="$finaldir/"`echo $i|sed -e 's/.tfrecords/.brca1_1.test.tfrecords/g'`
			cp $file $file1
		fi
		if [ $nm -lt 19 ] && [ $nm -gt 6 ]; then
			file="$dir/$i"
			file1="$finaldir/"`echo $i|sed -e 's/.tfrecords/.brca1_1.train.tfrecords/g'`
			cp $file $file1
		fi
	fi
	if [ $mut -eq 0 ]; then
		(( nn += 1 ))
		if [ $nn -lt 13 ]; then
			file="$dir/$i"
			file1="$finaldir/"`echo $i|sed -e 's/.tfrecords/.brca1_0.test.tfrecords/g'`
			cp $file $file1
		fi
		if [ $nn -lt 37 ]  && [ $nn -gt 12 ]; then
			file="$dir/$i"
			file1="$finaldir/"`echo $i|sed -e 's/.tfrecords/.brca1_0.train.tfrecords/g'`
			cp $file $file1
		fi
	fi
done
