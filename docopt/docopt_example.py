""" docopt is a library for parsing command line arguments.
    docopt creates beautiful command-line interfaces easily
        Usage:
          docopt_example.py test1
          docopt_example.py test1 new <name>
          docopt_example.py test1 <x> <y>
          docopt_example.py test (set|remove) <x> <y> [--moored|--drifting]
          docopt_example.py (-h | --help)
          docopt_example.py --version

        Options:
          -h --help        Show this screen
          --version        Show version
          --myfield        My custom field

     """


from docopt import docopt


if __name__ == '__main__':

    arguments = docopt(__doc__, version='1')
    print arguments
