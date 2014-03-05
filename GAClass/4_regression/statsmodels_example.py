
import statsmodels.formula.api as sm
import pandas as pd

data = pd.read_csv("http://data.princeton.edu/wws509/datasets/salary.dat", sep='\s+')
# sx, rk, yr, dg, yrd, sl
# male, full, 25, doctorate, 35, 36350

model = sm.ols(formula="sl ~ yr", data=data).fit()
print model.summary()

model = sm.ols(formula="sl ~sx + yr +rk", data=data).fit()
#print model.summary()

