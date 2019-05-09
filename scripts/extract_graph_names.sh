#python /data/Naresh_Learning/scripts/models/research/slim/export_inference_graph.py --model_name=resnet_v1_152 --output_file=/data/Naresh_Learning/freezemodels/resnet_v1_152_inf_graph.pb --dataset_name=bh_bach --dataset_dir /data/Naresh_Learning/data/bh_bach/tfrecords
#freeze_graph \
#--input_graph=/data/Naresh_Learning/freezemodels/resnet_v1_152_inf_graph.pb \
#--input_checkpoint=/data/Naresh_Learning/results/bh_bach/resnet_v1_152/train/model.ckpt-100000 \
#--input_binary=true --output_graph=/data/Naresh_Learning/freezemodels/resnet_v1_152_inf_graph.pb \
#--output_node_names=Resnet_v1_152/Predictions/Reshape_1

python print_tensors_from_ckpt.py |grep -P "^tensor_name" > data/Naresh_Learning/freezemodels/resnet_v1_152.tensornames.txt