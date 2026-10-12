import matplotlib.pyplot as plt 
import numpy as np 

index = np.arange(5) + 0.5 

v1 = [5,7,3,4,6]
v2 = [6,6,4,5,7]
v3 = [5,6,5,4,6]

bw = 0.3 
plt.axis([0, 6.0, 0, 8.5])
plt.title("A Multiseries Bar Chart", fontsize=20)
plt.bar(index, v1, bw, color='b')
plt.bar(index + bw, v2, bw, color='g')
plt.bar(index + 2 * bw, v3, bw, color='r')
plt.xticks(index + bw, ['A', 'B', 'C', 'D', 'E'])
plt.legend()
plt.show() 