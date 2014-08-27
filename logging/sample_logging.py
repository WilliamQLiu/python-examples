import logging


def log_console_basic():
    """ Start Log to console """
    print "Logging to console"
    logging.warning('Watching out!')  # will print a message to the console
    logging.info('I told you so')  # will not print anything
    print "see logging from command-line: python sample_logging.py --log=INFO"
    print "End logging to console"


def log_to_file():
    """ Log to file """
    print "Start Logging to file"
    logging.basicConfig(filename='mytest.log', level=logging.DEBUG)
    logging.debug('This message should go to the log info')
    logging.info('So should this')
    logging.warning('And this, too')
    logging.warning('%s before you %s', 'Look', 'leap!')  # log variables
    print "File should now have four lines of logs"
    print "End logging to file"


def log_time():
    """ How to log specific times """
    print "Start Logging time"

    # 2014-08-26 16:18:21,888
    #logging.basicConfig(format='%(asctime)s %(message)s')  # ISO8601

    # 08/26/2014 04:15:23 PM
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    logging.warning('is the start of when this event was logged.')

if __name__ == '__main__':

    #log_console_basic()
    #log_to_file()
    log_time()
