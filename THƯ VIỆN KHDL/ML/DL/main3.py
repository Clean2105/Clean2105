# Numpy code
import numpy as np 

# Tạo một danh sách hai chiều.
list_2D = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Tạo một mảng hai chiều.
arr_2D = np.array(list_2D)

# Kiểm tra hình dạng, kiểu dữ liệu, loại của mảng.
print(f"Hình dạng của mảng: {arr_2D.shape}")
print(f"Kiểu dữ liệu của mảng: {arr_2D.dtype}")
print(f"Loại của mảng: {type(arr_2D)}")
print(f"Mảng:\n {arr_2D}") 