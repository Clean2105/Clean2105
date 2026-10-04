import numpy as np 

a = [[1,2], [3,4], [5,6]]
b = np.array(a)
arr = np.arange(4,6)
sin_arr = b * np.sin(arr)
sqrt_arr = b * np.sqrt(arr) 

print(f"Mảng:\n {b}")
print(f"Arange:\n {arr}")
print(f"Sin_arr = \n {sin_arr}")
print(f"Sqrt_arr = \n {sqrt_arr}") 