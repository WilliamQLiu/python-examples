from kmeans_exercise import k_means
from kmeans_exercise import _compute_labels_and_score

from sklearn.utils import check_random_state
from sklearn.metrics.pairwise import euclidean_distances

class KMeans():
    """K-Means clustering

    Parameters
    ----------

    n_clusters : int, optional, default: 8
        The number of clusters to form as well as the number of
        centroids to generate.

    max_iter : int
        Maximum number of iterations of the k-means algorithm for a
        single run.

    n_init : int, optional, default: 10
        Number of time the k-means algorithm will be run with different
        centroid seeds. The final results will be the best output of
        n_init consecutive runs in terms of score.

    random_state : integer or numpy.RandomState, optional
        The generator used to initialize the centers. If an integer is
        given, it fixes the seed. Defaults to the global numpy random
        number generator.

    Attributes
    ----------
    `cluster_centers_` : array, [n_clusters, n_features]
        Coordinates of cluster centers

    `labels_` :
        Labels of each point

    `score_` : float
        The value of the score criterion associated with the chosen
        partition.

   """

    def __init__(self, n_clusters=8, n_init=10, max_iter=10, verbose=0, random_state=None):

        self.n_clusters = n_clusters
        self.max_iter = max_iter
        self.n_init = n_init
        self.verbose = verbose
        self.random_state = random_state

    def _check_fit_data(self, X):
        """Verify that the number of samples given is larger than k"""
        if X.shape[0] < self.n_clusters:
            raise ValueError("n_samples=%d should be >= n_clusters=%d" % (
                X.shape[0], self.n_clusters))
        return X

    def _check_test_data(self, X):
        n_samples, n_features = X.shape
        expected_n_features = self.cluster_centers_.shape[1]
        if not n_features == expected_n_features:
            raise ValueError("Incorrect number of features. "
                             "Got %d features, expected %d" % (
                                 n_features, expected_n_features))

        return X

    def _check_fitted(self):
        if not hasattr(self, "cluster_centers_"):
            raise AttributeError("Model has not been trained yet.")

    def fit(self, X, y=None):
        """Compute k-means clustering.

        Parameters
        ----------
        X : array-like or sparse matrix, shape=(n_samples, n_features)
        """
        random_state = check_random_state(self.random_state)
        X = self._check_fit_data(X)

        # Sets 3 things, clusters' center, the labels, and the score

        self.cluster_centers_, self.labels_, self.score_ = k_means(
            X, n_clusters=self.n_clusters, n_init=self.n_init,
            max_iter=self.max_iter)
        return self

    def fit_predict(self, X):
        """Compute cluster centers and predict cluster index for each sample.

        Convenience method; equivalent to calling fit(X) followed by
        predict(X).
        """
        return self.fit(X).labels_

    def transform(self, X, y=None):
        """Transform X to a cluster-distance space

        In the new space, each dimension is the distance to the cluster
        centers.  Note that even if X is sparse, the array returned by
        `transform` will typically be dense.

        Parameters
        ----------
        X : {array-like, sparse matrix}, shape = [n_samples, n_features]
            New data to transform.

        Returns
        -------
        X_new : array, shape [n_samples, k]
            X transformed in the new space.
        """
        self._check_fitted()
        X = self._check_test_data(X)
        return euclidean_distances(X, self.cluster_centers_)

    def predict(self, X):
        """Predict the closest cluster each sample in X belongs to.

        Parameters
        ----------
        X : {array-like, sparse matrix}, shape = [n_samples, n_features]
            New data to predict.

        Returns
        -------
        labels : array, shape [n_samples,]
            Index of the cluster each sample belongs to.
        """
        self._check_fitted()
        X = self._check_test_data(X)
        return _compute_labels_and_score(X, self.cluster_centers_)[0]

    def score(self, X):
        """Opposite of the value of X on the K-means objective.

        Parameters
        ----------
        X : {array-like, sparse matrix}, shape = [n_samples, n_features]
            New data.

        Returns
        -------
        score : float
            Opposite of the value of X on the K-means objective.
        """
        self._check_fitted()
        X = self._check_test_data(X)
        return -_compute_labels_and_score(X, self.cluster_centers_)[1]