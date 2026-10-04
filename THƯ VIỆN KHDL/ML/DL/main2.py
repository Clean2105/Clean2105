import numpy as np 
import torch
import tensorflow as tf 

list_ID = [1, 2, 3, 4, 5, 6, 7, 8, 9]

arr_ID = np.array(list_ID)
print(f"Mảng 1 chiều của array là:\n {arr_ID}, {type(arr_ID)}")

tensor_1D_pt = torch.tensor(list_ID)
print(f"Tensor Pytorch 1 chiều:\n {tensor_1D_pt}, {type(tensor_1D_pt)}")

tensor_1D_tf = tf.convert_to_tensor(list_ID)
print(f"Tensor TensoFlow:\n {tensor_1D_tf}") 
