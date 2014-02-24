#from pylab import *
import matplotlib.pyplot as plt
import numpy as np

#plt.switch_backend('agg')
#plt.ion() #Turn on interactive
#plt.ioff() # Non-interactive

x  = arange(-10.0, 10.0, 0.1)
y = sin(x)
plot(x,y)
show()

"""
# Simple Plot
print plt.get_backend()
plt.plot(range(10), range(10))
plt.title("Simple Plot")
plt.show()
"""

"""
x = np.arange(0, 10, 0.2)
y = np.sin(x)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, y)
plt.show()
"""