# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>


import pandas as pd
import os
import matplotlib as plt
import numpy as np



pd.set_option('display.max_columns', 1000)
pd.set_option('display.max_rows', 3000)
pd.set_option('display.width', 100000)





df = pd.read_csv('../input/2013_NCAA_Game.csv')

pd.scatter_matrix(df)


pd.scatter_matrix(df, diagonal='kde')


hist(df['Team Avg Scoring Margin'])


plt.scatter(df['Team Score'], df['Team Margin'])



pf = pd.read_csv('../input/clean_player_data.csv')
pf = pf.drop_duplicates()


tt = pf.groupby('Team').mean()



