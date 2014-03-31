"""
    K-means clustering implementation exercise

    GADS 8: Lesson 12

    KMeans code from sklearn/clustering/k_means_.py

"""

import numpy as np
from sklearn.utils.fixes import bincount
from sklearn.utils import check_random_state

""" Takes two vectors v1, v2 and tells us the distance between them
    Basic impl: Euclidean Distance =
          sum of squared distances =
          SQRT ( SUM_over_i ( (v1[i] - v2[i]) ^ 2 ) )
"""

def distance_function(v1, v2):
    #pass
    # Write a function to compute the euclidean distance between two vectors, v1 and v2
    #distance = 0
    #for x, y in zip(v1, v2):
    #    distance += (v1[i] - v2[i])**2
    #return np.sqrt(distance)

    # More efficient
    return np.sqrt ( np.sum( ( v1-v2) ** 2 ) )


def k_means(X, n_clusters,
            n_init=10, max_iter=10):
    """K-means clustering algorithm.

    Parameters
    ----------
    X : array-like or sparse matrix, shape (n_samples, n_features)
        The observations to cluster.

    n_clusters : int
        The number of clusters to form as well as the number of
        centroids to generate.

    max_iter : int, optional, default 300
        Maximum number of iterations of the k-means algorithm to run.

    n_init : int, optional, default: 10
        Number of time the k-means algorithm will be run with different
        centroid seeds. The final results will be the best output of
        n_init consecutive runs in terms of score.

    Returns
    -------
    centroid : float ndarray with shape (k, n_features)
        Centroids found at the last iteration of k-means.

    label : integer ndarray with shape (n_samples,)
        label[i] is the code or index of the centroid the
        i'th observation is closest to.

    score : float
        The final value of the score criterion (sum of squared distances to
        the closest centroid for all observations in the training set).

    """
    best_labels, best_score, best_centers = None, np.infty, None

    # We are going to `n_init` random starts and return the best one
    for it in range(n_init):
        # run a k-means once
        labels, score, centers = _kmeans_single(X, n_clusters, max_iter=max_iter)
        # determine if these results are the best so far
        #TODO: IMPLEMENT
        if score < best_score:
            best_centers = centers
            best_labels = labels
            best_score = score

    return best_centers, best_labels, best_score

def _kmeans_single(X, n_clusters, max_iter=10):
    """A single run of k-means, assumes preparation completed prior.

    Parameters
    ----------
    X: array-like of floats, shape (n_samples, n_features)
        The observations to cluster.

    n_clusters: int
        The number of clusters to form as well as the number of
        centroids to generate.

    max_iter: int, optional, default 10
        Maximum number of iterations of the k-means algorithm to run.

    Returns
    -------
    centroid: float ndarray with shape (k, n_features)
        Centroids found at the last iteration of k-means.

    label: integer ndarray with shape (n_samples,)
        label[i] is the code or index of the centroid the
        i'th observation is closest to.

    score: float
        The final value of the score criterion (sum of squared distances to
        the closest centroid for all observations in the training set).
    """
    best_labels, best_score, best_centers = None, np.infty, None
    # init
    centers = _init_random_centroids(X, n_clusters)

    for i in range(max_iter):
        # Figure out the labels, given the centers
        labels, score = _compute_labels_and_score(X, centers)

        # Recompute the centers given the labels and data
        centers = _recompute_centers(X, labels, n_clusters)

        # Save the best run
        #TODO: IMPLEMENT
        # Is this run better than the last run?
            # If so, update best_centers, best_labels, best_score

        if score < best_score:
            best_centers = centers
            best_labels = labels
            best_score = score


    return best_labels, best_score, best_centers

def _compute_labels_and_score(X, centers):
    """

    Compute the labels and the current score of the given samples and centers

    Parameters
    ----------
    X: float64 array-like or CSR sparse matrix, shape (n_samples, n_features)
        The input samples to assign to the labels.

    centers: float64 array, shape (k, n_features)
        The cluster centers.

    Returns
    -------
    labels: int array of shape(n)
        The resulting assignment

    score: float
        The value of the score criterion with the assignment
        The score (sum of squared distances to the centers).
    """
    n_clusters = centers.shape[0]
    n_samples = X.shape[0]
    score = 0.0

    # set the default value of centers to -1 to be able to detect errors
    labels = -np.ones(n_samples, np.int32) # Make entire array labels -1
    score = 0.0
    #TODO: IMPLEMENT - Completed below
        # Iterate over the samples and the clusters
        # Compute the distance between samples and cluster center
        # Save the closest cluster center
        # SCORE is the SUM of distances from point to closest center
        # So once we've found the closest center, add the distance to closest center to score

    for a in xrange(n_samples):
        closest_center = None
        min_dist = np.infty # or large number like 999999999
        for b in xrange(n_clusters):
            sample = X[a]
            center = centers[b]
            d = distance_function(sample, center)
            if d < min_dist: # If this is the highest 'min'
                min_dist = d
                closest_center = b
        labels[a] = closest_center
        score += min_dist

    return labels, score


def _recompute_centers( X, labels, n_clusters):
    """
    Computation of cluster centers / means.

    Parameters
    ----------
    X: array-like, shape (n_samples, n_features)

    labels: array of integers, shape (n_samples)
        Current label assignment

    n_clusters: int
        Number of desired clusters

    Returns
    -------
    centers: array, shape (n_clusters, n_features)
        The resulting centers
    """

    n_samples = X.shape[0]
    n_features = X.shape[1]
   
    # Initialize centers to all zero
    centers = np.zeros((n_clusters, n_features))
    n_samples_in_cluster = bincount(labels, minlength=n_clusters)

    for i in xrange(n_samples):
        label = labels[i]
        centers[label] += X[i]

    # Compute a center for each label
    # For each label, average over samples and features
    #TODO: IMPLEMENT
        # For each sample
            # What label is it? Let's say its label is 'label'
            # Add feature X's feature i to centers[label] feature value i

    # Normalize by the size of the cluster
    centers /= n_samples_in_cluster[:, np.newaxis]

    return centers

def _init_random_centroids(X, k, random_state=None):
    """Compute the initial centroids

    Parameters
    ----------

    X: array, shape (n_samples, n_features)

    k: int
        number of centroids

    random_state: integer or numpy.RandomState, optional
        The generator used to initialize the centers. If an integer is
        given, it fixes the seed. Defaults to the global numpy random
        number generator.

    Returns
    -------
    centers: array, shape(k, n_features)
    """
    random_state = check_random_state(random_state)
    n_samples = X.shape[0]

    seeds = random_state.permutation(n_samples)[:k]
    centers = X[seeds]

    return centers
