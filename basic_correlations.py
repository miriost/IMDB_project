import pandas as pd

import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import numpy as np


def facebook_likes_over_the_years(df):
    plt.subplot(211)
    years = list(range(int(min(df['title_year'][~np.isnan(df['title_year'])])),
                       int(max(df['title_year'][~np.isnan(df['title_year'])]))))
    sns.distplot(df['title_year'][~np.isnan(df['title_year'])],hist_kws=dict(edgecolor="k", linewidth=1, color = 'b'))
    plt.title('Title year histogram')
    plt.xlim(1900, 2020)
    plt.xlabel('')
    plt.ylabel('Frequency')

    likes = np.zeros(len(years))
    for i in range(0, len(years)):
        likes[i] = df['movie_facebook_likes'][df['title_year'] == years[i]].mean()
    plt.subplot(212)
    plt.scatter(years, likes, color = 'b')
    plt.title('Average number of facebook likes over the years')
    plt.xlim(1900, 2020)
    plt.ylim(-1, max(likes) + 1e3)
    plt.plot([2006, 2006], plt.ylim(), 'r')
    plt.legend(['facebook invention', 'Average likes'], loc='upper left')
    plt.xlabel('Title year')
    plt.show()


def facebook_likes_to_score(df):
    np.random.seed(19680801)
    colors = np.random.rand(len(df['imdb_score']),3)
    plt.scatter(df['imdb_score'], df['movie_facebook_likes'], c=colors, alpha=0.5, marker=(5, 2))
    plt.title('Facebook likes vs. score')
    plt.xlabel('IMDB score')
    plt.ylabel('Number of facebook likes')
    plt.ylim(-1000, max(df['movie_facebook_likes']) + 1000)
    plt.show()


def budget_to_score(df):
    np.random.seed(19680801)
    colors = np.random.rand(len(df['imdb_score']),3)
    ratio = np.divide(df['gross'], df['budget'], out=np.zeros(len(df['gross'])), where=(df['budget'].replace([None], 0) != 0))
    # for i in range(0,5000,100):
    #     print(['gross= ',list(df['gross'])[i], ' budget= ', list(df['budget'])[i], ' ratio= ', list(ratio)[i]])
#    print(ratio)
    plt.scatter(df['imdb_score'][ratio>0], ratio[ratio>0], c=colors[ratio>0], alpha=0.5)
    plt.plot([0, df['imdb_score'].max()],[5,5], 'r')
    ax = plt.gca()
    #ax.set_yscale('log')
    plt.title('Gross/Budget vs. score')
    plt.xlabel('IMDB score')
    plt.ylabel('Gross/bugdet ratio')
    plt.ylim(min(ratio), 30)
    plt.show()


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

def gender_vs_score(df):
    plt.subplot(121)
    sns.boxplot(x = df['actor_1_gender'][df['actor_1_gender'].isin(['Male', 'Female'])], y = 'imdb_score', data = df)
    plt.title('Actor 1 gender vs. score')
    plt.subplot(122)
    sns.boxplot(x = df['director_gender'][df['director_gender'].isin(['Male', 'Female'])], y = 'imdb_score', data = df)
    plt.title('Director vs. score')
    plt.show()