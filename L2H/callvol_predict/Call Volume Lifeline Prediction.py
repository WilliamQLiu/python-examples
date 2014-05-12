# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=1>

# Linear Regression - Call Volume Prediction

# <markdowncell>

# * Linear Regression doing Call Predictions for future
# * Looks at past rate of calls answered per day, does train/test split, then classifies with Linear Regression using sci-kit learn

# <codecell>

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
%matplotlib inline
%pylab inline
plt.xkcd() # Comment out to plot regular graphs instead of xkcd style

# <headingcell level=3>

# Load Data

# <codecell>

df = pd.DataFrame.from_csv('C:\Users\wliu\Desktop\lifelinecalls.csv')

# <codecell>

df.info()

# <codecell>

mydf = df[['AttemptStatus', 'EasternTime', 'IsVeteransNetwork']]

# <codecell>

mydf.dropna(inplace=True)

# <codecell>

mydf = mydf[mydf['AttemptStatus']=='DC'] # Get Calls Answered only
mydf['AttemptStatus'] = [1 if field=='DC' else 0 for field in mydf['AttemptStatus']] # Mark all Calls Answered as 1

# <codecell>

pd.unique(mydf.AttemptStatus.values.ravel()) # Find unique values in column

# <codecell>

mydf.info()

# <codecell>

mydf.dtypes

# <codecell>

mydf['EasternTime'] = pd.to_datetime(mydf['EasternTime'])

# <codecell>

mydf.dtypes

# <codecell>

print mydf.head()

# <codecell>

mydf = mydf.set_index('EasternTime')

# <codecell>

mydf.tail()

# <codecell>

mydf = mydf['20120101':'20140430']

# <codecell>

mydf.head()

# <headingcell level=4>

# Actual

# <codecell>

actual_calls = mydf.resample('m', how='sum') # m for month, D for day, 'AS-JAN' for Yearly with Jan as beginning

# <codecell>

print actual_calls.head()

# <codecell>

mydf = mydf.resample('d', how='sum') # Resample to per day (D) or month (m)
mydf.head(10)

# <codecell>

# Plot all the data
from matplotlib.font_manager import FontProperties
mydf.plot(kind='line', alpha=.7)
fontP = FontProperties()
fontP.set_size('small')
legend({"All Lifeline" : 1, "Veterans" : 1}, "title", prop = fontP)
axes=plt.plot()
axes=plt.gca()
axes.grid(False)
axes.set_title('CALLS BY TIME')
axes.set_xlabel('Time')
axes.set_ylabel('Number of Calls Answered')
plt.show()

# <codecell>

plt.scatter(mydf.index, mydf.AttemptStatus, alpha=.3, c='r')
plt.scatter(mydf.index, mydf.IsVeteransNetwork, alpha=.5, c='b')

# <codecell>

mydf = mydf.reset_index()

# <codecell>

#mydf.head()
mydf.tail()

# <codecell>

mydf.info()
mydf.describe()

# <codecell>

mydf = mydf.replace(np.nan, 0) # Removes NaNs

# <headingcell level=3>

# Create Train and Test Data

# <codecell>

# Create Train and Test Data
from sklearn.cross_validation import cross_val_score
from sklearn.cross_validation import train_test_split
#from sklearn.preprocessing import scale

X_train, X_test, y_train, y_test = train_test_split(
    mydf.index, mydf['IsVeteransNetwork'], test_size=0.25, random_state=100)
print "X train:", X_train.shape, "  ", "X test:", X_test.shape
print "y train:", y_train.shape, "  ", "y test:", y_test.shape

# <codecell>

#print X_train
#print y_train

# <codecell>

print "X train size is:", X_train.size
print "X train is type:", type(X_train)

# <headingcell level=3>

# Fit to Linear Regression Model

# <codecell>

from sklearn import linear_model

classifier = linear_model.LinearRegression()
classifier.fit(X_train.reshape(-1,1), y_train)

# <codecell>

print "Coefficient is: ", classifier.coef_
print "Intercept is: ", classifier.intercept_

# <codecell>

X_test

# <codecell>

predicted = classifier.predict(X_test.reshape(-1,1))

# <codecell>

predicted

# <codecell>

x_line = np.linspace(0, 3285, 200)
predicts = classifier.predict(x_line.reshape(-1,1))
plt.plot(x_line, predicts, '--', alpha=1)
plt.scatter(x=X_train, y=y_train, alpha=.1)
plt.show()

# <codecell>

classifier.score(X_test.reshape(-1,1), y_test)

# <codecell>

type(X_train)

# <headingcell level=3>

# Prediction

# <codecell>

