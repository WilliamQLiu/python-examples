import math
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.preprocessing import LabelEncoder
from sklearn.cross_validation import train_test_split
from sklearn.svm import LinearSVC
from matplotlib import pyplot as plt


def simple_wrong_approach():
    """ Simpliest way to test the performance of a classifier, but wrong
        because it overfits by training on the same dataset we test on """

    ### Get dataset
    iris = load_iris()
    X = iris.data
    y = iris.target

    ### Instantiate and Train the classifier
    clf = LinearSVC(loss='l2')
    clf.fit(X, y)

    ### Check input vs. output labels
    y_pred = clf.predict(X)
    print (y_pred == y)


def cross_validation():
    """ To avoid overfitting, we define two different datasets:
        * a training set X_train, y_train used to learn the parameters of a
        predictive model
        * a testing set X_test, y_test used to evaluate the fitted predictive
        model
    """

    ### Get dataset
    iris = load_iris()
    X = iris.data
    y = iris.target

    ### Instantiate and Train the classifier
    X_train, X_test, y_train, y_test = train_test_split(X, y,
            test_size=0.25, random_state=0)
    clf = LinearSVC(loss='l2').fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    print (y_pred == y_test)


def advanced_analysis():
    ### Get and Clean File
    df = pd.io.parsers.read_csv(
        filepath_or_buffer='https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data',
        header=None,
        sep=',',
        )
    df.dropna(how="all", inplace=True) # to drop the empty line at file-end

    ### Get Features into a dic
    feature_dict = {i:label for i,label in zip(
                    range(4),
                    ('sepal length in cm',
                    'sepal width in cm',
                    'petal length in cm',
                    'petal width in cm', ))}


    ### Convert class labels of flowers into 1,2,3 (numerical)
    X = df[[0,1,2,3]].values
    y = df[4].values

    enc = LabelEncoder()
    label_encoder = enc.fit(y)
    y = label_encoder.transform(y) + 1

    label_dict = {1: 'Setosa', 2: 'Versicolor', 3:'Virginica'}


    ### Plot exploratory data analysis
    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12,6))

    for ax,cnt in zip(axes.ravel(), range(4)):

        # set bin sizes
        min_b = math.floor(np.min(X[:,cnt]))
        max_b = math.ceil(np.max(X[:,cnt]))
        bins = np.linspace(min_b, max_b, 25)

        # plottling the histograms
        for lab,col in zip(range(1,4), ('blue', 'red', 'green')):
            ax.hist(X[y==lab, cnt],
                       color=col,
                       label='class %s' %label_dict[lab],
                       bins=bins,
                       alpha=0.5,)
        ylims = ax.get_ylim()

        # plot annotation
        leg = ax.legend(loc='upper right', fancybox=True, fontsize=8)
        leg.get_frame().set_alpha(0.5)
        ax.set_ylim([0, max(ylims)+2])
        ax.set_xlabel(feature_dict[cnt])
        ax.set_title('Iris histogram #%s' %str(cnt+1))

        # hide axis ticks
        ax.tick_params(axis="both", which="both", bottom="off", top="off",
                labelbottom="on", left="off", right="off", labelleft="on")

        # remove axis spines
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["bottom"].set_visible(False)
        ax.spines["left"].set_visible(False)

    axes[0][0].set_ylabel('count')
    axes[1][0].set_ylabel('count')

    fig.tight_layout()
    plt.show()


if __name__ == '__main__':
    simple_wrong_approach()
    cross_validation()
    advanced_analysis()
