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
