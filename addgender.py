'''
USING GENDER API TO ANALYZE GENDERS ACCORDING TO THE FIRST NAMES OF DIRECTORS AND ACTORS
https://gender-api.com/en/api-docs
'''
print("Hello!")
import json
from urllib.request import urlopen
import pandas as pd


df = pd.read_csv('movie_metadata.csv')


def extract_first_name(name):

    if not str or not(isinstance(name, str)):
        return 'Unknown'
    else:
        first_name = name.split()[0]
        try:
            first_name.encode('ascii')
        except UnicodeEncodeError:
            print(first_name + 'skipped!')
            return ('Ascii error')
        else:
            gender = extract_gender(first_name)
            print('first name: ' + first_name + ' gender: ' + gender)  # we can improve accuracy by adding country
            return (gender)



def extract_gender(first_name):
    myKey = "SVlpDsZvjtJXjjzxCH"
    data = []
    data = json.load(urlopen("https://gender-api.com/get?key=" + myKey + "&name=" + first_name))
    return(data['gender'])

df['actor1_gender'] = df['actor_1_name'].apply(extract_first_name)

#first_names = df['director_name'][1:10]

# first_names = first_names.split(str = '')

