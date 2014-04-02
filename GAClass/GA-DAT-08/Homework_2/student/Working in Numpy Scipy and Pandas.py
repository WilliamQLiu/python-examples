# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>



from numpy import *
from scipy import linalg
import pandas as pd




from numpy import array, dot # No longer neccesary, but shows where we got these functions

X = array([[1, 1], [1, 2], [1, 3], [1, 4]])
y = array([[1], [2], [3], [4]])
n = linalg.inv(dot(X.T, X))
k = dot(X.T, y)
coef_ = dot(n, k)



print X
print '-----------'
print y



# Watch out for namespace issues!!
def regression(X, y):
    return dot(linalg.inv(dot(X.T, X)), dot(X.T, y))



regression(X, y)



a1 = array([ [1, 2], [3, 4] ])
a2 = array([ [1, 3], [2, 4] ])
m1 = matrix('1 2; 3 4')
m2 = matrix('1 3; 2 4')
print a1 * a2
print m1 * m2



print dot(a1, a2)
print dot(m1, m2)



# Numpy Has Great Mathematical Functions!!

print exp(10) # e ^ value
print log(1)
print sqrt(4)



# .T Transposes the array or matrix:
print a1.T



# .I returns the matrix inverse:
print m1.I



# eye(value) creates an identity matrix:
iFive = eye(5)
print iFive



# Lets Get Into Pandas!
df = pd.read_csv('../input/nytimes.csv')



df.describe()



# Create the average impressions and clicks for each age.
dfg = df[ ['Age', 'Impressions', 'Clicks'] ].groupby(['Age']).agg([numpy.mean])
dfg[:3]



# Creating New Columns
df['log_impressions'] = df['Impressions'].apply(numpy.log)



# Function that groups users by age.
def map_age_category(x):
    if x < 18:
        return '1'
    elif x < 25:
        return '2'
    elif x < 32:
        return '3'
    elif x < 45:
        return '4'
    else:
        return '5'

df['age_categories'] = df['Age'].apply(map_age_category)



dfg = df[ ['age_categories', 'Impressions', 'Clicks'] ].groupby(['age_categories']).agg([numpy.mean])
dfg



# Now Load the Data from http://stat.columbia.edu/~rachel/datasets/nyt1.csv for sets 1-30







