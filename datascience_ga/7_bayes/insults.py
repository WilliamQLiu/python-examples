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
import csv
import unidecode as uni

np.set_printoptions(threshold='nan')
np.set_printoptions(threshold=np.nan)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_columns', 0) # Display any number of columns
pd.set_option('display.max_rows', 0) # Display any number of rows

#df = pd.read_csv(
#    '/Users/williamliu/Dropbox/NYC-DAT-08/Homework_7/input/test-utf8.csv',
#    header=None, index_col=False, encoding='utf-8')
#df = pd.read_csv('/Users/williamliu/Dropbox/NYC-DAT-08/Homework_7/input/nyt_categories.csv')

df = pd.read_csv(
    '/Users/williamliu/Dropbox/NYC-DAT-08/Homework_7/william_liu/output/mytest-utf8.csv',
    header=None, index_col=False, dtype={0:object})

df.rename(columns={0:'Text'}, inplace=True)

#df_bad_words = pd.read_csv(
#    '/Users/williamliu/Dropbox/NYC-DAT-08/Homework_7/william_liu/output/badwords.csv',
#    header=0, index_col=False)

badwords = ([
    "4r5e",
    "5h1t",
    "5hit",
    "a55",
    "anal",
    "anus",
    "ar5e",
    "arrse",
    "arse",
    "ass",
    "ass-fucker",
    "asses",
    "assfucker",
    "assfukka",
    "asshole",
    "assholes",
    "asswhole",
    "a_s_s",
    "b!tch",
])

if __name__ == "__main__":

    # Unidecode to remove ascii errors
    df.Text = [uni.unidecode(line) for line in df.Text]
    #print type(df.Text) # <class pandas.core.series.Series>
    #print df.Text

    vectorizer = CountVectorizer(ngram_range=(1,1))
    #X = vectorizer.fit_transform(df['Text'].values)
    X = vectorizer.fit_transform(badwords).toarray()
    print X
    print type(X) # <class 'scipy.sparse.csc.csc_matrix'>
    print vectorizer
    print "Vectorizer is \n", X
    print "Vectorizer Feature Names are ", vectorizer.get_feature_names()
    print "Vectorizer Vocab is ", vectorizer.vocabulary_

    analyze = vectorizer.build_analyzer()
    #vectorizer.vocabulary_.get('fuck')
    #vectorizer.TfidfTransformer
    X_2 = vectorizer.fit_transform(badwords).toarray()

    #vectorizer = TfidfTransformer() # n_estimators means we're going to use n different trees

    #clf = MultinomialNB() # classifier for Naive Bayes multinomial models
    #clf.fit(X, y)

    #mydf = clf.predict(X)
    #print mydf

    # sklearn can take a lot of different models at once and will go through each model object
    #text_clf = Pipeline([('vect', CountVectorizer(encoding=u'utf-8')), # Convert text to matrix of token counts
    #                     ('tfidf', TfidfTransformer()), # Transform a count matrix to a Term-frequency and Inverse-Document-Frequency
    #                     ('clf', MultinomialNB()), # Classification with discrete features
    #                     ])

    #train, test = cross_validation.train_test_split(df, test_size=.5, train_size=.5)
    #test_df = pd.DataFrame(test, columns=['Text'])

    #print type(train)

    # Sometimes doesn't work for dataframes, so using numpy arrays
    #categories, articles  = map(np.array, zip(*train))
    #categories_test, articles_test  = map(np.array, zip(*test))

    #data = map(np.array, zip(*train))
    #data_test = map(np.array, zip(*test))

    #print data_test.head()

    #model = text_clf.fit(data)
    #test_df['a'] = model.predict(data_test)
