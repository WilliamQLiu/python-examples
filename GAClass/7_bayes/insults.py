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

corpus = [{
    "4r5e":1,
    "5h1t":1,
    "5hit":1,
    "a55":1,
    "anal":1,
    "anus":1,
    "ar5e":1,
    "arrse":1,
    "arse":1,
    "ass":1,
    "ass-fucker":1,
    "asses":1,
    "assfucker":1,
    "assfukka":1,
    "asshole":1,
    "assholes":1,
    "asswhole":1,
    "a_s_s":1,
    "b!tch":1,
}]


if __name__ == "__main__":

    # Unidecode to remove ascii errors
    [uni.unidecode(m) for m in df.Text]

    print df.columns
    print df.head()

    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(df)
    print "Vectorizer is ", X
    print "Vectorizer Feature Names are ", vectorizer.get_feature_names()


    #print "Vectorizer Vocab is ", vectorizer.vocabulary_

    #print "Vectorizer Feature Names are ", vectorizer.get_feature_names()

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
