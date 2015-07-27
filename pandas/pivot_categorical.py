import pandas as pd

df = pd.DataFrame({
    'id': [25418726, 25418726, 25418731, 25418731, 25418740],
    'question': ['A', 'B', 'A', 'B', 'A'],
    'answer': ['V', 'W', 'X', 'Y', 'Z']
    })


if __name__ == '__main__':
    print df
    #  answer        id question
    #0      V  25418726        A
    #1      W  25418726        A
    #2      X  25418731        A
    #3      Y  25418731        A
    #4      Z  25418726        B

    temp = df.pivot(index='id', columns='question', values='answer')
    print temp
    #ValueError: Index contains duplicate entries, cannot reshape

    #temp = pd.pivot_table(df, index='id', columns='question', values='answer')
    #print temp
    #pandas.core.groupby.DataError: No numeric types to aggregate

    #temp = pd.pivot_table(df, index='id',
    #                      columns='question',
    #                      values='answer',
    #                      aggfunc = lambda x: x.to_string())
    #print temp