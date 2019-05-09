set -x
IFS=$'\n'
#for i  in `cat tcga_anygene.txt`
#do
	#echo $i
	#i=$i".tfrecords"
	#file=`grep $i all_tcga.tfrecords`
	#cp $file  /research/bsi/projects/PI/tertiary/Sun_Zhifu_zxs01/s4331393.GTEX/processing/naresh/Digital_path/tfrecords/selected
	#exit
#done
rm labeltf.txt
for i in `ls /research/bsi/projects/PI/tertiary/Sun_Zhifu_zxs01/s4331393.GTEX/processing/naresh/Digital_path/tfrecords/labeltf/`
do
	#echo $i
	#exit
	file=`grep $i all_tcga.tfrecords`
	echo $i $file >> labeltf.txt
	#exit
done
