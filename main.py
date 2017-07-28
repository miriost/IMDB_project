import pandas as pd
from cleandata import clean
from currencyConvert import fixcurrency

df = pd.read_csv('movie_metadata.csv')
df = clean(df)
df = fixcurrency(df)
print(df['isAction'])
