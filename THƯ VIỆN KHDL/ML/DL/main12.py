import numpy as np 
list_2D = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
a = np.array(list_2D)
b = np.arange(4,10)
b_list = b + 1
a_arr = a - 1

print(f"Mảng:\n {a}")
print(f"Arange:\n {b}")
print(f"b = \n {b_list}")
print(f"a = \n {a_arr}") 