"""creates a random walk graph using python"""

import matplotlib.pyplot as plt
import time
import RandomWalk  as rw


#make random walk
walker = rw.RandomWalk(75_000)
walker.fill_walk()

plt.style.use('seaborn')
plt.figure(figsize=(15,9))
point_numbers = range(walker.num_points)

plt.scatter(walker.x_vals,walker.y_vals, s = 1, c=point_numbers,cmap=plt.cm.Blues,edgecolors='none')

# Add the first and last points on the walk
plt.scatter(walker.x_vals[0],walker.y_vals[0],c='green',s=100,edgecolors='none')
plt.scatter(walker.x_vals[-1],walker.y_vals[-1], c='red',s=100,edgecolors='none')


plt.show()   


