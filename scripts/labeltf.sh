#set -x
IFS=$'\n'
#for i in `cat labeltf.txt`
#do
#	echo $i
#	cp /data/Naresh_Learning/data/BRCA_TCGA/tfrecords/Test1/$i /data/Naresh_Learning/data/BRCA_TCGA/tfrecords/Test
#	bash inference.sh > ./labeltf/$i 2>&1
#	rm /data/Naresh_Learning/data/BRCA_TCGA/tfrecords/Test/*.tfrecords	
#done
rm labeltf_new.txt
for i in `cat labeltf.txt`
do
	#echo $i
	file=`ls /data/Naresh_Learning/data/BRCA_TCGA/tfrecords/Test1/$i`
	echo $i $file >> labeltf_new.txt
	#exit
done
