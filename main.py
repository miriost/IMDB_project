import pandas as pd
from cleandata import clean
df = pd.read_csv('movie_metadata.csv')
df = clean(df)
print(df['isAction'])
