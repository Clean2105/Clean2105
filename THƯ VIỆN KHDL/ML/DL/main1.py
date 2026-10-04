import numpy as np 
import torch
import tensorflow as tf 

arrayID = np.array([1, 2, 3])
print(f"Numpy array ID:\n {arrayID}, {type(arrayID)}")

arr_tensor_torch = torch.from_numpy(arrayID)
print(f"Chuyển đổi mảng numpy thành tensor Pytorch:\n {arr_tensor_torch}, {type(arr_tensor_torch)}")

tensor_touch_arr = arr_tensor_torch.numpy()
print(f"Chuyển đổi mảng tensor Pytorch thành numpy:\n {tensor_touch_arr}, {type(tensor_touch_arr)}")

arr_tensor_tf = tf.convert_to_tensor(arrayID) 
print(f"Chuyển đổi mảng numpy thành TensorFlow:\n {arr_tensor_tf}, {type(arr_tensor_tf)}")

tensor_tf_arr = arr_tensor_tf.numpy()
print(f"Chuyển đổi mảng  TensorFlow thành Numpy:\n {tensor_tf_arr}, {type(tensor_tf_arr)}") 