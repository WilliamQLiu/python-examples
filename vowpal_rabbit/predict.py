
import pandas as pd
import numpy as np
import string as stri
from datetime import datetime
import math


def zygmoid(x):
    return 1 / (1 + math.exp(-x))

if __name__ == '__main__':

    with open("/run/shm/results/kaggle.click.submission.csv","wb") as outfile:
            outfile.write("id,click\n")
            for line in open("/run/shm/results/click.preds.txt"):

                row = line.strip().split(" ")
                try:
                    outfile.write("%s,%f\n"%(row[1],zygmoid(float(row[0]))))
                except:
                    pass