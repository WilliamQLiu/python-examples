""" Datetime Dataframe manipulations """

from datetime import datetime # From standard library, to use datetime format
from dateutil.parser import parse # Allows automatic parsing of dates

import numpy as np
import pandas as pd
from pandas.tseries.offsets import Hour, Minute, Day, MonthEnd, MonthBegin, YearBegin


def stdlib_get_time():
    """ Standard Library Date and Time Tools """
    now = datetime.now()
    print "Datetime is", now # 2014-03-31 10:06:29.826000
    print "Year is", now.year # 2014
    print "Month is", now.month # 3
    print "Day is", now.day # 31
    print "\n"


def read_datetime():
    """ Convert a string to date """
    stamp = datetime(2014, 11, 13)
    print "Explicitly stating datetime", stamp # 2014-11-13 00:00:00

    str_value = '2014-01-11'
    date_value = datetime.strptime(str_value, '%Y-%m-%d') # 2014-01-11 00:00:00
    print "String conversion to datetime", date_value

def dateutil_parser():
    """ Use third party library to parse almost any type of date"""
    print "Date parsed is", parse('Jan 31, 1997 10:45 PM') # 1997-01-31 22:45:00
    print "\n"


def series_date():
    """ Setting a DatetimeIndex on a Series """
    dates = [datetime(2011, 1, 2), datetime(2011, 1, 5), datetime(2011, 1, 7),
        datetime(2011, 1, 8), datetime(2011, 1, 10), datetime(2011, 1, 12)]
    ts = pd.Series(np.random.randn(6), index=dates) # Random nums to timeseries
    print type(ts) # <class 'pandas.core.series.Series'>
    print "This is now a TimeSeries type \n", ts
    #Pandas stores timestamps using NumPy's datetime64 data type (to nanosecond)
    print "TimeSeries index datatype is:", ts.index.dtype

    # Indexing and Selecting Data
    print "Selecting a specific row index:", ts.index[2] # 2011-01-07 00:00:00


def slicing_series():
    """ How to slice a DateTime Series """
    longer_ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000',
        periods=1000))
    print "Long TimeSeries is: \n", longer_ts
    print type(longer_ts) # <class 'pandas.core.series.Series'>

    print "Slicing by date (year): \n", longer_ts['2001']
    print "Slicing by date range: \n", longer_ts['2001-05':'2011-06']


def convert_to_datetime():
    """ How to convert a Series into a Time Series """
    now_ts = pd.to_datetime(pd.Series(['Jul 31, 2009', '2010-01-10', None]))
    print "Converting Series to a Time Series", now_ts


def timestamp_duplicates():
    """ How to handle duplicates in a timestamp """
    dates = pd.DatetimeIndex(['1/1/2000', '1/2/2000', '1/2/2000', '1/2/2000',
        '1/3/2000'])
    dup_ts = pd.Series(np.arange(5), index=dates)
    print "TimeSeries with Duplicates: \n", dup_ts
    print "Is Index unique?", dup_ts.index.is_unique

    # Aggregate data by having non-unique timestamps using groupby
    grouped = dup_ts.groupby(level=0) #the only level of indexing
    print "Mean of grouped: \n", grouped.mean()
    print "Count of grouped: \n", grouped.count()


def timestamp_resample():
    """ How to assign a fixed frequency"""
    dates = pd.DatetimeIndex(['1/1/2000', '1/1/2000', '1/10/2000',
        '2/2/2000', '2/3/2000'])
    my_ts = pd.Series(np.arange(5), index=dates)
    my_ts = my_ts.resample('D') # Resample by Days
    print "Resampled TimeStamp \n", my_ts


def timestamp_dateoffset():
    """ How to set a date offset using Shift """
    hour = pd.tseries.offsets.Hour()
    print hour # <Hour>
    four_hours = pd.tseries.offsets.Hour(4)
    print four_hours # <4 * Hours>

    rng = pd.date_range('1/1/2000', '12/31/2000 23:59', freq='MS') # Pass freq
    ts = pd.Series(np.random.randn(12), index=rng)
    print type(rng) # <class 'pandas.tseries.index.DatetimeIndex'>
    print "Ranges cover:\n", list(rng)

    print "Original List:\n", ts
    print "Shifting index forward 2:\n", ts.shift(2)
    #print "Shifting index backwards 2:\n", ts.shift(-1, freq='M')
    print "Percent change in times\n", ts / ts.shift(1) - 1


def timestamp_rollforward_rollback():
    """ How to role the date forward (end of time) or backward (beg of time) """
    now = datetime(2014, 4, 15)
    print "Current time is:", now
    now = now + 3 * Day()
    print "Adding 3 days to now:", now

    offset = MonthEnd()
    now = offset.rollforward(now)
    print "Rolling foward to last day of the month", now

    offset = MonthBegin()
    now = offset.rollback(now)
    print "Rolling foward to first day of the month", now

    ts = pd.Series(np.random.randn(20), index=pd.date_range('1/1/2000',
        periods=20, freq='4d'))
    print "Original Time Series is:\n", ts

    offset = YearBegin()
    ts = ts.groupby(offset.rollforward).mean()
    print "Time Series after rolling forward\n", ts


def period_test():
    """ How to use Periods to represent time spans like days, months, years"""
    p = pd.Period('2007-1-1', freq='A-DEC') # Anchor Annual last given month
    print "Original Period is", p #2007

    pd_rng = pd.period_range('1/1/2013', '3/30/2014', freq='M')
    print "Period Range is", pd_rng

    new_p = p.asfreq('M', how='start')
    print "Changed frequency (with start)", new_p # 2007-01
    new_p = p.asfreq('M', how='end')
    print "Changed frequency (with end)", new_p # 2007-12

    pi = pd.PeriodIndex(['2011-1-1', '2011-2', '2011-3', '2011-5'], freq='M')
    print type(pi) # <class 'pandas.tseries.period.PeriodIndex'>


if __name__ == "__main__":
    #stdlib_get_time() # how to use standard library's datetime funcs
    #read_datetime() # how to read in datetimes
    #dateutil_parser() # 3rd party library to parse datetimes
    #series_date() # how to manipulate set Date Time Index on a Series
    #slicing_series() # how to slice data by Time Series Index
    #convert_to_datetime() # How to return a Series of Date Time Stamps
    #timestamp_duplicates() # How to handle duplicates in Time Series
    timestamp_resample() # How to create a fixed frequency date index
    #timestamp_dateoffset() # How to shift the data on index by a specific time
    #timestamp_rollforward_rollback() # How to roll fwd and back by date index
    #period_test()
    #timestamp_rollforward_rollback() # How to roll fwd and back by date index
