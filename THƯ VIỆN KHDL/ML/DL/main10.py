import numpy as np 
a = [[1,2], [3,4], [5,6]]
b = np.arange(4,6)
arr = np.array(a) 
x = arr + b 
y = arr - b 
z = arr * b 
print(f"Arange:\n {b}")
print(f"Mảng:\n {arr}")
print(f"x = \n {x}")
print(f"y = \n {y}")
print(f"z = \n {z}") 