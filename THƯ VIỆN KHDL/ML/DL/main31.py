import tensorflow as tf 

tensor_1 = tf.constant([[1,2,3], [4,5,6]])
tensor_2 = tf.constant([[7,8,9], [10,11,12]])

tensor_3 = tf.concat((tensor_1, tensor_2), axis=0)
tensor_4 = tf.concat((tensor_1, tensor_2), axis=1)

print(f"Tensor 1:\n {tensor_1}")
print(f"Tensor 2:\n {tensor_2}")
print(f"Chiều dọc:\n { tensor_3}")
print(f"Chiều ngang:\n {tensor_4}") 