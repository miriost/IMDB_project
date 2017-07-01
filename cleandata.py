import pandas as pd

df = pd.read_csv('movie_metadata.csv')

# Color: blanks to "color"
df['color'] = df['color'].replace(['NaN', 'nan', None],'Color')


# Duration: Median
df['duration'] = df['duration'].replace([None],df['duration'].median())
