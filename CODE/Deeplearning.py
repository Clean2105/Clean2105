import numpy 
import matplotlib.pyplot as plt 

weightValue = 1000

biasValue = 5000

biasValue2 = -5000

plt.axis([-10, 10, -1, 10]) 

print("The step function starts at {0} and ends at {1}".format(-biasValue/weightValue, -biasValue2/weightValue))

x = numpy.linspace(-10, 10, 1000)
y1 = 1.0 /(1.0 + numpy.exp(-weightValue*x - biasValue))
y2 = 1.0 /(1.0 + numpy.exp(-weightValue*x - biasValue2))
w = 7 
y = y1*w-y2*w 
plt.plot(x, y, lw=2, color='black')
plt.grid(True, linestyle='-')
plt.show() 