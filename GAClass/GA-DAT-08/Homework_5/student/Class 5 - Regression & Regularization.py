# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

!pip install -U scikit-learn
!pip install -U patsy
!pip install -U statsmodels

# <codecell>

import statsmodels.formula.api as sm
import pandas as pd

df = pd.read_csv("http://data.princeton.edu/wws509/datasets/salary.dat", sep='\s+')

model = sm.ols(formula="sl ~ yr", data=df).fit()
model.summary()

# <codecell>

def summary_df(res):
    reg_sum = res.summary()
    a = reg_sum.tables[1]
    af = [[b.strip() for b in row.split(',')] for row in ('feature'+a.as_csv()).split('\n')]
    
    for wq in af:
        if size(wq)>6:
            print wq
    rf = DataFrame(af[1:], columns=af[0])
    rf = rf.rename(columns={'P>|t|':'tp', 'std err':'std_err'})
    rf.coef = rf.coef.astype(float)
    rf.t = rf.t.astype(float)
    rf.std_err = rf.std_err.astype(float)
    rf.tp = rf.tp.astype(float)
    rf['abs_t'] = rf.t.abs()
    return rf

summary_df(model)

# <codecell>

model = sm.ols(formula="sl ~ sx + yr + rk", data=df).fit()
model.summary()

# <codecell>

from patsy import dmatrices

y, X = dmatrices('sl ~ sx + yr + rk', data=df, return_type='dataframe')

# <codecell>

from sklearn.linear_model import LinearRegression

model = LinearRegression()
model = model.fit(X,y)
model.score(X,y)

# <codecell>

from sklearn.metrics import mean_absolute_error

mean_absolute_error(model.predict(X), y)

# <codecell>

from sklearn import linear_model

model = linear_model.Ridge(alpha = .5)
model.fit(X,y)

print model.coef_

# <codecell>

from sklearn import linear_model

model = linear_model.RidgeCV(alphas=[0.1, 1.0, 10.0])
model.fit(X,y)

print model.coef_

# <codecell>

from sklearn.cross_validation import train_test_split

train, test = train_test_split(df, test_size=0.25)

# <codecell>


