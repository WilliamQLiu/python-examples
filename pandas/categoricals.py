import pandas


if __name__ == '__main__':
    # Setup
    df = pandas.DataFrame({'id':[1,2,3,4,5,6], 'raw_grade':['a', 'b', 'b', 'a', 'a', 'e']})
    #print "Original df is:"
    #print df

    # Create a new column as type 'category'
    df['grade'] = df['raw_grade'].astype('category')
    #print df['grade']  # Categories (3, object): [a < b < e]
    '''  id raw_grade  grade
          0   1         a
          1   2         b
          2   3         b
          3   4         a
          4   5         a
          5   6         e
    '''

    # Rename the categories
    df['grade'].cat.categories = ['very good', 'good', 'very bad']
    #print df['grade']  #
    '''    id raw_grade      grade
            0   1         a  very good
            1   2         b       good
            2   3         b       good
            3   4         a  very good
            4   5         a  very good
            5   6         e   very bad
    '''

    # Reorder the categories and add the missing categories
    df['grade'] = df['grade'].cat.set_categories(['very bad', 'bad', 'medium', 'good', 'very good'])

    # Sort by grade
    df.sort('grade')

    # Group by grade and size
    df = df.groupby('grade').size()
    print df
    '''
    grade
    very bad      1
    bad         NaN
    medium      NaN
    good          2
    very good     3
    '''
