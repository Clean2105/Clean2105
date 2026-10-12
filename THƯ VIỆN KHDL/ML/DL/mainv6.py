import matplotlib.pyplot as plt 
import numpy as np 

data1= np.linspace(0,6,100)

fig, axs = plt.subplots(1, 2, figsize=(5, 2.7), layout='constrained')

xdata = np.arange(len(data1))
data = 10 ** data1 
axs[0].plot(xdata, data)
axs[0].set_title('Linear Scale')

axs[1].set_yscale('log')
axs[1].plot(xdata, data)
axs[1].set_title('Log Scale')
plt.show() 