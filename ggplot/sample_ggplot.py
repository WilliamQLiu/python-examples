from ggplot import *


def data_describe():
    print "Describing the Data"
    print diamonds.head()
    """
       carat      cut color clarity  depth  table  price     x     y     z
    0   0.23    Ideal     E     SI2   61.5     55    326  3.95  3.98  2.43
    1   0.21  Premium     E     SI1   59.8     61    326  3.89  3.84  2.31
    2   0.23     Good     E     VS1   56.9     65    327  4.05  4.07  2.31
    3   0.29  Premium     I     VS2   62.4     58    334  4.20  4.23  2.63
    4   0.31     Good     J     SI2   63.3     58    335  4.34  4.35  2.75
    """


def plot_trendline():
    print "Add different layers to a plot, including points and trendline"
    p = ggplot(aes(x='date', y='beef'), data=meat)  # Blank Canvas
    p = p + geom_point()  # Add points
    p = p + geom_line()  # Connect points as a line
    p = p + stat_smooth(color='blue')  # Add a trendline
    print p


def facet_histogram():
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
    plot_trendline()
    #facet_histogram()
    #facet_scatter_two()
    #facet_scatter_three()
