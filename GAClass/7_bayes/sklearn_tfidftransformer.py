""" sklearn > feature_extraction > text > TfidfTransformer 
    Transform a count matrix to a normalized tf or tf-idf representation
      Tf means term-frequency (i.e. raw frequencies of occurrence)
      Tf-idf means term-frequency times inverse document-frequency
      Tf-idf's goal is to scale down impact of frequently appearing tokens


    Parameters
      norm : l1, l2, or None.  Norm used to normalize term vectors
      use_idf : boolean.  Enable inverse-document-frequency reweighting
      smooth_idf : boolean.  Smooth idf weights and prevents zero divisions
      sublienar_tf : boolean.  Apply sublinear tf scaling (i.e. replace tf
        with 1 + log(tf))

    Methods
      fit(X[,y]) : Learn the idf vector (global term weights)
      fit_transform(X[,y]) : Fit to data, then Transform
      get_params([deep]) : Get parameters for this estimator
      set_params(**params) : Set parameters of this estimator
      transform(X[,copy]) : Transform count matrix to tf or tf-df representation
      
"""

