import tensorflow as tf 

var = tf.Variable(initial_value=tf.constant([1.0, 2.0, 3.0], dtype=tf.float32))
var.assign([4.0, 5.0, 6.0])
print(f"Biến sau khi cập nhật giá trị:\n {var}")

var.assign_add([1.0, 1.0, 1.0])
print(f"Biến sau khi cập nhật giá trị hiện tại:\n {var}") 