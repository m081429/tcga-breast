#! /bin/bash
#$ -q 1-day
#$ -l h_vmem=30G
#$ -M prodduturi.naresh@mayo.edu
#$ -t 1-92:1
#$ -m abe
#$ -V
#$ -cwd
# #$ -pe threaded 4
#$ -j y
#$ -o /research/bsi/projects/PI/tertiary/Sun_Zhifu_zxs01/s4331393.GTEX/processing/naresh/Digital_path/temp/log

set -x
source /research/bsi/tools/biotools/tensorflow/1.12.0/PKG_PROFILE
source /research/bsi/tools/biotools/openslide/3.4.1/PKG_PROFILE
source /research/bsi/tools/biotools/tensorflow/1.12.0/miniconda/bin/activate tf-gpu-cuda8
file=/research/bsi/projects/PI/tertiary/Sun_Zhifu_zxs01/s4331393.GTEX/processing/naresh/Digital_path/scripts/tcga-breast/scripts/labeltf.txt
# SGE_TASK_ID=1
label=`head -$SGE_TASK_ID $file|tail -1|cut -f1 -d ' '`
input_tf=`head -$SGE_TASK_ID $file|tail -1|cut -f2 -d ' '`
LABEL_DIR=/research/bsi/projects/PI/tertiary/Sun_Zhifu_zxs01/s4331393.GTEX/processing/naresh/Digital_path/tfrecords/labeltf 
grep -P "\[" $LABEL_DIR/$label|grep -P "^\[0|\[1"|sed -e 's/\[//g'|sed -e 's/\]//g' >  $LABEL_DIR/$label.final
OUTPUT_DIR=/research/bsi/projects/PI/tertiary/Sun_Zhifu_zxs01/s4331393.GTEX/processing/naresh/Digital_path/tfrecords/selected_samples_tumonly98
echo $LABEL_DIR/$label.final $input_tf $OUTPUT_DIR/$label 
python /research/bsi/projects/PI/tertiary/Sun_Zhifu_zxs01/s4331393.GTEX/processing/naresh/Digital_path/scripts/tcga-breast/scripts/Subset_tumor_only_images_tfrecords.py -l $LABEL_DIR/$label.final -i $input_tf -o $OUTPUT_DIR/$label 
conda deactivate
