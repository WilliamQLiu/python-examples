"""
    pandas' melt() function is useful to munge data from wide to long.
    1+ variables are identifers (id_vars) and remaining fields fall into
    two variables: variable and value.
"""


import pandas as pd


if __name__ == '__main__':

    # Setup data
    cheese = pd.DataFrame({'first_name': ['Will', 'Laura', 'Mike', 'Mandy'],
                           'last_name': ['Liu', 'Summers', 'Liu', 'Summers'],
                           'height': [5.10, 5.3, 5.9, 5.2],
                           'weight': [150, 120, 190, 110]})


    print cheese
    #   first_name  height  last_name   weight
    #0        Will    5.11        Liu     150
    #1       Laura     5.3    Summers     120
    #2        Mike     5.9        Liu     190
    #3       Mandy     5.2    Summers     110


    # Melt and specify variable name
    print pd.melt(cheese, id_vars=['first_name', 'last_name'])
    #   first_name  last_name  variable  value
    #0        Will        Liu    height   5.11
    #1       Laura    Summers    height    5.3
    #2        Mike        Liu    height    5.9
    #3       Mandy    Summers    height    5.2
    #4        Will        Liu    weight    150
    #5       Laura    Summers    weight    120
    #6        Mike        Liu    weight    190
    #7       Mandy    Summers    weight    110


    # Filter for a specific variable
    print pd.melt(cheese, id_vars=['first_name', 'last_name'],
                  var_name='quantity')
    #   first_name  last_name  quantity  value
    #0        Will        Liu    height   5.11
    #1       Laura    Summers    height    5.3
    #2        Mike        Liu    height    5.9
    #3       Mandy    Summers    height    5.2
