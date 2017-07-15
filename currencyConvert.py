import pandas as pd


def convert(currencies, country, val, year):
    if year < 1960:
        return -999 # TODO how to return error codes?
    if country == 'USA':
        return val
    return val*currencies[currencies['Country Name'].str.match(country)][str(year)].iloc[0]

def inflate(year):
    df = pd.read_csv('inflation.csv',delimiter  ='\t')
    if year < 1960:
        return -999 # TODO how to return error codes?
    return df[str(year)].iloc[0]

if __name__ == '__main__':
    df = pd.read_csv('movie_metadata.csv')
    currencies = pd.read_table('currencyTable.txt')
    country = 'Israel' # for testing
    year = 2016
    print('The value is: ' + str(convert(currencies, country, 1*inflate(year), year)))

