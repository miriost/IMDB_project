import dlib
from scikit-image import io


def makefeats(df):
    # Move Genres to single boolean features: histogram of genres, see which are N most common, split to new feats
    genres = df['genres'].str.split('|', expand=True)
    mostCommonGenres = list(genres.stack().value_counts().head(5).index)
    for genre in mostCommonGenres:
         df['is' + genre] = df.apply(lambda x: isgenre(genre, x['genres']), axis=1)
    df['numfaces']


def facesinposter(movieName):
    pass