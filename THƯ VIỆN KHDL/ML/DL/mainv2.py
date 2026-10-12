import matplotlib.pyplot as plt 

fig = plt.figure()
fig, ax = plt.subplots()
fig, axs = plt.subplots(2,2)

fig, axs = plt.subplot_mosaic([['left', 'right_top'], ['left', 'right_bottom']])

plt.show() 