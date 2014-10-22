import pandas as pd


if __name__ == '__main__':
    raw_data = {'name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze', 'Jacon', 'Ryaner', 'Sone', 'Sloan', 'Piger', 'Riani', 'Ali'],
        #'score': [25, 94, 57, 62, 70, 25, 94, 57, 62, 70, 62, 70]
        'score': [1, 24, 25, 26, 30, 50, 55, 65, 74, 75, 80, 100]
        }
    df = pd.DataFrame(raw_data, columns = ['name', 'score'])

    #print df # Original

    #df['score'] = df['score'].astype('category')
    #print df['score']  # Categories (5, int64): [25 < 57 < 62 < 70 <94]

    #df['score'].cat.set_categories(['Low', 'Okay', 'Good', 'Great'])

    bins = [0, 25, 50, 75, 100]
    group_names = ['Low', 'Okay', 'Good', 'Great']

    #cat_obj = pd.cut(df['score'], bins, labels=group_names)
    #print cat_obj

    df['cat'] = pd.cut(df['score'], bins, labels=group_names)
    #print df['cat']  # Categories (4, object): [Low < Okay < Good < Great]
    #print df['score']
    #df['new'] = df['cat'].cat.set_categories(group_names)
    #df['new'] = df['new'].astype('category')
    #print df['new']
    #print df['cat']
    print df['cat']

    #df = df.groupby('cat').size()
    #print df
