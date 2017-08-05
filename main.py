import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LassoCV, Lasso
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from cleandata import clean
from currencyConvert import fixcurrency

df = pd.read_csv('movie_metadata.csv')
df = clean(df)
df = fixcurrency(df)

# show feature correlation
selectedFeatures = ['imdb_score',
                    'director_facebook_likes',
                    'num_critic_for_reviews',
                    'num_voted_users',
                    'duration',
                    'cast_total_facebook_likes',
                    'actor_1_facebook_likes',
                    'actor_2_facebook_likes',
                    'actor_3_facebook_likes',
                    'movie_facebook_likes',
                    'facenumber_in_poster',
                    'gross',
                    'budget']

sns.heatmap(df[selectedFeatures].corr())
plt.yticks(rotation=0)
plt.xticks(rotation=70)
plt.show()
