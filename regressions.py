import pandas as pd
import numpy as np
import operator
from pprint import pprint
import matplotlib.pyplot as plt
from sklearn.linear_model import LassoCV, Lasso
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split



def doLassoRegression(df, features):
    X_train, X_test, y_train, y_test = train_test_split(
        df[features].drop('imdb_score', axis='columns').dropna(), df.dropna(subset=features,axis=0)['imdb_score'], test_size=0.3,
        random_state=777)
    lasso = LassoCV(normalize=True, copy_X=True, positive=True)
    lasso.fit(X_train, y_train)
    print('Alpha: %s' % lasso.alpha_)
    print('Train R^2: %s' % lasso.score(X_train, y_train))
    print('Test R^2: %s' % lasso.score(X_test, y_test))
    plt.scatter(y_test, lasso.predict(X_test))
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=4)
    plt.xscale('log')
    plt.yscale('log')
    plt.grid(True)
    plt.title('Residual plot')
    plt.xlabel('Measured')
    plt.ylabel('Predicted')
    plt.show()


def doForestRegression(df, features):
    X_train, X_test, y_train, y_test = train_test_split(
        df[features].drop('imdb_score', axis='columns').dropna(),
        df.dropna(subset=features, axis=0)['imdb_score'], test_size=0.3,
        random_state=777)
    forest = RandomForestRegressor(n_estimators=1000, oob_score=True, n_jobs=-1, max_features=0.5, min_samples_split=10)
    forest.fit(X_train, y_train)
    print('Train R^2: %s' % forest.score(X_train, y_train))
    print('Test R^2: %s' % forest.score(X_test, y_test))
    plt.scatter(y_test, forest.predict(X_test))
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=4)
    plt.xscale('log')
    plt.yscale('log')
    plt.grid(True)
    plt.title('Residual plot')
    plt.xlabel('Measured')
    plt.ylabel('Predicted')
    plt.show()

if __name__ == '__main__':
    df = pd.read_csv('movie_metadata.csv')
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
    doLassoRegression(df, selectedFeatures)
