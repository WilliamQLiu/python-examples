import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression, RidgeClassifierCV
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.cross_validation import cross_val_score
from sklearn.preprocessing import Imputer
from sklearn import preprocessing
from sklearn.base import BaseEstimator
import random


class Bagging(BaseEstimator):

    def __init__(self, models, bag_size):
        assert bag_size > 0.0 and bag_size < 1.0
        self.models = models
        self.bag_size = bag_size

    def fit(self, X, y):
        N = X.shape[0]
        for model in self.models:
            bag_indices = np.random.randint(0, N, int(N*self.bag_size))
            model.fit(X[bag_indices], y[bag_indices])
        return self

    def predict_proba(self, X):
        return np.mean([m.predict_proba(X) for m in self.models], axis=0)


class CreditScoreFeaturizer():
    def __init__(self):
      pass

    def fit_transform(self, dataset):
        """
          Transform a datframe <dataset> into a feature matrix

          params:
          dataset : Pandas DataFrame, the input dataset

          Returns a matrix N samples x M features
        """

        ###First step, select some fields we care about, all of these are numeric, so we can just pick them out
        data = np.array(dataset[[ 'age', 'MonthlyIncome']])

        # ## You want to perform some more interesting transformations of the data
        # ## For example, ratios
        # dataset['dollar_per_year'] = dataset['MonthlyIncome'] / dataset['age']

        ## One preprocesing step we will need to perform is imputation, fill in missing values
        imputer = Imputer(missing_values='NaN', strategy='mean', axis=0)
        data = imputer.fit_transform(data)

        #return np.hstack([data])

        ## Scaling features may be important you have very large outliers or need more intepretable coefficients
        # scaler = preprocessing.StandardScaler()
        # scaled_income = scaler.fit_transform(data[:,1])

        # data =  np.column_stack([data, scaled_income])

        # ## Turning features into discrete features is important if you are using linear classifier, but the underlying
        # ## data does not have a linear relationship

        ## NOTE: the binarizer, turns everything > 0 to 1 and and everything less than 0 to 0, so use the StandardScaler first
        # binarizer = preprocessing.Binarizer()
        # binned_income = binarizer.fit_transform(scaled_income)

        # data =  np.column_stack( [data,binned_income ] )

        return data


def create_submission(model, X_test, test_df):
    predictions = pd.Series(x[1] for x in model.predict_proba(X_test))

    submission = pd.DataFrame({'Id': test_df['Unnamed: 0'], 'Probability': predictions})
    submission.sort_index(axis=1, inplace=True)
    submission.to_csv('submission.csv', index=False)

def main():
    train_input = pd.read_csv('train.csv')
    test_input = pd.read_csv('test.csv')
    data = pd.concat([train_input, test_input])

    featurizer = CreditScoreFeaturizer()

    print "Transforming dataset into features..."
    # Create matrix of features from raw dataset
    X = featurizer.fit_transform(data)
    X_train = X[:len(train_input)]
    X_test = X[len(train_input):]

    # Use any model that we might find appropriate
    model = RidgeClassifierCV(alphas=[ 0.1, 1., 10. ])

    # Create the object and set relevant parameters
    #model = LogisticRegression(C=10)

    # Set target variable y
    y = train_input.SeriousDlqin2yrs

    print "Cross validating..."
    print np.mean(cross_val_score(model, X_train, y, scoring='roc_auc', cv=10))

    print "Training final model..."
    model = model.fit(X_train, y)


    n_models=5
    bag_size=0.70

    models = [LogisticRegression(C=10) for _ in xrange(n_models)]
    model = Bagging(models, bag_size)

    #Fit Final Model
    model.fit(X_train, y)

    print "Create predictions on submission set..."
    create_submission(model, X_test, test_input)

if __name__ == '__main__':
    main()