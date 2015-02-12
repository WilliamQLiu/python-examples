""" Another random shuffle program by line """


import random

if __name__ == '__main__':

    with open('/Users/williamliu/Desktop/Kaggle_Avazu/click.train_original_data.vw','r') as source:
        data = [ (random.random(), line) for line in source ]
    data.sort()
    with open('/Users/williamliu/Desktop/Kaggle_Avazu/click.train_shuffle_data.vw','w') as target:
        for _, line in data:
            target.write( line )