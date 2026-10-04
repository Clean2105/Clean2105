import numpy as np 
list_2D = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
list_arr = np.array(list_2D)
list_arange = np.arange(1, 10)
list_reshape = np.reshape(list_arange, (3, 3))
list_linspace = np.linspace(1, 9, 9)

print(f"Mảng:\n {list_arr}")
print(f"Hàm arange:\n {list_arange}")
print(f"Hàm reshape:\n {list_reshape}")
print(f"Hàm linspace:\n {list_linspace}") 