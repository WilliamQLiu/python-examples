import pandas as pd
import scipy.stats as stats


if __name__ == '__main__':

    raw_data = {'gender': ['Male', 'Female', 'Male', 'Male', 'Female', 'Male',
                           'Female', 'Male', 'Male', 'Female', 'Female',
                           'Female', 'Female', 'Female', 'Male', 'Female',
                           'Male', 'Female', 'Male', 'Male', 'Female',
                           'Female', 'Female', 'Male', 'Male'],
                'diet': ['Yes', 'No', 'No', 'Yes', 'No', 'Yes', 'Yes', 'No',
                         'Yes', 'No', 'No', 'Yes', 'Yes', 'No', 'No', 'Yes',
                         'No', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'Yes',
                         'No', 'No']}
    df = pd.DataFrame(raw_data, columns=['gender', 'diet'])
    print df
    #     gender diet
    # 0     Male  Yes
    # 1   Female   No
    # 2     Male   No
    # 3     Male  Yes
    # 4   Female   No
    # 5     Male  Yes
    # 6   Female  Yes
    # 7     Male   No
    # 8     Male  Yes
    # 9   Female   No
    # 10  Female   No
    # 11  Female  Yes
    # 12  Female  Yes
    # 13  Female   No
    # 14    Male   No
    # 15  Female  Yes
    # 16    Male   No
    # 17  Female  Yes
    # 18    Male  Yes
    # 19    Male   No
    # 20  Female  Yes
    # 21  Female  Yes
    # 22  Female  Yes
    # 23    Male   No
    # 24    Male   No

    # See crosstab of counts
    a = df['gender']
    b = df['diet']

    ct = pd.crosstab(index=a, columns=b)
    ct = ct[['Yes', 'No']]  # Reorder columns
    print ct
    # diet    Yes  No
    # gender
    # Female    8   5
    # Male      5   7

    row_1 = list(ct.ix['Female'])
    row_2 = list(ct.ix['Male'])

    fvalue, pvalue = stats.fisher_exact([row_1, row_2])
    print "fvalue is {f}, pvalue is {p}".format(f=fvalue, p=pvalue)
    # fvalue is 2.24, pvalue is 0.433752668115
