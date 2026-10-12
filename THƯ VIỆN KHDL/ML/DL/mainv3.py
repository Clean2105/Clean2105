import matplotlib.pyplot as plt 
import numpy as np 

x = np.arange(-2*np.pi, 2*np.pi, 0.01)
y = np.sin(x)/x 
y2 = np.sin(2*x)/x 
y3 = np.sin(3*x)/x 
plt.plot(x,y)
plt.plot(x,y2)
plt.plot(x,y3)
plt.show() 