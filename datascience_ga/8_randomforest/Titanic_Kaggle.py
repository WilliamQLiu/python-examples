# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_columns', 0) # Display any number of columns
pd.set_option('display.max_rows', 0) # Display any number of rows

# <codecell>

# Get Kaggle Titanic Datasets
t_train = pd.read_csv('/Users/williamliu/Dropbox/NYC-DAT-08/Homework_8/input/titanic_train.csv')
t_test = pd.read_csv('/Users/williamliu/Dropbox/NYC-DAT-08/Homework_8/input/titanic_test.csv')

# <codecell>

print t_train.head()

# <codecell>

t_train['BoolSex'] = [ 1 if field=='male' else 0 for field in t_train.Sex]
t_test['BoolSex'] = [ 1 if field=='male' else 0 for field in t_test.Sex]

# <codecell>

t_train.describe()

# <codecell>

# Data Cleaning
#t_train = t_train.dropna()
#t_test = t_test.dropna()
#t_train = t_train.dropna()
#t_train = t_train.dropna(subset=['Age'], how='any')
#t_test = t_test.dropna(subset=['Age'], how='any')
t_train['Age'].fillna(30, inplace=True) # Fill blanks with mean Age
t_train['Fare'].fillna(32, inplace=True) # Fill blanks with mean Fare
#t_test.describe()
t_test['Fare'].fillna(35, inplace=True) # Fill blanks with mean Fare
t_test['Age'].fillna(30, inplace=True) # Fill blanks with mean Age

# <codecell>

#t_train.Embarked.unique() # Plot Embarked and Fare, see coor
#t_train.c_emb = [1 if a.contains('c') else 0 for a in t_train.Embarked]

# <codecell>

#def clean_embark(x):
#    if x.contains('C'):
#        return 2844
#    return 0


#t_train['Embarked'].replace('C', 1, inplace=True)
#t_train['Embarked'].replace('S', 2, inplace=True)
#t_train['Embarked'].replace('Q', 3, inplace=True)

#t_test['Embarked'].replace('C', 1, inplace=True)
#t_test['Embarked'].replace('S', 2, inplace=True)
#t_test['Embarked'].replace('Q', 3, inplace=True)

# <codecell>

#t_train['NumCabin'] = []
#test = t_train.groupby('Cabin')
#print test.head()

# <codecell>

print t_train.head()

# <codecell>

#features = ['Fare', 'Age', 'Parch', 'Pclass']
features = ['Fare', 'Age', 'Parch', 'Pclass', 'BoolSex']
t_train[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']]

# <codecell>

t_test = t_test[features]
print t_test

# <codecell>

#from sklearn.feature_extraction.text import CountVectorizer

#Creates a column for every possible word, length 2 sequence of words and length 3 sequence of words
#vectorizer = CountVectorizer(ngram_range=(1,3)) # Set ngram_range means take all possibilities of 1, 2, or 3 words
#X_train = vectorizer.fit_transform(t_train.Sex)

# <codecell>

#vectorizer = TfidfVectorizer(stop_words='english', lowercase=True, ngram_range=(1,5)) # Can try different ngrams (lower = faster)
#X_train = vectorizer.fit_transform(t_train.Sex)

# <codecell>

from sklearn.cross_validation import cross_val_score
from sklearn.tree import DecisionTreeClassifier
# Going to import the Decision Tree to compare with RandomForest

vectorizer = TfidfVectorizer(stop_words='english', lowercase=True, ngram_range=(1,5), min_df=1) # n_estimators means we're going to use n different trees
X_train = vectorizer.fit_transform(t_train[features])

tree_model = DecisionTreeClassifier() # Use Decision Tree first, then switch to Random Forest for more accuracy later
print cross_val_score(tree_model, np.asarray(t_train[features]), t_train.Survived) # toarray takes type and returns as array
# You'll see that the Decision Tree isn't quite as accurate as the Random Forest

# <codecell>


from sklearn.ensemble import RandomForestClassifier

rf_model = RandomForestClassifier(n_estimators=100, compute_importances=True)
rf_model.fit(np.asarray(t_train[features]), t_train.Survived)
print cross_val_score(tree_model, np.asarray(t_train[features]), t_train.Survived) # toarray takes type and returns as array

print sorted(zip(rf_model.feature_importances_, features), reverse=True)[:10] # Random Forest

# <codecell>

print features
rf_model = RandomForestClassifier(n_estimators=100, compute_importances=True)
print rf_model.fit(np.asarray(t_train[features]), t_train)

# <codecell>

rf_model = RandomForestClassifier(n_estimators=10, compute_importances=True)
rf_model.fit(np.asarray(t_train[features]), t_train.Survived)
mydf = rf_model.predict(t_test)

# <codecell>

print mydf

# <codecell>

for line in mydf:
    print line

# <codecell>


