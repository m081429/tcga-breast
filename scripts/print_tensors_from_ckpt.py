
import os
import argparse
import sys
from tensorflow.python.tools.inspect_checkpoint import print_tensors_in_checkpoint_file

check_point=sys.argv[1]
print_tensors_in_checkpoint_file(file_name=check_point, tensor_name='', all_tensors=True, all_tensor_names=True)