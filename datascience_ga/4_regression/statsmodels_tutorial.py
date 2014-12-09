import numpy as np
import pandas as pd
import statsmodels.formula.api as smf

# Load data
url = 'http://vincentarelbundock.github.io/Rdatasets/csv/HistData/Guerry.csv'
dat = pd.read_csv(url)

# Url data looks like
# "","dept","Region","Department","Crime_pers","Crime_prop","Literacy",
# "Donations","Infants","Suicides","MainCity","Wealth","Commerce","Clergy",
# "Crime_parents","Infanticide","Donation_clergy","Lottery","Desertion",
# "Instruction","Prostitutes","Distance","Area","Pop1831"

# Fit regression model (using the natural log of one of the regressors)
results = smf.ols('Lottery ~ Literacy + np.log(Pop1831)', data=dat).fit()

# Inspect the results
print results.summary()