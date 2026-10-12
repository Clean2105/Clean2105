import numpy as np 
import matplotlib.pyplot as plt 

from sklearn.ensemble import GradientBoostingRegressor

np.random.seed(1)
def f(X):
    return X * np.sin(X)

X = np.atleast_2d(np.random.uniform(0, 10.0, size=100)).T 
X = X.astype(np.float32)

Y = f(X) .ravel()

dy = 1.5 + 1.0 * np.random.random(Y.shape)
noise = np.random.normal(0, dy)
Y += noise 
Y = Y.astype(np.float32)

xx = np.atleast_2d(np.linspace(0, 10, 1000)).T 
xx = xx.astype(np.float32)

alpha = 0.95

clf = GradientBoostingRegressor(loss='quantile', alpha=alpha, n_estimators=250, 
                                max_depth=3, learning_rate=1, 
                                min_samples_leaf=9, min_samples_split=9)
clf.fit(X,Y)

Y_upper = clf.predict(xx)

clf.set_params(alpha=1.0-alpha)
clf.fit(X,Y) 

Y_lower = clf.predict(xx)

clf.set_params(loss='squared_error')
clf.fit(X,Y)

Y_pred = clf.predict(xx)

fig = plt.figure()
plt.plot(xx, f(xx), 'g-', label=r'$f(X)=X\,\sin(X)$')
plt.plot(X, Y, 'b.', markersize=10, label=u'Observations')
plt.plot(xx, Y_pred, 'r-', label=u'Prediction')
plt.plot(xx, Y_upper, 'k-')
plt.plot(xx, Y_lower, 'k-')

plt.fill(np.concatenate([xx, xx[::-1]]), np.concatenate([Y_upper, Y_lower[::-1]]), alpha=.5, fc='b', ec='None', label='90% prediction interval')
plt.xlabel('$x$')
plt.ylabel('$f(X)$')
plt.ylim(-10,20)
plt.legend(loc='upper left')
plt.show() 