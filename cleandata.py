import pandas as pd
if __name__ == '__main__':
    df = pd.read_csv('movie_metadata.csv')



def clean(df):
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
    # unknown money values
    df['gross'] = df['gross'].replace([None], 0)
    df['budget'] = df['budget'].replace([None], 0)
    #clean TV shows
    df = df[df['content_rating'].str.contains("TV") != True]
    df = df[pd.notnull(df['title_year'])]

    return df
#print(df['isAction'])
