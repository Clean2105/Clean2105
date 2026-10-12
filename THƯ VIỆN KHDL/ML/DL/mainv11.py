import matplotlib.pyplot as plt 
import numpy as np 

x = np.arange(-10,10,1)
y = np.arange(-10,10,1)
u,v = np.meshgrid(x,y)

fig, ax = plt.subplots()
q = ax.quiver(x, y, u, v)
ax.quiverkey(q, X=0.3, Y=1.1, U=10, label='Quiverkey, length=10', labelpos='E')
plt.show() 