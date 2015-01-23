import numpy as np
import pandas as pd
from scipy import stats
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns


def simple_histogram():
    """ Simple histogram """
    data = np.random.randn(75)
    plt.hist(data, bins=10, color="#6495ED", alpha=.5)
    plt.title('Simple histogram')
    plt.show()


def simple_distplot():
    """ Variations on distribution plotting """
    f, axes = plt.subplots(2, 2, figsize=(7, 7), sharex=True)
    sns.despine(left=True)  # Remove left axis spine

    b, g, r, p = sns.color_palette("muted", 4)
    rs = np.random.RandomState(1234)  # create random probability distributions
    #print type(rs)  # <type 'mtrand.RandomState'>
    data = rs.normal(size=100)  # normal Gaussian distribution, 

    ### Plot across different parts of axes
    sns.distplot(data, kde=False, color=b, ax=axes[0, 0])
    sns.distplot(data, hist=False, rug=True, color=r, ax=axes[0,1])
    sns.distplot(data, hist=False, color=g, kde_kws={"shade": True}, ax=axes[1, 0])
    sns.distplot(data, color=p, ax=axes[1,1])

    plt.setp(axes, yticks=[])  # set property of no yticks
    plt.tight_layout()  # auto adjusts subplot params so subplots fit
    plt.show()


def facetgrid_example():
    """
        Use FacetGrid to visualize distribution of a variable's relationship
        between multiple variables; plot shows the same relationship 
            conditioned on different levels of other variables
        * Main approach, FacetGrid.map() with name(s) of variables in dataframe
        * FacetGrid initializes grid and sets up figure and axes
    """
    tips = sns.load_dataset("tips")
    # print tips.head()
    #   total_bill   tip   sex  smoker  day    time  size
    # 0      16.99  1.01  Male     No   Sun  Dinner     2

    # Histogram with split by Time (Dinner, Lunch)
    my_grid = sns.FacetGrid(tips, col="time")  # Splits by 'Dinner' and 'Lunch'
    my_grid.map(plt.hist, "tip")
    plt.show()

    # Scatterplot with split by Gender (Male, Female)
    my_grid = sns.FacetGrid(tips, col="sex", hue="smoker")  # Splits by M/F
    my_grid.map(plt.scatter, "total_bill", "tip", alpha=.7)
    my_grid.add_legend()
    plt.show()

    # Scatterplot with 4 way split by Time (Dinner, Lunch) and Smoker (Yes, No)
    my_grid = sns.FacetGrid(tips, row="smoker", col="time", margin_titles=True)
    my_grid.map(sns.regplot, "size", "total_bill", color=".3", fit_reg=False, x_jitter=.1)
    plt.show()

    # Barplot with split by Day (Fri, Sat, Sun) grouped by Gender (Male, Female)
    my_grid = sns.FacetGrid(tips, col="day", size=4, aspect=.5)
    my_grid.map(sns.barplot, "sex", "total_bill")
    plt.show()


def pairgrid_pairplot_example():
    """
        Draw a grid of small subplots with the same plot type in each
        PairGrid, each row and col is assigned to a different variable showing
            a plot of each pairwise relationship (scatterplot matrix)
        * PairGrid shows a different relationship conditioned on different levels
        of other variables.
        * pairplot is a quicker looker at the dataset
    """

    # Relationship plot
    iris = sns.load_dataset("iris")
    my_grid = sns.PairGrid(iris)
    my_grid.map(plt.scatter)
    plt.show()

    # Relationship plot and coloring a separate categorical variable
    my_grid = sns.PairGrid(iris, hue="species", palette="Set2")
    my_grid.map(plt.scatter)
    my_grid.add_legend()
    plt.show()


if __name__ == '__main__':

    # Set default options
    np.random.seed(1234)
    sns.set_context(rc={"figure.figsize": (6,6)})
    sns.set_palette(name="deep", n_colors=10, desat=.6)
    #palette names include deep,muted,bright,pastel,dark,colorblind

    # Plot
    #simple_histogram()
    #simple_distplot()
    facetgrid_example()
    pairgrid_pairplot_example()