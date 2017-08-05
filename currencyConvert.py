import pandas as pd

currencies = pd.read_table('currencyTable.txt')
inflations = pd.read_csv('inflation.csv', delimiter='\t')

def convert(currencies, country, val, year):
    if year < 1960:
        return -999 # TODO how to return error codes?
    if country == 'USA':
        return val
    try:
        return val/currencies[currencies['Country Name'].str.match(country)][str(year)].iloc[0]
    except: # fails with countries like Soviet Union
        pass


def inflate(infaltions,val, title_year):
    if title_year < 1960:
        return -999 # TODO how to return error codes?
    multiplication_factor = 1
    for year in range(title_year, 2016):
        multiplication_factor *= (100 + infaltions[str(year)].iloc[0]) / 100
    return val*multiplication_factor



def fixcurrency(df):
    for feature in ['gross','budget']:
        df[feature] = df.apply(lambda x: convert(currencies, x['country'], x[feature], int(x['title_year'])), axis=1)
        df[feature] = df.apply(lambda x: inflate(inflations, x[feature], int(x['title_year'])), axis=1)
    return df

if __name__ == '__main__':
    df = pd.read_csv('movie_metadata.csv')
    country = 'Israel' # for testing
    year = 2010
    value = 1000
    print(inflate(inflations, val = value, title_year=year))
