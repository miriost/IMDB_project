import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def isgenre(genre, genresList):
    if genre in genresList.split('|'):
        return True
    else:
        return False


def addgenres(df):
    # Move Genres to single boolean features: histogram of genres, see which are N most common, split to new feats
    genres = df['genres'].str.split('|', expand=True)
    mostCommonGenres = list(genres.stack().value_counts().head(5).index)
    for genre in mostCommonGenres:
         df['is' + genre] = df.apply(lambda x: isgenre(genre, x['genres']), axis=1)
    return df
    # Add all male/female cast

def is_blockbuster(df):
    # Which movies are blockbusters?
    # 3 categories - 1. High profit movie - we will decide this according to the gross column
    # 2. High ratio of budget/gross - would indicate 2 categories - low budget movies that earned at least 5 times more
    # more than they cost, and just good ROI movies -

    # First let's the histogram of gross
    # print(df['gross'])
    sns.set(style="whitegrid")
    sns.set_palette("husl")
    gross_sorted = df['gross'].sort_values(ascending=False, inplace=False)
    sns.distplot(gross_sorted.dropna(), bins=70, hist_kws=dict(edgecolor="k", linewidth=1, color = 'b'))
    plt.plot([2e8, 2e8], plt.ylim(), 'r')
    plt.title('Gross value histogram')
    plt.legend(['Histogram values', 'High profit threshold'])
    plt.show()
    # accroding to the histogram, we choose the high gross value to be 200 million and above
    df['is_blockbuster'] = df['gross'] > 0.2e9
    print(['number of high gross movies = ', sum(df['is_blockbuster'])])

    ratio = np.divide(df['gross'], df['budget'], out=np.zeros(len(df['gross'])), where=(df['budget'].replace([None], 0) != 0))
    #ratio = ratio[~np.isnan(ratio) & ~np.equal(ratio, 0)]
    df['is_blockbuster'] = np.bitwise_or(list(df['is_blockbuster']), ratio > 5)
    print(['number of total blockbusters = ', sum(df['is_blockbuster'])])
    return df
