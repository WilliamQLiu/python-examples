"""
    PyPrind basically shows a Progress Bar and Percentage Indicator, mainly
    (good for loops)
"""


import pyprind as pp
import time
#import psutil


def setup_progress_bar(self, filename):
    with open(filename, 'rU') as data:
        self._total_lines = sum(1 for row in data)
    data.close()
    print "Total lines in file is: ", self._total_lines


def simple_example(items):
    """ Simple use of Progress bar in a for loop """
    pbar = pp.ProgBar(len(items), title='My Progress Bar 1')

    for i in items:
        time.sleep(0.5)  # do some computation
        pbar.update()


def advanced_example(items):
    """ Advanced Progress bar in a for loop (shows item,
        completion stats of start time, end time, cpu%, mem%) """
    pbar = pp.ProgBar(len(items), monitor=True,
                      title='My Progress Bar 2')

    for i in items:
        time.sleep(0.5)  # do some computation
        pbar.update(item_id='Item %s' %i)
    print pbar


if __name__ == '__main__':

    ### Create a simple list
    my_list = []
    for x in xrange(100):
        my_list.append(x+1)
    print my_list

    #simple_example(my_list)  # do a simple progress bar

    advanced_example(my_list)  # do an advanced progress bar
