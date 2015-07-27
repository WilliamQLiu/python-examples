import pandas as pd
import numpy as np

data_a = pd.DataFrame({
        'date':[
            '1959-03-01 00:00:00', '1959-03-02 00:00:00', '1959-03-03 00:00:00',
            '1959-03-31 00:00:00', '1959-06-02 00:00:00', '1959-06-04 00:00:00',
            '1959-09-30 00:00:00', '1959-10-01 00:00:00', '1959-10-15 00:00:00',
            '1959-12-31 00:00:00'],
        'item':['realgdp', 'infl', 'unemp', 'realgdp', 'infl', 'unemp',
            'realgdp', 'infl', 'unemp', 'realgdp'],
        'value':[2710.349, 0.000, 5.800, 2778.801, 2.340, 5.100,
            2775.488, 2.740, 5.300, 2785.204]
        }, index=range(0, 10))

data_b = pd.DataFrame({
        ''
    })

if __name__ == '__main__':

    print data_a
    #                  date     item     value
    #0  1959-03-01 00:00:00  realgdp  2710.349
    #1  1959-03-02 00:00:00     infl     0.000
    #2  1959-03-03 00:00:00    unemp     5.800
    #3  1959-03-31 00:00:00  realgdp  2778.801
    #4  1959-06-02 00:00:00     infl     2.340
    #5  1959-06-04 00:00:00    unemp     5.100
    #6  1959-09-30 00:00:00  realgdp  2775.488
    #7  1959-10-01 00:00:00     infl     2.740
    #8  1959-10-15 00:00:00    unemp     5.300
    #9  1959-12-31 00:00:00  realgdp  2785.204

    # get_value returns a single value with a passed index and column
    print data_a.loc[2, 'item']  # unemp
    #print data_a.get_value(2, 'item')  # unemp  # DEPRECATED


    # returns values of an ndarray given a sequence of row labels and column labels
    print data_a.lookup([2, 4], ['item', 'value'])  # ['unemp' 2.3399999999999999]


    # returns specific column values
    print data_a.loc[:,('item', 'value')]
    #      item     value
    #0  realgdp  2710.349
    #1     infl     0.000
    #2    unemp     5.800
    #3  realgdp  2778.801
    #4     infl     2.340
    #5    unemp     5.100
    #6  realgdp  2775.488
    #7     infl     2.740
    #8    unemp     5.300
    #9  realgdp  2785.204

