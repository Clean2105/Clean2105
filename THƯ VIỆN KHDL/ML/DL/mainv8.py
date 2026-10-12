import matplotlib.pyplot as plt 
import numpy as np 

from matplotlib.colors import LogNorm 

np.random.seed(19680801)
z = np.random.rand(6,10)

fig, (ax0, ax1) = plt.subplots(2,1)
c = ax0.pcolor(z) 

ax0.set_title('default:n edges')

c = ax1.pcolor(z, edgecolor='k', linewidths=4)
ax1.set_title('thick edges')

plt.tight_layout()
plt.show() 