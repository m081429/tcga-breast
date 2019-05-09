#! /bin/bash
#$ -q 1-day
#$ -l h_vmem=30G
#$ -M prodduturi.naresh@mayo.edu
#$ -t 2-393:1
#$ -m abe
#$ -V
#$ -cwd
# #$ -pe threaded 4
#$ -j y
#$ -o /research/bsi/projects/PI/tertiary/Sun_Zhifu_zxs01/s4331393.GTEX/processing/naresh/Digital_path/temp/log

set -x
temp_dir=/research/bsi/projects/PI/tertiary/Sun_Zhifu_zxs01/s4331393.GTEX/processing/naresh/Digital_path/temp/log
FINAL_COMBINED_FILE=/research/bsi/projects/PI/tertiary/Sun_Zhifu_zxs01/s4331393.GTEX/processing/naresh/Digital_path/scripts/tcga-breast/scripts/FINAL_TCGA_SVS.txt
PATCH_DIR=/research/bsi/projects/PI/tertiary/Sun_Zhifu_zxs01/s4331393.GTEX/processing/naresh/Digital_path/patches/
TF_DIR=/research/bsi/projects/PI/tertiary/Sun_Zhifu_zxs01/s4331393.GTEX/processing/naresh/Digital_path/tfrecords
Patch_size=224
cd /research/bsi/projects/PI/tertiary/Sun_Zhifu_zxs01/s4331393.GTEX/processing/naresh/Digital_path/scripts/tcga-breast/scripts
#TEMP_FINAL_COMBINED_FILE="$temp_dir/$SGE_TASK_ID.FINAL_TCGA_SVS.txt"
# head -1 $FINAL_COMBINED_FILE > $TEMP_FINAL_COMBINED_FILE
# head -$SGE_TASK_ID  $FINAL_COMBINED_FILE|tail -1 >> $TEMP_FINAL_COMBINED_FILE
#/research/bsi/projects/PI/tertiary/Sun_Zhifu_zxs01/s4331393.GTEX/processing/naresh/Digital_path/packages/
#source /research/bsi/projects/PI/tertiary/Sun_Zhifu_zxs01/s4331393.GTEX/processing/naresh/Digital_path/mypython3/bin/activate
#/research/bsi/tools/biotools/tensorflow/1.12.0/miniconda/bin/conda create --prefix /research/bsi/projects/PI/tertiary/Sun_Zhifu_zxs01/s4331393.GTEX/processing/naresh/Digital_path/mypython python=3
#conda activate /research/bsi/tools/biotools/tensorflow/1.12.0/miniconda/envs/tensorflow/
#export PYTHONPATH=$PYTHONPATH://research/bsi/tools/biotools/openslide/3.4.1
#export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/research/bsi/tools/biotools/openslide/3.4.1/lib/:/research/bsi/tools/biotools/tensorflow/1.12.0/miniconda/lib/
#export PYTHONPATH=$PYTHONPATH:/research/bsi/projects/PI/tertiary/Sun_Zhifu_zxs01/s4331393.GTEX/processing/naresh/Digital_path/models/research/slim/
source /research/bsi/tools/biotools/tensorflow/1.12.0/PKG_PROFILE
source /research/bsi/tools/biotools/openslide/3.4.1/PKG_PROFILE
source /research/bsi/tools/biotools/tensorflow/1.12.0/miniconda/bin/activate tf-gpu-cuda8
#python /research/bsi/projects/PI/tertiary/Sun_Zhifu_zxs01/s4331393.GTEX/processing/naresh/Digital_path/scripts/tcga-breast/scripts/Create_TCGA_ImagePatches.py -i $TEMP_FINAL_COMBINED_FILE -p $PATCH_DIR -o $TF_DIR -s $Patch_size
cd /research/bsi/projects/PI/tertiary/Sun_Zhifu_zxs01/s4331393.GTEX/processing/naresh/Digital_path/models/research/slim/
python /research/bsi/projects/PI/tertiary/Sun_Zhifu_zxs01/s4331393.GTEX/processing/naresh/Digital_path/scripts/tcga-breast/scripts/Inference_apply_model.py
#deactivate
conda deactivate
