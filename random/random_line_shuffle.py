"""
    Opens up a file, randomly shuffles each line, writes back to another
    file.  Useful for stats and machine learning.

    For larger files, use Linux's shuf or Mac's gshuf
"""


import random
INPUT_FILE = '/Users/williamliu/Desktop/train'
OUTPUT_FILE = '/Users/williamliu/Desktop/shuffled'

if __name__ == '__main__':

    print "Opening file..."
    lines = open(INPUT_FILE, 'rU').readlines()
    print "Shuffling file..."
    random.shuffle(lines)
    print "Writing shuffled lines back"
    open(OUTPUT_FILE, 'wb').writelines(lines)
    print "Shuffle Success!"
