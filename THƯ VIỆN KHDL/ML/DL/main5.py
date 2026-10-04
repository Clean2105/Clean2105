# Pytorch code
import tensorflow as tf

# Tạo một danh sách hai chiều.
list_2D = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Tạo một tensor hai chiều.
tensor_2D_tf = tf.convert_to_tensor(list_2D)

# Kiểm tra hình dạng, kiểu dữ liệu, loại, thiết bị mã tensor của tensorflow.
print(f"Hình dạng của tensor: {tensor_2D_tf.shape}")
print(f"Kiểu dữ liệu của tensor: {tensor_2D_tf.dtype}")
print(f"Loại của tensor: {type(tensor_2D_tf)}")
print(f"Thiết bị mã của tensor: {tensor_2D_tf.device}")
print(f"Tensorflow:\n {tensor_2D_tf}") 