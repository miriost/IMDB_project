import pandas as pd

import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


def facebook_likes_over_the_years(df):
    plt.subplot(211)
    years = list(range(int(min(df['title_year'][~np.isnan(df['title_year'])])),
                       int(max(df['title_year'][~np.isnan(df['title_year'])]))))
    sns.distplot(df['title_year'][~np.isnan(df['title_year'])])
    plt.title('Title year histogram')
    plt.xlim(1900, 2020)
    plt.xlabel('')
    plt.ylabel('Frequency')

    likes = np.zeros(len(years))
    for i in range(0, len(years)):
        likes[i] = df['movie_facebook_likes'][df['title_year'] == years[i]].mean()
    plt.subplot(212)
    plt.scatter(years, likes)
    plt.title('Average number of facebook likes over the years')
    plt.xlim(1900, 2020)
    plt.ylim(-1, max(likes) + 1e3)
    plt.plot([2006, 2006], plt.ylim(), 'r')
    plt.legend(['facebook invention', 'Average likes'], loc='upper left')
    plt.xlabel('Title year')
    plt.show()


def facebook_likes_to_score(df):
    np.random.seed(19680801)
    colors = np.random.rand(len(df['imdb_score']))
    plt.scatter(df['imdb_score'], df['movie_facebook_likes'], c=colors, alpha=0.5)
    plt.title('Facebook likes vs. score')
    plt.xlabel('IMDB score')
    plt.ylabel('Number of facebook likes')
    plt.ylim(-1000, max(df['movie_facebook_likes']) + 1000)
    plt.show()


def budget_to_score(df):
    np.random.seed(19680801)
    colors = np.random.rand(len(df['imdb_score']))
    ratio = np.divide(df['gross'], df['budget'])
    print(ratio)
    plt.scatter(df['imdb_score'], ratio, c=colors, alpha=0.5)
    plt.title('Gross/Budget vs. score')
    plt.xlabel('IMDB score')
    plt.ylabel('Gross/bugdet ratio')
    plt.ylim(min(ratio), max(ratio))
    plt.show()

# Which movies are blockbusters?
# 3 categories - 1. High profit movie - we will decide this according to the gross column
# 2. High ratio of budget/gross - would indicate 2 categories - low budget movies that earned a
# lot more than they cost, and just good ROI movies

# First let's the histogram of budgets, and gross
# print(df['gross'])

# g = sns.JointGrid('budget', 'gross', df)
# g.plot_marginals(sns.distplot, hist=True, kde=True, color='blue')
# g.plot_joint(plt.scatter, color='black', edgecolor='black')
# ax = g.ax_joint
# ax.set_xscale('log')
# ax.set_yscale('log')
# g.ax_marg_x.set_xscale('log')
# g.ax_marg_y.set_yscale('log')
# plt.show()
# plt.figure()
# budg = df['budget']/1e6
# bins = [10, 100, 200, 300, 1000, 10000, 100000]
# sns.distplot(budg, hist=True, bins= bins)
# plt.show()
# df['budget [Millions]'] = df['budget']/1e6
# df.sort_values(by='budget [Millions]',ascending=False, inplace=True)
#
# fig, ax = plt.subplots(1,2,figsize=(8, 3))
#
# #sns.distplot(df['budget [Millions]'].values,bins=8,kde=False,ax=ax[0])
# #ax[0].set_title('Linear Bins')
#
# LogMin, LogMax = np.log10(df['budget [Millions]'].min()),np.log10(df['budget [Millions]'].max())
# newBins = np.logspace(LogMin, LogMax,8)
# sns.distplot(df['budget [Millions]'].values,bins=newBins,kde=False,ax=ax[1])
# ax[1].set_xscale('log')
# ax[1].set_title('Log Bins')
#
# fig.show()
