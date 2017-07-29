import pandas as pd

df = pd.read_csv('movie_metadata.csv')
## DELETE THE NEXT PART AFTER CLEAN DATA CAN BE USED A A FUNCTION
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

## DELETE TIL HERE
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
plt.figure()
plt.style.use('classic')
plt.subplot(211)
#
years = list(range(int(min(df['title_year'][~np.isnan(df['title_year'])])),
                   int(max(df['title_year'][~np.isnan(df['title_year'])]))))
sns.distplot(df['title_year'][~np.isnan(df['title_year'])])
plt.title('Title year histogram')
plt.xlim(1900, 2020)


# according to the simple year histogram we can note that we mainly deal with new films

# movie facebook likes as a correlation to the year
import ipdb
#ipdb.set_trace()

likes = np.zeros(len(years))
for i in range(0, len(years)):
    likes[i] = df['movie_facebook_likes'][df['title_year']==years[i]].mean()
plt.subplot(212)
plt.scatter(years, likes)
plt.title('Average number of facebook likes over the years')
plt.xlim(1900, 2020)
plt.ylim(-1, max(likes)+1e3)
plt.plot([2004, 2004], plt.ylim(), 'r')
plt.legend(['facebook invention','Average likes'], loc = 'upper left')
plt.show()






