## Working with names_DB.csv to anaylze all names in our movie DB

import pandas as pd
import csv

#df = pd.read_csv('movie_metadata.csv')
names = pd.read_csv('names_DB.csv')
names_dict = dict(zip(names['Name'], names['prob.gender']))
#problematic_names_dictionary = {}

def extract_first_name_gender(name):

    if not str or not(isinstance(name, str)):
        return 'Unknown'
    else:
        first_name = name.split()[0]
        try:
            first_name.encode('ascii')
        except UnicodeEncodeError:
            #add_name_to_problematic_DB(first_name)
            #print(first_name + ' added to problematic names and skipped (ascii)!')
            return ('Skipped')
        else:
            gender = get_gender(first_name)
            #print('first name: ' + first_name + ' gender: ' + gender)
            return (gender)

def add_name_to_problematic_DB(first_name):
    with open(r'problematic_names_DB.csv',
              'a', newline = '') as f:  # write all names you could not find at the end of the names_DB so I can manually add the gender
        writer = csv.writer(f)
        writer.writerow([first_name])
        # to do: add the row numbers from which the name came, check if the value already exists.

def get_gender(name):
    if name in names_dict:
        return(names_dict[name])
    else:
        return('Unknown')


def add_genders(df):
    """
    :type df: object
    """
    #names = pd.read_csv('names_DB.csv')
    #names_dict = dict(zip(names['Name'], names['prob.gender']))
    cols = ['actor_1_', 'actor_2_', 'actor_3_', 'director_']
    for feature in cols:
        df[feature+'gender'] = df[feature+'name'].apply(extract_first_name_gender)

    return df



#add_genders(df)
#df['actor_1_gender'] = df['actor_1_name'].apply(extract_first_name_gender)
#print(df[['actor_1_name', 'actor_1_gender']].head(100))
