from pandas import DataFrame, read_csv
from numpy import random
import matplotlib.pyplot as plt
import pandas as pd

# List of names
names = ['Bob','Jessica','Mary','John','Mel']

if __name__ == '__main__':
    random.seed(500) # So random samples can be reproduced

    # Setup random names, births, and store as a DataFrame
    random_names = [names[random.randint(low=0, high=len(names))] for i in range(1000)]
    births = [random.randint(low=0, high=1000) for i in range(1000)]
    print "Births, last 10: ", births[:10]

    BabyDataSet = zip(random_names, births)
    print "BabyDataSet, last 10:", BabyDataSet[:10]
    
    df = DataFrame(data = BabyDataSet, columns = ['Names', 'Births'])
    print "DataFrame, last 10: ", df[:10]


    # Get unique properties
    print "Unique Names Array", df['Names'].unique() #['Mary' 'Jessica' 'Bob' 'John' 'Mel']
    
    # Print through all unique properties
    for x in df['Names'].unique():
        print x
    
    # Describe a dataframe
    print df['Names'].describe()
    # count     1000
    # unique       5
    # top        Bob
    # freq       206

    # Use groupby function to aggregate data
    Name = df.groupby('Names')
    df = Name.sum()
    print df
    #        Births
    #Names          
    #Bob      106817
    #Jessica   97826
    #John      90705
    #Mary      99438
    #Mel      102319

    # To get highest occurring names
    Sorted = df.sort(['Births'], ascending=[0])
    print Sorted.head(1)
    # Names        
    # Bob    106817

    # To get highest occurring names (other method)
    print df['Births'].max() # 106817

    ### Presenting Data
    df['Births'].plot(kind='bar')
    plt.show() # Show graph with default of 'Names' as X, Sum as Y

    print "The most popular name"
    df.sort(columns = 'Births', ascending = False)