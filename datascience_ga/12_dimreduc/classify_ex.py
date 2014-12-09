import sys
from sklearn.cross_validation import cross_val_score
from sklearn.decomposition import RandomizedPCA
import numpy as np
from PIL import Image
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

import os, sys
import random

#setup a standard image size; this will distort some images but will get everything into the same shape
STANDARD_SIZE = (300, 167)
def img_to_matrix(filename, verbose=False):
    """
    takes a filename and turns it into a numpy array of RGB pixels
    """
    img = Image.open(filename)
    if verbose==True:
        print "changing size from %s to %s" % (str(img.size), str(STANDARD_SIZE))
    img = img.resize(STANDARD_SIZE)
    img = list(img.getdata())
    img = map(list, img)
    img = np.array(img)
    return img

def flatten_image(img):
    """
    takes in an (m, n) numpy array and flattens it
    into an array of shape (1, m * n)
    """
    s = img.shape[0] * img.shape[1]
    img_wide = img.reshape(1, s)
    return img_wide[0]

if __name__ == '__main__':

    img_dir = "images/"
    images = [img_dir+ f for f in os.listdir(img_dir)]
    random.shuffle(images)
    ### Right now this says the targe is true if the file has 'kittens' in the name.
    ### This means we are building a binary classifier of kitten or not.  Change this is so you can pass an argument
    ### to build a classifier for any set of images.  Use sys.argv ('import sys' first)
    print "Enter your comparisions separated by spaces: ", sys.argv
    for i in range(1,len(sys.argv),1):
        print("Argument", i," is ", sys.argv[i])

    #Original
    #labels = np.array([1 if "kittens" in f.split('/')[-1] else 0 for f in images])
    for index in range(1, len(sys.argv)):
        labels = np.array([1 if sys.argv[i] in f.split('/')[-1] else 0 for f in images])

    data = []

    ### Apply transformation for each matrix
    for image in images:
      img = img_to_matrix(image)
      img = flatten_image(img)
      data.append(img)

    data = np.array(data)


    ### This creates a simpler representation of the images other than the raw pixels
    ### Change the number of components to see how this effects classification accuracy
    pca = RandomizedPCA(n_components=5)
    # Try to change number of features
    #pca = RandomizedPCA(n_components=10)

    ### Transform your dataset `data` into a feature setX
    X = pca.fit_transform(data)

    ### Setup a classifier (or multiple, play around with different models)
    ### How much data do you have?  Do you think the relationships are linear?
    model = LogisticRegression()
    #model = RandomForestClassifier(n_estimators=10)

    # Another model to try is:
    #model = RandomForestClassifier(n_estimators=10)

    ### Do some cross validation
    print cross_val_score(model, X, labels, scoring='roc_auc')
    # Logistic Regression # [ 0.73157895  0.62573099  0.60233918]
    # Random Forest Classifier # [ 0.6         0.48538012  0.66959064]




