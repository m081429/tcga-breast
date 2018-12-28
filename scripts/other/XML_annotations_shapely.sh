#set -x
export PYTHONPATH=$PYTHONPATH:/data/Naresh_Learning/PYTHON_PACKAGES/
#for i in `ls /data/projects/breast/raw_data/XML_TCGA_HG/*.xml`
#do
#	/usr/local/bin/python3 /data/Naresh_Learning/scripts/XML_annotations_shapely.py -i $i -o /data/Naresh_Learning/TCGA/xml_pickle/ -s 
#done
#/usr/local/bin/python3 /data/Naresh_Learning/scripts/XML_annotations_shapely.py -i /data/projects/breast/raw_data/XML_TCGA_HG/TCGA-A2-A0CL-01Z-00-DX1.5342E971-DCD2-42C4-B4FF-E6942A95829E.xml -o /data/Naresh_Learning/TCGA/xml_pickle/ -s /data/projects/breast/raw_data/TCGA/aa0ead42-9917-494c-8d72-36941d533742/TCGA-A2-A0CL-01Z-00-DX1.5342E971-DCD2-42C4-B4FF-E6942A95829E.svs
#/usr/local/bin/python3 /data/Naresh_Learning/scripts/XML_annotations_shapely2.py -i /data/projects/breast/raw_data/XML_TCGA_HG/TCGA-A2-A0CL-01Z-00-DX1.5342E971-DCD2-42C4-B4FF-E6942A95829E.xml -s /data/projects/breast/raw_data/TCGA/aa0ead42-9917-494c-8d72-36941d533742/TCGA-A2-A0CL-01Z-00-DX1.5342E971-DCD2-42C4-B4FF-E6942A95829E.svs -p /data/Naresh_Learning/scripts/patches/ -n TCGA-A2-A0CL-01Z-00-DX1
#exit
xml_directory=/data/projects/breast/raw_data/XML_TCGA_HG
patch_dir=/data/Naresh_Learning/scripts/patches/
#set -x
#find /data/projects/breast/raw_data/TCGA/ -name '*.svs' > svs_file.txt
IFS=$'\n'
# for i in {1..1136};
# do
	# svs_file=`cat svs_file.txt|head -$i|tail -1`
	# #echo $svs_file
	# tcga_id=`basename $svs_file|cut -f1 -d '.'`
	# xml_file=`find $xml_directory -name "$tcga_id*.xml"`
	# n=`find $xml_directory -name "$tcga_id*.xml"|wc -l`
	# if [ $n -gt 0 ];then
		# comm="/usr/local/bin/python3 /data/Naresh_Learning/scripts/XML_annotations_shapely2.py -i $xml_file -s $svs_file -p $patch_dir -n $tcga_id"
		# #/usr/local/bin/python3 /data/Naresh_Learning/scripts/XML_annotations_shapely2.py -i $xml_file -s $svs_file -p $patch_dir -n $tcga_id
		# ec=$?
		# echo "svs_num $i;exitcode $ec;$comm "
	# fi	
# done
#removing failed samples
#grep "exitcode 1" XML_annotations_shapely.txt|rev|cut -f2 -d ' '|rev > samples_failed_patchstep_tcga.txt
# IFS=$'\n'
# for i in `cat samples_failed_patchstep_tcga.txt`
# do
	# m="rm ./patches/binary_subpatch/Name_"$i"*.png"
	# echo $m
	# m="rm ./patches/original_subpatch/Name_"$i"*.png"
	# echo $m
	# #exit
# done
#ls ./patches/binary_subpatch/ > All_subpatch.txt
#ls ./patches/original_subpatch/ > All_subpatch_ori.txt

#total number of samples
#cat All_subpatch.txt |cut -f2 -d '_'|sort|uniq |wc -l
#sorting sample names according to num of patches
#cat All_subpatch.txt |cut -f2 -d '_'|sort|uniq -c|awk '{print $2"\t"$1}'|sort -k2,2n|cut -f1 > sample_names_sorted_num_patch.txt