import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from cleandata import clean
from currencyConvert import fixcurrency
import basic_correlations as eda
import regressions as reg
from names_DB_analysis import add_genders
import numpy as np


df = pd.read_csv('movie_metadata.csv')
df= add_genders(df)
eda.gender_vs_score(df)