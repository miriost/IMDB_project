import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from cleandata import clean
from currencyConvert import fixcurrency
import basic_correlations as eda
import regressions as reg
from names_DB_analysis import add_genders
import numpy as np


df = pd.read_csv('movie_metadata.csv')
df = clean(df)
df = fixcurrency(df)
# Add gender columns for director and 3 main actors
df= add_genders(df)
#print(df[['actor_1_name', 'actor_1_gender']].head(100))

# show feature correlation
selectedFeatures = ['imdb'
                    ''
                    '_score',
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
eda.is_blockbuster(df)
eda.gender_vs_score(df)

# Regressions parts

# reg.doForestRegression(df, selectedFeatures)
x_train, x_test, y_train, y_test = reg.createtesttrain(df, selectedFeatures, 6)
reg.showPca(x_train)
plt.show()
[ridge_test_error, ridge_train_error] = reg.doRidgeRegression(df, selectedFeatures)
[knn_test_error, knn_train_error] = reg.doKnnRegression(df, selectedFeatures, 5)
[bayes_test_error, bayes_train_error] = reg.doBayesianRegression(df, selectedFeatures)
[svm_test_error, svm_train_error] = reg.doSvmRegression(df, selectedFeatures)
[tree_test_error, tree_train_error] = reg.doDecisionTreeRegression(df, selectedFeatures)

train_error = [ridge_train_error, knn_train_error, bayes_train_error, svm_train_error, tree_train_error]
test_error = [ridge_test_error, knn_test_error, bayes_test_error, svm_test_error, tree_test_error]

col = {'Train Error': train_error,'Test Error': test_error}
models = ['Ridge Regression', 'Knn', 'Bayesian Regression', 'SVM', 'Decision Tree']
errors = pd.DataFrame(data=col, index=models)
errors.plot(kind='bar')
plt.show()

