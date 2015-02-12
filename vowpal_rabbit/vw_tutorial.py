"""
    Intro to Vowpal Wabbit - Will's Notes
    Tutorial from https://github.com/JohnLangford/vowpal_wabbit/wiki/Tutorial

    Some Housing Data (house_dataset):
    0 | price:.23 sqft:.25 age:.05 2006
    1 2 'second_house | price:.18 sqft:.15 age:.35 1976
    0 1 0.5 'third_house | price:.53 sqft:.32 age:.87 1924

    Loading Housing Data:
    * First number in each line (0, 1) is a label (what we want to predict)
        0 means no roof-replacement
        1 means roof-replacement
        * Optional second number shows weight of label
            If this optional value is missing, assumes value of `1`
        * Optional third number (e.g. 0.5) is an initial prediction
            E.g. you want to predict an offset instead of an absolute value
        * Can also tag (e.g. 'second_house', 'third_house')
    * `|` bar separates label (want to predict) from features (what we know)
    * Each feature can have an optional `:<numeric_value> following it
        If this optional value is missing, assumes value of `1`
    * By default, hashes feature names into in-memory indexes

    Useful command line arguments:
    https://github.com/JohnLangford/vowpal_wabbit/wiki/Command-line-arguments

"""


if __name__ == '__main__':

    print "Use these commands in terminal, not through python"
    # $vw house_dataset
    """
    Num weight bits = 18
    learning rate = 0.5
    initial_t = 0
    power_t = 0.5
    using no cache
    Reading datafile = house_dataset
    num sources = 1
    average    since         example     example  current  current  current
    loss       last          counter      weight    label  predict features
    0.000000   0.000000            1         1.0   0.0000   0.0000        5
    0.666667   1.000000            2         3.0   1.0000   0.0000        5

    finished run
    number of examples per pass = 3
    passes used = 1
    weighted example sum = 4
    weighted label sum = 2
    average loss = 0.75
    best constant = 0.5
    best constant's loss = 0.25
    total feature number = 15
    """

    # What it means
    """
        'using no cache' means if you do multiple passes (--passes), you want
            to cache the data so it'll be much faster.  Default loc creates
            as house_dataset.cache or you can override.  Use -c to cache

        'Reading datafile = house_dataset' means we're using the csv file,
            can also use other sources like cache files, stdin, tcp socket

        'num sources = 1' means only one file, though we can specify multiple

        'Num weight bits = 18' means 18 bits of the hash function will be used
            Can adjust using `-b bits`
            Increase shit out of this on a super EC2 to be real accurate
            The more hashing space for more variables, avoids hash collision
            -b 28 for 8GB of RAM
            -b 29 for 12GB of RAM

        'learning rate = 0.5' is default learning rate; higher learning rate
            will converge faster, but a too high learning rate may overfit or
            end up with a worse on average.  Use -l for learning rate

        'initial_t = 1' specifies initial time, not really needed to adjust,
            learning rates should decay over time

        'power_t = 0.5' specifies the power on the learning rate decay.
            0 means learning rate does not decay - constantly learns against
                changing conditions, like when rules-of-the-game keep changing
            1  means very aggressive - the fundamental relation between input
                features and the target label are not changing over time
            Choose depending on what you're doing, usually .5 is good

        'average loss' computes the progressive validation loss

        'neural network' means --nn <num>, a network with <num> hidden units
            think of a neural network as a tool (e.g. check if bus in picture)
            by making a wheel, box, and size detector (if all goes off then
            it might be a bus), usually small like 10

        'quadratic and cubic features' means creating all possible combinations
            between original featuers so instead of d features, you have d^2
            in quadratic and d^3 for cubic mode
            -q nn where 'n' is a namespace
            --cubic nnn where 'n' is a namespace
            E.g. can do: -q aa -q ab
                 -q : to uses wildcard ':' to cross every name space with every other

        'n-gram' are contiguous sequences of n items from a given sequence,
            useful for modeling text beyond a bag of words (e.g. red wine)
            --ngram <num> where n is the number of grams

        'regularization' prevents overfitting using --l1 or --l2

        --passes means the number of passes to do (e.g. 25 passes with 3 rows
            of data means 75 rows)
        --holdout_off option means that by default, 10 percent of examples are
            withheld to avoid overfitting.  Can use all data with holdout_off
        --quiet means don't print out diagnostics
        -a means to audit (print weights of features)
        --nn <number> means the neural network with <number> hidden units

        Reading your model
            -f <arg> option writes the weight vector to a file
            --readable_model is like -f, except human readable format
            --invert_hash is like --readable_model, more readable (no hashes)


        Utilities/Tools:

        vw-hypersearch
        https://github.com/JohnLangford/vowpal_wabbit/wiki/Using-vw-hypersearch
        vw-hypersearch is a wrapper to 'vw' to help find lowest-loss hyper-
        paramters.  E.g. find lowest average loss for --l2 on a train-set with
            $vw-hypersearch 1e-10 1 vw --l2 <argmin> train.dat
                <argmin> is the lowest percent
                1e-10 is the lowest-bound of search range
                1 is the upper bound of search range

        vw-varinfo
        https://github.com/JohnLangford/vowpal_wabbit/wiki/using-vw-varinfo
        exposes all variables of a model in human readable form
        Shows input variable names, name-spaces, hash value, range (min, max),
        the model (regressor) weight, and relative distance of each variable
        from the best constant prediction
            $vw-varinfo data.train
                Can also pass arguments (e.g. see relationship strength
                between two groups of features with respect to output label)
                $vw-varinfo -q XY data.train

        vw-regr
        https://github.com/JohnLangford/vowpal_wabbit/wiki/Using-vw-regr
        Used for preprocessing and manipulating datasets (e.g. feature
        greater than, less than, binned)

        vw-top-errors
        https://github.com/arielf/vowpal_wabbit/wiki/vw-top-errors:-online-learning-debugging-for-better-models
        Debug to determine what's a good model by pointing out unusal
        deviations from model convergence.  Shows root causes of bad models
        like bad feature selection, bad feature engineering, bad tuning, etc.
            $vw-top-errors ... vw ... data.train
            where ... are optional parameters

    """

    # Saving your model into a file (e.g. final regressor weights of features)
    # $vw house_dataset -l 10 -c --passes 25 --holdout_off -f house.model
    """
        0600 0000 372e 372e 3000 6d00 0000 0000
        0080 3f12 0000 0000 0000 0000 0000 0000
        0000 0000 0000 0000 0000 0000 0000 0001
        0000 0000 0084 0700 008c e41e bfb8 0700
        008e 9f45 3fd6 0700 00cf 816e be5c c501
        0025 4494 3e25 7c02 0010 adc1 bc51 8502
        00f4 dd70 bd0e 8203 00f3 e054 be
    """

    # Getting predictions and seeing outputs
    # $vw house_dataset -p /dev/stdout --quiet
    """
        0.000000
        0.000000 second_house
        1.000000 third_house
    """

    # How to debug
    # $vw house_dataset --audit --quiet
    """
        0.000000
            ^price:229902:0.23:0@0  ^sqft:162853:0.25:0@0   ^age:165201:0.05:0@0    ^2006:2006:1:0@0   Constant:116060:1:0@0
        0.000000 second_house
            ^price:229902:0.18:0@0  ^sqft:162853:0.15:0@0   ^age:165201:0.35:0@0    ^1976:1976:1:0@0   Constant:116060:1:0@0
        1.000000 third_house
            ^price:229902:0.53:0.951045@0.2592  ^age:165201:0.87:0.488997@0.98  ^sqft:162853:0.32:1.14111@0.18 Constant:116060:1:0.171125@8     ^1924:1924:1:0@0

        * ^ means a 'namespace', which lets you group features and operate
            them in the core of VW with -q and --ignore
        * 229902 means the index of the feature (computed by a hash function
            on the feature name)
        * .23 is the value of the feature
        * 0 is the value of the feature's weight
        * @0.25 is the sum of gradients squared for that feature using a
            per-feature adaptive learning rate
        * Note: Feature 2006 uses index 2006.  You may use hashes as features
            Advantage of int-based feature-names is no collision after hashing
            Advantage of free-text (non-int) feature-names is readability
    """
