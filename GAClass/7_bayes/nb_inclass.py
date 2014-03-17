import numpy as np
import math
import pandas as pd

class NaiveBayes():


  def __init__(self):

    """ Setup useful datastructures
        Feel free to change this
    """

    self._word_counts = {}  ## Table indexed on word + class, holds count(word + class)
    self._class_counts = {} ## Array of counts per class [ 143, 234 ]
    self._priors = {}


  def fit(self, X, Y):
    """Fit a Multinomial NaiveBayes model from the training set (X, y).

        Parameters
        ----------
        X : array-like of shape = [n_samples]
            The training input samples.

        Y : array-like, shape = [n_samples]

        Returns
        -------
        self : object
            Returns self.
    """
    for (x, y) in zip(X, Y):
      self._fit_instance(x, y)

    self._fit_priors()

  def _fit_priors(self):
    """Set priors based on data"""
    ##TODO##

  def _fit_instance(self, instance, y):
    """Train based on single samples       

     Parameters
        ----------
        instance : string = a line of text or single document
                   instance =  "This is not an insult"
                   instanec = "You are a big moron"
        y : int = class of instance
                = 0 , 1 , class1, class2

    """
    ## Update counts on y
    ##Increment count by 1, or set count to 1 if never seen before
    self._class_counts[y] = self._class_counts.get(y, 0) + 1

    for word in instance.split():
        ## Update counts on word + y
        ## Use pair (word, y) as key and increment counts
        #self._word_counts[(word, y)] = self._word_counts.get((word, y), 0) + 1


      try:
        self._word_counts[word]
      except:
        self._word_counts[word] = {}

      self._word_counts[word][y] = self._word_counts[word].get(y, 0) + 1.0
      



  def predict(self, X):
    """ Return array of class predictions for samples
      Parameters
      ----------
        X : array-like of shape = [n_samples]
            The test input samples.

        Returns
        -------
          : array[int] = class per sample
    """

    return [self._predict_instance(x) for x in X]


  def predict_proba(self, X):
    """ Return array of class predictions for samples
      Parameters
      ----------
        X : array-like of shape = [n_samples]
            The test input samples.

        Returns
        -------
          : array[array[ float, float ... ], ...] =  class probabilities per sample 
    """

    return [ self._predict_instance(instance) for instance in X ]

  def _predict_instance(self, instance):
    """ Return array of class predictions for samples
      Parameters
      ----------
        instance : string = a line of text or single document

        Returns
        -------
          : array[ float, float ... ] =  class probabilities 
    """
    return [ self._compute_class_probability(instance, c) for c in self._class_counts.keys()]
    #return  [ x / sum(p) for x in p]
  def _prior_prob(self, c):
    return self._priors[c]

  def _compute_class_probability(self, instance, c):
    """ Compute probability of instance under class c
        Parameters
        ----------
        instance : string = a line of text or single document

        Returns
        -------
          p : float =  class probability

      HINT : Often times, multiplying many small probabilities leads to underflow, a common numerical tricl
      is to compute the log probability.

      Remember, the log(p1 * p2 * p3) = log p1 + log p2 + log p3
    """

    ## P( instance | c) = P(w1 | c ) * .. * P(wN | c) * P(c)
    p_instance_c = 0 
    for word in instance.split():
      #Compute P(word | c)

      ##What happens when we haven't seen word in c?

      ##Ignore it
      if word in self._word_counts.keys() and c in self._word_counts[word].keys(): 
       p_word_c = math.log(float(self._word_counts[word][c]) / self._class_counts[c])
       p_instance_c += p_word_c # add when logging instead of multiplying

      ##Smoothing (another form of regularization)
      #try:
      #  p_word_c = (float(self._word_counts[word].get(c, 0) + 5.0 / (self._class_counts[c] + 5.0)
      #except KeyError:
      #  p_word_c = 1.0/ 100000 #lambda smoothing (plus-one, or plus lambda)
        #p_word_c =  #lambda smoothing (plus-one, or plus lambda)
      #p_instance_c *= p_word_c
    return p_instance_c + math.log(float(self._class_counts[c]) / sum(self._class_counts.values()))

if __name__ == '__main__':
  data = pd.read_csv('/Users/williamliu/Dropbox/NYC-DAT-08/Homework_7/input/train-utf8.csv')
  model = NaiveBayes()
  model.fit(data.Comment, data.Insult)

  phrases = ["This is not an insult", "You are a big moron moron moron", "I went to the store", 'idiot moron']
  probabilities = np.exp(model.predict_proba(phrases))
  for phrase, probability in zip(phrases, probabilities):
    print "Phrase: {0}\nCategory: {1}\n\n".format(phrase, 'Insult' if probability[1] > probability[0] else 'Not Insult')

