"""
    There's many ways to process csv files, each with its own adv/disadv.
    You can use csv loops, pandas' DataFrame.read_csv, or create a class.

    The csv module doesn't support encoding, reading, or writing data from
    a file so we use the `unicodecsv` module when we can; this helps
    translate the native file to 'UTF-8', which the csv module can read.

    Basics of CSV Processing from documentation and tutorial:
    https://docs.python.org/2/library/csv.html
    https://districtdatalabs.silvrback.com/simple-csv-data-wrangling-with-python
"""

import pandas as pd
import collections  # high performance container datatypes
import sys # for warnings
try:
    import unicodecsv as csv  # for UTF8Recoder, UnicodeReader, UnicodeWriter classes
except ImportError:
    import warnings
    warnings.warn("can't import `unicodecsv` encoding errors may occur")
    import csv


def read_simple_data(path):
    """ How to read a csv file lazily (i.e. no more than one row is in mem),
        Few things to note:
        * mode 'rU' is opening file in universal newline mode
        * use csv.DictReader only when headers present, otherwise csv.reader
        * using `with [callable] as [name]` ensures handle automatically closes
     """
    with open(path, 'rU') as data:  # wrap reader in a function that returns a generator
        reader = csv.DictReader(data)  # use csv.reader if no header
        for row in reader:
            yield row  # yield returns the generator, don't need to upload all in memory


def read_data_catch_errors(path):
    """ Same as above, but catches and reports on errors """
    with open(path, 'rU') as data:  # also can try rb
        reader = csv.DictReader(data)
        try:
            for row in reader:
                yield row
        except csv.Error as e:
            sys.exit('File %s, line %d: %s' % (path, reader.line_num, e))


def write_simple_data(path):
    """ Write data instead of read data """
    with open(path, 'wb') as data:
        writer = csv.writer(data)
        for row in writer:
            writer.writerows(row)


class FundingReader(object):
    """ A class can save some state of the data between reads """

    def __init__(self, path):
        self.path = path
        self._length = None
        self._counter = None

    def __iter__(self):
        self._length = 0
        self._counter = collections.Counter()
        with open(self.path, 'rU') as data:
            reader = csv.DictReader(data)
            for row in reader:
                # Save these statistics
                self._length += 1
                self._counter[row['company']] += 1

                yield row

    def __len__(self):
        if self._length is None:
            for row in self: continue  # Read the data for length and counter
        return self._length

    @property
    def counter(self):
        if self._counter is None:
            for row in self: continue  # Read the data for length and counter
        return self._counter

    @property
    def companies(self):
        return self.counter.keys()

    def reset(self):
        """ In case of partial seeks (e.g. breaking in the middle of the read)
        """
        self._length = None
        self._counter = None


### Adds support for reading and writing Unicode (UTF-8, not UTF-16)
### Apply by using these as a wrapped function or just use `unicodecsv`
#  https://docs.python.org/2/library/csv.html
def unicode_csv_reader(unicode_csv_data, dialect=csv.excel, **kwargs):
    # csv.py doesn't do Unicode; encode temporarily as UTF-8:
    csv_reader = csv.reader(utf_8_encoder(unicode_csv_data),
                            dialect=dialect, **kwargs)
    for row in csv_reader:
        # decode UTF-8 back to Unicode, cell by cell:
        yield [unicode(cell, 'utf-8') for cell in row]

def utf_8_encoder(unicode_csv_data):
    for line in unicode_csv_data:
        yield line.encode('utf-8')
### Note: recommend just importing `unicodecsv` instead of these two methods


if __name__ == '__main__':
    ### READING DATA
    mypath = 'funding.csv'
    #|-----------+------------+-------- +---------+------------+-------+------------+-----------+----------------+------|
    #|permalink  | company    | numEmps | category| city       | state | fundedDate | raisedAmt | raisedCurrency | round|
    #|-----------+------------+-------- +---------+------------+-------+------------+-----------+----------------+------|
    #|lifelock   | LifeLock   |         | web     | Tempe      | AZ    | 1-May-07   | 6850000   | USD            | b    |
    #|lifelock   | LifeLock   |         | web     | Tempe      | AZ    | 1-Oct-06   | 6000000   | USD            | a    |
    #|lifelock   | LifeLock   |         | web     | Tempe      | AZ    | 1-Jan-08   | 25000000  | USD            | c    |
    #|mycityfaces| MyCityFaces| 7       | web     | Scottsdale | AZ    | 1-Jan-08   | 50000     | USD            | seed |


    ### Using simple csv method - Print first 11 items - shows we can read the file using our function
    for index, row in enumerate(read_simple_data(mypath)):
        if index > 10: break
        print "%(company)s (%(numEmps)s employees) raised %(raisedAmt)s on %(fundedDate)s" % row


    ### Using same as above, but catches and returns errors
    for index, row in enumerate(read_data_catch_errors(mypath)):
        if index > 10: break
        print "%(company)s (%(numEmps)s employees) raised %(raisedAmt)s on %(fundedDate)s" % row


    ### Using pandas.read_csv method
    #df = pd.read_csv(filepath_or_buffer=mypath, sep=",")
    #print df.head()

    ### Using csv class
    reader = FundingReader(mypath)
    print "Funding reader with %i rows and %i companies" % (len(reader), len(reader.companies))


    ### WRITING