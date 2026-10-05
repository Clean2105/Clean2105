import numpy as np 
rg = np.random.default_rng(1) 
import matplotlib.pyplot as plt 
mu, sigma = 2, 0.5
v = rg.normal(mu, sigma, 1000)
count, bins, ignored = plt.hist(v, bins=50, density=True, alpha=0.6, color='b', label='Sample Histogram')
bin_centers = 0.5 * (bins[1:] + bins[:-1])
pdf_curve = 1 / (sigma * np.sqrt(2 * np.pi)) * np.exp(- (bins - mu)**2 / (2 * sigma**2))
plt.plot(bins, pdf_curve, linewidth=2, color='r', label='Theoretical PDF')
plt.xlabel('Values')
plt.ylabel('Density')
plt.title('Normal Distribution Histogram')
plt.legend()
plt.show()