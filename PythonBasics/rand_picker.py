""" Take a list, pick X random items """

import random

items = [
    22200623,
    22200365,
    22215672,
    22198166,
    22182962,
    22182648,
    22181937,
    22134238,
    22098423,
    22089540,
    22060999
]


if __name__ == '__main__':

    random.shuffle(items)  # Shuffle things around
    print random.sample(items, 3)  # Pick x out of the items
