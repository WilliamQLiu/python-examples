""" sklearn > feature_extraction > text > CountVectorizer 
    Convert a collection of text documents to a matrix of token counts

    Parameters
    analyzer : whether the feature should be made of word or character n-grams
    ngram_range
    stop_words : words removed from tokens (e.g. the, is, at , which)
    max_df, min_df : ignore terms that have a term frequency higher/lower than
    the given threshold (i.e. float in range[0.0, 1.0])
    vocabulary : either a mapping (e.g. a dict) where keys are terms and values
    are indicies in the feature matrix

    Attributes
      vocabulary_ : a dict with a mapping of terms to feature indicies
      stop_words_ : a set of terms that were ignored because they occurred in
                    either too many (max_df) or too few (min_df) docs
"""
from sklearn.feature_extraction.text import CountVectorizer

# Vectorize and Tokenize the text
vectorizer = CountVectorizer()
print vectorizer
corpus = ['Bursting the Big Data bubble starts with appreciating certain nuances about its products and patterns","the real solutions that are useful in dealing with Big Data will be needed and in demand even if the notion of Big Data falls from the height of its hype into the trough of disappointment']
print type(corpus)
X = vectorizer.fit_transform(corpus)
print "Vectorizer is ", vectorizer
print type(vectorizer)

print "Vectorizer Feature Names are ", vectorizer.get_feature_names()

#l = vectorizer.get_feature_names()

#for line in l:
#    print line

