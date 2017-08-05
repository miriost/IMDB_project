import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from cleandata import clean
from currencyConvert import fixcurrency


df = pd.read_csv('movie_metadata.csv')
print(df['gross'])
#df = clean(df)
#df = fixcurrency(df)

np.random.seed(19680801)
colors = np.random.rand(len(df['imdb_score']))
ratio = np.divide(df['gross'], df['budget'])
print(df['gross'])
plt.scatter(df['imdb_score'], ratio, c=colors, alpha=0.5)
plt.title('Gross/Budget vs. score')
plt.xlabel('IMDB score')
plt.ylabel('Gross/bugdet ratio')
plt.ylim(min(ratio), max(ratio))
plt.show()