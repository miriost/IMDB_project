import pandas as pd

df = pd.read_csv('movie_metadata.csv')

# Color: blanks to "color"
df['color'] = df['color'].replace(['NaN', 'nan', None],'Color')


# Duration: Median
df['duration'] = df['duration'].replace([None],df['duration'].median())
# num_critics: 0
df['num_critic_for_reviews'] = df['num_critic_for_reviews'].replace([None], 0)
# Likes: 0
df['director_facebook_likes'] = df['director_facebook_likes'].replace([None], 0)
df['actor_1_facebook_likes'] = df['actor_1_facebook_likes'].replace([None], 0)
df['actor_2_facebook_likes'] = df['actor_2_facebook_likes'].replace([None], 0)
df['actor_1_facebook_likes'] = df['actor_3_facebook_likes'].replace([None], 0)
df['cast_total_facebook_likes'] = df['cast_total_facebook_likes'].replace([None], 0)
df['movie_facebook_likes'] = df['movie_facebook_likes'].replace([None], 0)

# Move Genres to single boolean features: histogram of genres, see which are N most common, split to new feats
genres = df['genres'].str.split('|', expand=True)
mostCommonGenres = list(genres.stack().value_counts().head(5).index)

def isgenre(genre, genresList):
     if genre in genresList.split('|'):
        return True
     else:
        return False

for genre in mostCommonGenres:
    df['is' + genre] = df.apply(lambda x: isgenre(genre, x['genres']),axis=1)
print(df['isAction'])
