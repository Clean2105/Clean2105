import tensorflow as tf 

tf.random.set_seed(2024) 

tensor_random = tf.random.uniform((3,4), minval=-10, maxval=10, dtype=tf.int32)
print(f"Ngẫu nhiên trong khoảng [-10, 10):\n {tensor_random}")

tensor_clip = tf.clip_by_value(tensor_random, clip_value_min=3, clip_value_max=8)
print(f"Sau khi được cắt trong khoảng [3,8]:\n {tensor_clip}") 