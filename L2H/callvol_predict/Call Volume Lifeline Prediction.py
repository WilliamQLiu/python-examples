# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

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
mydf['AttemptStatus'] = [1 if field=='DC' else 0 for field in mydf['AttemptStatus']]

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

mydf = mydf.set_index('EasternTime')

# <codecell>

mydf.tail()

# <codecell>

mydf = mydf[:'20140430']

# <codecell>

mydf = mydf.resample('m', how='sum') # Resample to per day (D) or month (m)
mydf.head()

# <codecell>

# Plot all the data
mydf.plot(kind='bar')

#plt.scatter(X_train, y_train, alpha=1)
axes=plt.plot()
axes=plt.gca()
axes.grid(False)
axes.set_title('CALLS BY TIME')
axes.set_xlabel('Time')
axes.set_ylabel('Number of Calls Answered')

plt.show()

# <codecell>

plt.scatter(mydf.index, mydf.AttemptStatus, alpha=.3, c='r')
#plt.scatter(mydf.index, mydf.IsVeteransNetwork, alpha=.5, c='b')

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
    mydf.index, mydf['AttemptStatus'], test_size=0.25, random_state=100)
print "X train:", X_train.shape, "  ", "X test:", X_test.shape
print "y train:", y_train.shape, "  ", "y test:", y_test.shape

# <codecell>

print X_train
print y_train

# <codecell>

print "X train size is:", X_train.size

# <codecell>

#from sklearn.feature_extraction import DictVectorizer

#dv = DictVectorizer()
#X_train_matrix = dv.fit_transform(X_train.T.to_dict().values())

# If features don't match between train and test, then use just 'transform'
# because if a value does not exist in the test data, it drops that column
# using fit_transform
#X_test_matrix = dv.transform(X_test.T.to_dict().values())

#correlation_matrix = dv.fit_transform(df_features.T.to_dict().values())
#col_names = dv.get_feature_names()

# <codecell>

plt.plot_date(x=X_train, y=y_train, alpha=.05)

#plt.scatter(X_train, y_train, alpha=1)
axes=plt.plot()
axes=plt.gca()
axes.grid(False)
axes.set_title('CALLS BY TIME')
axes.set_xlabel('Time')
axes.set_ylabel('Y')
plt.show()

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

x_line = np.linspace(0, 120, 200)
predicts = classifier.predict(x_line.reshape(-1,1))
plt.plot(x_line, predicts, '--', alpha=1)
plt.scatter(x=X_train, y=y_train, alpha=.01)

plt.show()

# <codecell>

classifier.score(X_test.reshape(-1,1), y_test)

# <codecell>

classifier.predict(112)

# <codecell>


