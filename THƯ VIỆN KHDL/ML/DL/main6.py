import numpy as np 
list_arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
list_zeros = np.zeros_like(list_arr)
list_ones = np.ones_like(list_arr)
list_2D_arr = np.array(list_arr)

print(f"Mảng:\n {list_2D_arr}")
print(f"Hàm zeros:\n {list_zeros}")
print(f"Hàm ones:\n {list_ones}") 