"""
    logging defines functions and classes that implement a flexible logging
    system.  logging is important for debugging and running (e.g. what happened
    when a system crashed)

"""

import logging


def log_console_basic():
    """ Start Log to console """
    print "Logging to console"
    logging.warning('Watching out!')  # will print a message to the console
    logging.info('I told you so')  # will not print anything
    print "see logging from command-line: python sample_logging.py --log=INFO"
    print "End logging to console"


def log_to_file_simple():
    """ Log to file; can be different levels (Critical, Error, Warning, Info,
        Debug, Notset) """

    print "Start Logging to file"
    logging.basicConfig(filename='mytest.log', level=logging.DEBUG)
    logging.debug('This message should go to the log info')
    logging.info('So should this')
    logging.warning('And this, too')
    logging.warning('%s before you %s', 'Look', 'leap!')  # log variables
    print "File should now have four lines of logs"
    print "End logging to file"


def log_to_file_realworld():
    """ Log to file; this example is reading db, updating db, finishing """
    logging.basicConfig(filename='mytest.log', level=logging.INFO)
    logger = logging.getLogger(__name__)

    logger.info('Start reading database')
    # Read database

    records = {'john': 55, 'tom': 66}
    logger.debug('Records: %s', records)
    logger.info('Updating records ... ')
    # Update records

    logger.info('Finishing Updating records')



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
    #log_to_file_simple()
    #log_to_file_realworld()
    log_time()
