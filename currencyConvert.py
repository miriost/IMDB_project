import pandas as pd


def convert(currencies, country, val, year):
    if year < 1960:
        return -999 # TODO how to reutrn error codes?
    if country == 'USA':
        return val
    return currencies[currencies['Country Name'].str.match(country)][str(year)].iloc[0]


if __name__ == '__main__':
    df = pd.read_csv('movie_metadata.csv')
    currencies = pd.read_table('currencyTable.txt')
    country = 'Israel' # for testing
    print('The value is: ' + str(convert(currencies, country, 1, 2016)))

