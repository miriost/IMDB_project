import pandas as pd
import numpy as np
from sklearn import tree
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.preprocessing import StandardScaler
import statsmodels.formula.api as smf
import statsmodels.api as sm
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns
from sklearn import neighbors
from sklearn import linear_model
from sklearn.decomposition import PCA
from sklearn.linear_model import LassoCV, Lasso
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split


def createtesttrain(df,features, nPca):
    x_train, x_test, y_train, y_test = train_test_split(
        df[features].drop('imdb_score', axis='columns').dropna(), df.dropna(subset=features, axis=0)['imdb_score'],
        test_size=0.3,
        random_state=666)
    x_train = StandardScaler().fit_transform(x_train)
    x_test = StandardScaler().fit_transform(x_test)

    sklearn_pca = PCA(n_components=nPca)
    x_train = sklearn_pca.fit_transform(x_train)
    x_test = sklearn_pca.fit_transform(x_test)

    return x_train, x_test, list(y_train), list(y_test)


def showPca(X_std):
    pca = PCA().fit(X_std)
    plt.plot(np.cumsum(pca.explained_variance_ratio_))
    plt.xlim(0, 7, 1)
    plt.xlabel('Number of components')
    plt.ylabel('Cumulative explained variance')
    plt.title('#PCA of selected features')

def calcerror(predict, test):
    error = 0
    for i in range(len(test)):
        error += (abs(test[i] - predict[i]) / test[i])
    return error / len(test) * 100

def doRidgeRegression(df, features):
    x_train, x_test, y_train, y_test = createtesttrain(df, features, 6)
    model = linear_model.Ridge()
    model.fit(x_train, y_train)

    y_predict = model.predict(x_train)
    train_error = calcerror(y_predict, y_train)
    print("Train error = "'{}'.format(train_error) + " percent in Ridge Regression")

    prediction = model.predict(x_test)
    test_error = calcerror(prediction, y_test)
    print("Test error = "'{}'.format(test_error) + " percent in Ridge Regression")
    return train_error, test_error


def doKnnRegression(df, features, n_neighbors):
    x_train, x_test, y_train, y_test = createtesttrain(df, features, 6)
    model = neighbors.KNeighborsRegressor(n_neighbors, weights='uniform')
    model.fit(x_train, y_train)

    y_predict = model.predict(x_train)
    train_error = calcerror(y_predict, y_train)
    print("Train error = "'{}'.format(train_error) + " percent in KNN Regression")

    prediction = model.predict(x_test)
    test_error = calcerror(prediction, y_test)
    print("Test error = "'{}'.format(test_error) + " percent in KNN Regression")
    return train_error, test_error


def doBayesianRegression(df, features):
    x_train, x_test, y_train, y_test = createtesttrain(df, features, 6)
    model = linear_model.BayesianRidge()
    model.fit(x_train, y_train)

    y_predict = model.predict(x_train)
    train_error = calcerror(y_predict, y_train)
    print("Train error = "'{}'.format(train_error) + " percent in Bayesian Regression")

    prediction = model.predict(x_test)
    test_error = calcerror(prediction, y_test)
    print("Test error = "'{}'.format(test_error) + " percent in Bayesian Regression")
    return train_error, test_error


def doDecisionTreeRegression(df, features):
    x_train, x_test, y_train, y_test = createtesttrain(df, features, 6)
    model = tree.DecisionTreeRegressor(max_depth=1)
    model.fit(x_train, y_train)

    y_predict = model.predict(x_train)
    train_error = calcerror(y_predict, y_train)
    print("Train error = "'{}'.format(train_error) + " percent in Decision Tree  Regression")

    prediction = model.predict(x_test)
    test_error = calcerror(prediction, y_test)
    print("Test error = "'{}'.format(test_error) + " percent in Decision Tree  Regression")
    return train_error, test_error


def doSvmRegression(df, features):
    x_train, x_test, y_train, y_test = createtesttrain(df, features, 6)
    model = svm.SVR()
    model.fit(x_train, y_train)

    y_predict = model.predict(x_train)
    train_error = calcerror(y_predict, y_train)
    print("Train error = "'{}'.format(train_error) + " percent in SVM  Regression")

    prediction = model.predict(x_test)
    test_error = calcerror(prediction, y_test)
    print("Test error = "'{}'.format(test_error) + " percent in SVM  Regression")
    return train_error, test_error



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