# Predict for Months
#for x in xrange(112, 120):
#    print classifier.predict(x)

# <codecell>

# Create dataframe, one for index, one column for days, and one for predicted output

# Index
my_index = []
for x in xrange(0, 3288):
    my_index.append(x)
print my_index

# <codecell>

# Time Range
time_rng = pd.date_range('1/1/2012', periods=3288, freq='D')
print time_rng

# <codecell>

# Predicted Output in Days
pred_output=[]
for x in xrange(0, 3288):
    temp = classifier.predict(x)
    pred_output.append(int(temp))

# <codecell>

my_data = zip(my_index, time_rng, pred_output)

# <codecell>

print my_data

# <codecell>

print type(my_data)

# <codecell>

eval_df = pd.DataFrame(data = my_data, columns=['DaysSince', 'Date', 'Pred_Output'])
eval_df.tail()

# <codecell>

eval_df['Date'] = pd.to_datetime(eval_df['Date'])
eval_df = eval_df.set_index('Date')

# <codecell>

print eval_df.head()

# <codecell>

eval_df = eval_df.resample('m', how='sum') # Resample to per day (D) or month (m), 'AS-JAN' (yearly with Jan as beginning)
print eval_df

# <codecell>

# Plot all the data
actual_calls.plot(kind='line', y='IsVeteransNetwork', alpha=.6)
eval_df.plot(kind='line', y='Pred_Output', alpha=.7, style='-', c='g')
fontP = FontProperties()
fontP.set_size('small')
legend({"Actual" : 1, "Predicted" : 1}, "title", prop = fontP)
axes=plt.plot()
axes=plt.gca()
axes.grid(False)
axes.set_title('PREDICTED CALLS ANSWERED \nPER MONTH (LIFELINE)')
axes.set_xlabel('Time')
axes.set_ylabel('Number of Calls Answered')
plt.show()

# <headingcell level=1>

# TESTING BELOW - IGNORE FOR NOW

# <headingcell level=3>

# Using DictVectorizer to explode Features

# <codecell>

df = pd.DataFrame.from_csv('C:\Users\wliu\Desktop\lifelinecalls_small.csv')

# <codecell>

dvdf = df[['AttemptStatus', 'EasternTime']]

# <codecell>

dvdf = dvdf[dvdf['AttemptStatus']=='DC'] # Get Calls Answered only
dvdf['AttemptStatus'] = [1 if field=='DC' else 0 for field in dvdf['AttemptStatus']] # Mark all Calls Answered as 1

# <codecell>

dvdf['EasternTime'] = pd.to_datetime(dvdf.EasternTime)

# <codecell>

from time import strftime

dvdf['Year'] = dvdf.EasternTime.apply(lambda x: x.strftime("%Y"))
dvdf['Month'] = dvdf.EasternTime.apply(lambda x: x.strftime("%b"))
dvdf['Day'] = dvdf.EasternTime.apply(lambda x: x.strftime("%a"))
dvdf['Hour'] = dvdf.EasternTime.apply(lambda x: x.strftime("%H"))

# <codecell>

dvdf.head()

# <codecell>

dvdf.set_index('EasternTime')

# <codecell>

dvdf = dvdf.resample('m', how='sum') # Resample to per day (D) or month (m)

# <codecell>

from sklearn.feature_extraction import DictVectorizer

X_temp = dvdf[['Year', 'Month', 'Day', 'Hour']]
y_temp = pd.DataFrame(dvdf['AttemptStatus'])

dv = DictVectorizer()
X_matrix = dv.fit_transform(X_temp.T.to_dict().values())
y_matrix = dv.fit_transform(y_temp.T.to_dict().values())

# <codecell>

print "X Matrix is: ", X_matrix
print "Y Matrix is: ", y_matrix

# <codecell>

dvdf.dropna(inplace=True)

# <codecell>

dvdf.shape

# <codecell>

# Create Train and Test Data
from sklearn.cross_validation import cross_val_score
from sklearn.cross_validation import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    dvdf[['Year', 'Month', 'Day', 'Hour', 'AttemptStatus']], dvdf[['AttemptStatus']], test_size=0.25, random_state=100)
print "X train:", X_train.shape, "  ", "X test:", X_test.shape
print "y train:", y_train.shape, "  ", "y test:", y_test.shape

# <codecell>

print "X train is: ", X_train
print "Y train is: ", y_train

# <codecell>

X_train_matrix

# <codecell>

from sklearn import linear_model

classifier = linear_model.LinearRegression()
classifier.fit(X_train_matrix, y_train)

# <codecell>

print classifier.coef_

# <codecell>

classifier.predict(100)

# <codecell>


