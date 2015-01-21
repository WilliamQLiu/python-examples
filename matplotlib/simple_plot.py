""" Matplotlib is a python 2D plotting library that mimics MATLAB and works 
    well with NumPy.

    http://matplotlib.org/api/pyplot_summary.html
    API: http://matplotlib.org/api/pyplot_api.html#module-matplotlib.pyplot
    Tutorial: http://matplotlib.org/users/pyplot_tutorial.html

    Note: Differences from Pyplot Vs Pylab
    These are just different ways of doing the same thing;
    pyplot is the python plotting library on matplotlib and so is pylab,
    but pylab also imports numpy automatically.  By default, just use
    pyplot and import numpy because its cleaner to not pollute namespace.

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


def simple_plot():
    """ Do a simple plot """

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
    #plt.set_xticklabels()  # Set X tick labels (e.g. if you want 3.142 to be pi symbol instead)
    plt.xlim(0, 9)  # Set how far we can see x-axis

    ### Configure Y
    plt.yticks(np.arange(min(y), max(y)+1, 2.0))  # How often there are tick labels on y-axis
    #plt.set_yticklabels()  # Set Y tick lables (e.g. if you want 3.142 to be pi symbol instead)
    plt.ylim(0, )  # Set how far we can see y-axis

    ### Legend
    plt.legend(loc='upper left')
    #plt.legend(bbox_to_anchor=(1,1), loc=2)

    ### Plot
    plt.plot(x, y, color='blue', linewidth=2.5, linestyle='-', label='first')
    plt.plot(x, c, color='red', linewidth=2.5, linestyle='--', label='second')

    ### TODO: Scatterplots, Bar Plots, Pie charts
    #plt.scatter(x, y, alpha=0.5)  # Create Scatterplot

    ### TODO: Annotate specific points - point out neat stuff
    #plt.annotate('Neat text here', xy=(0, 1), xycoords='data',
    #   xytext=(-50, 30), textcoords='offset points', arrowprops=dict(arrowstyle="->"))

    ### TODO: Tick Locators - control the position of the ticks

    plt.savefig('my_picture.png', dpi=72)  # Save image
    plt.show()  # Display on screen


def simple_subplot():
    """ How to generate subplots.  Subplots can be arranged like this:
    https://scipy-lectures.github.io/intro/matplotlib/matplotlib.html#subplots

    If you want the placement of a smaller plot into a larger plot at any
    location, then use 'Axes'
    """

    ### Make some data
    x1 = np.linspace(0.0, 5.0)
    x2 = np.linspace(0.0, 2.0)

    y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
    y2 = np.cos(2 * np.pi * x2)

    ### First plot (top)
    plt.subplot(2, 1, 1)  # (grid rows, grid columns, grid pos for new axes)
    plt.plot(x1, y1, 'ko-')
    plt.title('A tale of 2 subplots')
    plt.ylabel('Damped oscillation')

    ### Second plot (bottom)
    plt.subplot(2, 1, 2)  # (grid rows, grid columns, grid pos for new axes)
    plt.plot(x2, y2, 'r.-')
    plt.xlabel('time (s)')
    plt.ylabel('Undamped')

    plt.show()  # Display plot


if __name__ == '__main__':
    simple_plot()  # Do a basic plot
    simple_subplot()  # Have multiple plots    
