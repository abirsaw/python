import sys
import matplotlib
matplotlib.use('agg')

import matplotlib.pyplot as plt
import numpy as np
x_points=np.array([0,10])
y_points = np.array([0,100])

plt.point (x_points,y_points, level = "linear")
plt.show()
