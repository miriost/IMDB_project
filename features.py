import pandas as pd



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


