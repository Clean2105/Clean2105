import matplotlib.pyplot as plt 
import numpy as np 

from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator 

np.random.seed(19680801)
z = np.random.rand(6,10)
x = np.arange(-0.5,10,1)
y = np.arange(4.5,11,1)

fig, ax = plt.subplots()
ax.pcolormesh(x, y, z)
plt.show() 