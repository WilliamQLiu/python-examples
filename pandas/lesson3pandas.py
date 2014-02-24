# Import libraries
from pandas import DataFrame, date_range, read_excel, concat
import pandas as pd
import matplotlib.pyplot as plt
import numpy.random as np

def CreateDataSet(Number=1):
    Output = []
    for i in range(Number):

        #Create a weekly (Mondays) date range
        rng = date_range(start='1/1/2009', end='12/31/2012', freq='W-MON')

        # Create random data
        data = np.randint(low=25, high=1000, size=len(rng))

        # Status pool
        status = [1,2,3]

        # Make a random list of statuses
        random_status = [status[np.randint(low=0, high=len(status))] for i in range(len(rng))]

        # State pool
        states = ['GA', 'FL', 'fl', 'NY', 'NJ', 'TX']

        # Make a random list of states
        random_states = [states[np.randint(low=0, high=len(states))] for i in range(len(rng))]

        Output.extend(zip(random_states, random_status, data, rng))

    return Output


if __name__ == "__main__":
    ### Setting up Data
    np.seed(500) # Set seed so we can reproduce results
    dataset = CreateDataSet(4)
    df = DataFrame(data=dataset, columns=['State', 'Status', 'CustomerCount', 'StatusDate'])

    print df.info()
    #<class 'pandas.core.frame.DataFrame'>
    #Int64Index: 836 entries, 0 to 835
    #Data columns (total 4 columns):
    #State            836 non-null object
    #Status           836 non-null int64
    #CustomerCount    836 non-null int64
    #StatusDate       836 non-null datetime64[ns]
    #dtypes: datetime64[ns](1), int64(2), object(1)None

    print df.head()

    # How to write data to read_excel
    #df.to_excel('Lesson3.xlsx', index=False)

    ### Reading Data
    