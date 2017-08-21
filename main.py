import pandas as pd
from cleandata import clean
from currencyConvert import fixcurrency
import basic_correlations as eda
import numpy as np


df = pd.read_csv('movie_metadata.csv')
df = clean(df)
df = fixcurrency(df)

# EDA part:
eda.facebook_likes_over_the_years(df)

# according to the simple year histogram we can note that we mainly deal with new films
# from movie facebook likes as a correlation to the year we see that obviously since the facebook was first public, the
# number of likes per movie increased until it reached a certain stability.
# There are some exceptions of old movies with high likes, usually "classics"
# TODO arrows with examples of the exceptions

eda.facebook_likes_to_score(df)
# we can see that the the really low score movies (below 5) really don't receive many likes, but other than that, there
# seems to be no clear correlation between a high score and the number of likes.

# amax = np.argmax(df['budget'])
# print(amax)
# print(df['movie_title'][amax] + ' ;' + df['country'][amax] + ' ;' + str(df['budget'][amax]))

eda.budget_to_score(df)

