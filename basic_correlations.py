import pandas as pd

import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from cleandata import clean
from currencyConvert import fixcurrency

df = pd.read_csv('movie_metadata.csv')
#df = clean(df)
#df = fixcurrency(df)
# plt.subplot(211)
# #
# years = list(range(int(min(df['title_year'][~np.isnan(df['title_year'])])),
#                    int(max(df['title_year'][~np.isnan(df['title_year'])]))))
# sns.distplot(df['title_year'][~np.isnan(df['title_year'])])
# plt.title('Title year histogram')
# plt.xlim(1900, 2020)
#
#
# # according to the simple year histogram we can note that we mainly deal with new films
#
# # movie facebook likes as a correlation to the year
# import ipdb
# #ipdb.set_trace()
#
# likes = np.zeros(len(years))
# for i in range(0, len(years)):
#     likes[i] = df['movie_facebook_likes'][df['title_year']==years[i]].mean()
# plt.subplot(212)
# plt.scatter(years, likes)
# plt.title('Average number of facebook likes over the years')
# plt.xlim(1900, 2020)
# plt.ylim(-1, max(likes)+1e3)
# plt.plot([2004, 2004], plt.ylim(), 'r')
# plt.legend(['facebook invention','Average likes'], loc = 'upper left')
# plt.show()

# Which movies are blockbusters?
# 3 categories - 1. High profit movie - we will decide this according to the gross column
# 2. High ratio of budget/gross - would indicate 2 categories - low budget movies that earned a
# lot more than they cost, and just good ROI movies

# First let's the histogram of budgets, and gross
#print(df['gross'])

# g = sns.JointGrid('budget', 'gross', df)
# g.plot_marginals(sns.distplot, hist=True, kde=True, color='blue')
# g.plot_joint(plt.scatter, color='black', edgecolor='black')
# ax = g.ax_joint
# ax.set_xscale('log')
# ax.set_yscale('log')
# g.ax_marg_x.set_xscale('log')
# g.ax_marg_y.set_yscale('log')
# plt.show()
# plt.figure()
# budg = df['budget']/1e6
# bins = [10, 100, 200, 300, 1000, 10000, 100000]
# sns.distplot(budg, hist=True, bins= bins)
# plt.show()
df['budget [Millions]'] = df['budget']/1e6
df.sort_values(by='budget [Millions]',ascending=False, inplace=True)

fig, ax = plt.subplots(1,2,figsize=(8, 3))

#sns.distplot(df['budget [Millions]'].values,bins=8,kde=False,ax=ax[0])
#ax[0].set_title('Linear Bins')

LogMin, LogMax = np.log10(df['budget [Millions]'].min()),np.log10(df['budget [Millions]'].max())
newBins = np.logspace(LogMin, LogMax,8)
sns.distplot(df['budget [Millions]'].values,bins=newBins,kde=False,ax=ax[1])
ax[1].set_xscale('log')
ax[1].set_title('Log Bins')

fig.show()
