""" Using Python's requests library """

import requests


def get_webpage(site):
    """ GET """
    r = requests.get(site)


if __name__ == '__main__':
    get_webpage('https://api.github.com/events')
