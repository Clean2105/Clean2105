import tensorflow as tf 

tf.random.set_seed(2024) 

tensor_random = tf.random.uniform((3,4))
print(f"Ngẫu nhiên trong khoảng [0, 1):\n {tensor_random}")

tensor_random = tf.random.uniform((3,4), minval=-10, maxval=10, dtype=tf.int32)
print(f"Ngẫu nhiên trong khoảng [-10, 10):\n {tensor_random}") 