"""
    Read a file, get a list of random number of items
    Write list to a new file
"""


import pandas as pd
import numpy as np
import random
import csv


if __name__ == '__main__':

    data = pd.read_csv(r'C:\Users\WLiu\Desktop\LifelineCrisisChatsJan.csv', skiprows=9)
    #print data.head()

    mysample = random.sample(data.CallReportNum, 2000)
    #print mysample
    #print type(mysample)
    #mysample.to_csv('sampled.csv')

    with open('sampled.csv', 'wb') as data:
        writer = csv.writer(data)
        writer.writerow(mysample)

    print "Writing complete"