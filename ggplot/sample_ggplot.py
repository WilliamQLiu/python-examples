from ggplot import *


def data_describe():
    print "Describing the Data - Diamonds"
    print type(diamonds)
    print diamonds.head()

    """
    <class 'pandas.core.frame.DataFrame'>
       carat      cut color clarity  depth  table  price     x     y     z
    0   0.23    Ideal     E     SI2   61.5     55    326  3.95  3.98  2.43
    1   0.21  Premium     E     SI1   59.8     61    326  3.89  3.84  2.31
    2   0.23     Good     E     VS1   56.9     65    327  4.05  4.07  2.31
    3   0.29  Premium     I     VS2   62.4     58    334  4.20  4.23  2.63
    4   0.31     Good     J     SI2   63.3     58    335  4.34  4.35  2.75
    """

    print "Describing the Data - Meat"
    print type(meat)
    print meat.head()
    """
            date  beef  veal  pork  lamb_and_mutton  broilers  other_chicken  turkey
    0 1944-01-01   751    85  1280               89       NaN            NaN        NaN
    1 1944-02-01   713    77  1169               72       NaN            NaN        NaN
    2 1944-03-01   741    90  1128               75       NaN            NaN        NaN
    3 1944-04-01   650    89   978               66       NaN            NaN        NaN
    4 1944-05-01   681   106  1029               78       NaN            NaN        NaN
    """

    print "Describing the Data - mtcars"
    print type(mtcars)
    print mtcars.head()
    """
                    name   mpg  cyl  disp   hp  drat     wt   qsec  vs  am  gear  carb
    0          Mazda RX4  21.0    6   160  110  3.90  2.620  16.46   0   1     4     4
    1      Mazda RX4 Wag  21.0    6   160  110  3.90  2.875  17.02   0   1     4     4
    2         Datsun 710  22.8    4   108   93  3.85  2.320  18.61   1   1     4     1
    3     Hornet 4 Drive  21.4    6   258  110  3.08  3.215  19.44   1   0     3     1
    4  Hornet Sportabout  18.7    8   360  175  3.15  3.440  17.02   0   0     3     2
    """

def plot_trendline():

    print "Add different layers to a plot, including points and trendline"
    p = ggplot(aes(x='date', y='beef'), data=meat)  # Blank Canvas
    p = p + geom_point()  # Add points
    p = p + geom_line()  # Connect points as a line
    p = p + stat_smooth(color='blue')  # Add a trendline
    print p


def facet_histogram():
    print diamonds
    print "Faceting Histogram Example"
    p = ggplot(aes(x='price'), data=diamonds)
    p = p + geom_histogram() + facet_wrap('cut')
    print p


def facet_scatter_two():
    print "Faceting Scatter Plot with 2 variables"
    p = ggplot(aes(x='wt', y='mpg'), data=mtcars)
    p = p + geom_point() + facet_grid('cyl', 'gear', scales='free_y')
    print p


def facet_scatter_three():
    print "Faceting Scatter plot with 3 variables"
    p = ggplot(aes(x='carat', y='price', colour='cut'), data=diamonds) + \
        geom_point() + facet_wrap('clarity')
    print p


if __name__ == '__main__':

    data_describe()
    #plot_trendline()
    facet_histogram()
    #facet_scatter_two()
    #facet_scatter_three()
