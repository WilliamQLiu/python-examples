""" Try to minimize Error Rate [False Positives + False Negatives] / All Samples
"""
# pip install UniDecode

from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn import cross_validation
import sklearn.metrics as m
import pandas as pd
import numpy as np

np.set_printoptions(threshold='nan')
np.set_printoptions(threshold=np.nan)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_columns', 0) # Display any number of columns
pd.set_option('display.max_rows', 0) # Display any number of rows

#df = pd.read_csv(
#    '/Users/williamliu/Dropbox/NYC-DAT-08/Homework_7/input/test-utf8.csv',
#    header=None, index_col=False)
df = pd.read_csv('/Users/williamliu/Dropbox/NYC-DAT-08/Homework_7/input/nyt_categories.csv')

df.rename(columns={0:'Text'}, inplace=True)

if __name__ == "__main__":
    print "DF head ", df.head()
    print "DF columns ", df.columns

    # sklearn can take a lot of different models at once and will go through each model object
    text_clf = Pipeline([('vect', CountVectorizer()), # http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html
                     ('tfidf', TfidfTransformer()), # http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfTransformer.html
                     ('clf', MultinomialNB()), # http://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.MultinomialNB.html
                     ])

    train, test = cross_validation.train_test_split(df[['category','article']])
    test_df = pd.DataFrame(test, columns=['category', 'article'])

    print "Cross Validation - Train data is \n", train[:3] # numpy.ndarray
    # E.g. sports The proper thing to don nights like this is...
    #      arts Jim Farmer must have had some bizarre experiences ...
    #      business THE utter failings of our natoin's credit rating
    #      obituaries Leyla Gencer, an operatic soprano who was among

    print "Cross Validation - Test data is \n", test[:3] # numpy.ndarray

    # Sometimes doesn't work for dataframes, so using numpy arrays
    categories, articles  = map(np.array, zip(*train)) # Calls function np.array on zip(*train), which passes arguments
    categories_test, articles_test  = map(np.array, zip(*test)) # Calls function np.array on zip(*test)

    cv = cross_validation.StratifiedKFold(categories, 10, indices=False)
    # Returns type: <class 'sklearn.cross_validation.StratifiedKFold'>

    cross_validation.cross_val_score(text_clf, articles, y=categories, cv=cv, score_func=m.recall_score)
    # cross_validation is a module

    model = text_clf.fit(articles, categories)
    # Type <class 'sklearn.pipeline.Pipeline'>

    test_df['pred_category'] = model.predict(categories_test)

    #print "Categories Sample", categories

    #print "Articles Sample", articles

    print test_df.head(20)



    """
    # sklearn can take a lot of different models at once and will go through each model object
    text_clf = Pipeline([('vect', CountVectorizer()), # Convert text to matrix of token counts
                         ('tfidf', TfidfTransformer()), # Transform a count matrix to a Term-frequency and Inverse-Document-Frequency
                         ('clf', MultinomialNB()), # Classification with discrete features
                         ])

    train, test = cross_validation.train_test_split(df, test_size=.5, train_size=.5)
    test_df = pd.DataFrame(test, columns=['Text'])

    print test_df.head()

    # Sometimes doesn't work for dataframes, so using numpy arrays
    #categories, articles  = map(np.array, zip(*train))
    #categories_test, articles_test  = map(np.array, zip(*test))

    data = map(np.array, zip(*train))
    data_test = map(np.array, zip(*test))

    print data_test
    #cv = cross_validation.StratifiedKFold(categories, 10, indices=False)
    #cross_validation.cross_val_score(text_clf, articles, y=categories, cv=cv, score_func=m.recall_score)

    #cv = cross_validation.StratifiedKFold(data, indices=False) # Provides train/test indices to split data in train test sets

    model = text_clf.fit(data)
    test_df['a'] = model.predict(data_test)

    """