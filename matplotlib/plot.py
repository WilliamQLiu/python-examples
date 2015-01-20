""" Matplotlib is a python 2D plotting library that mimics MATLAB and works 
    well with NumPy.  

    http://matplotlib.org/api/pyplot_summary.html
    API: http://matplotlib.org/api/pyplot_api.html#module-matplotlib.pyplot
    Tutorial: http://matplotlib.org/users/pyplot_tutorial.html

"""


import matplotlib as mpl  # Only need for configuring default settings
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches  # for legend

import numpy as np


### Default Settings for Matplotlib
print mpl.matplotlib_fname()  # Find configuration file 'matplotlibrc'

### Settings for Pyplot
#plt.switch_backend('agg')
#plt.ion() #Turn on interactive
#plt.ioff() # Non-interactive


if __name__ == '__main__':

    ### Setup Different Types of Data
    a = np.linspace(0, 50, 10, endpoint=False)  # start, stop, num=50 (# of samples), endpoint (stop at last sample?)
    print a  # [0, 5, 10, 15, 20, 25, 30, 35, 40, ]
    b  = np.arange(0, 20, 2)  # start, stop, step; returns evenly spaced values given the interval/step
    print b  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
    c = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
    print c

    ### Set X and Y
    x, y = a, b

    ### Format Text
    plt.figure(figsize=(8,6), dpi=80)  # Create 8*6 inch figure
    plt.title("Test")  # Create a title
    plt.grid()  # Display grid
    plt.xlabel("X axis")  # Create text for X-axis
    plt.ylabel("Y axis")  # Create text for Y-axis
    plt.axes()

    ### Configure X
    plt.xticks(np.arange(min(x), max(x)+1, 1.0))  # How often there are tick labels on x-axis
    plt.xlim(0, 9)  # Set how far we can see x-axis

    ### Configure Y
    plt.yticks(np.arange(min(y), max(y)+1, 2.0))  # How often there are tick labels on y-axis
    plt.ylim(0, )  # Set how far we can see y-axis

    ### Legend
    plt.legend(loc='upper left')
    #plt.legend(bbox_to_anchor=(1,1), loc=2)

    ### Plot
    plt.plot(x, y, color='blue', linewidth=2.5, linestyle='-', label='first')
    plt.plot(x, c, color='red', linewidth=2.5, linestyle='--', label='second')
    #plt.scatter(x, y)  # Create Scatterplot


    ### TODO: Tick Locators - control the position of the ticks

    ### TODO: Annotate specific points - point out neat stuff

    ### TODO: Subplots - arranges plots in a regular grid

    ### TODO: Scatterplots, Bar Plots, Pie charts, Grids, 

    plt.savefig('my_picture.png', dpi=72)  # Save image
    plt.show()  # Display on screen

