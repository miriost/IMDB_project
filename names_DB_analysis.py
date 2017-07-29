## Working with names_DB.csv to anaylze all names in our movie DB

import pandas as pd
import csv

df = pd.read_csv('movie_metadata.csv')
problematic_names_dictionary = {}

def extract_first_name(name):

    if not str or not(isinstance(name, str)):
        return 'Unknown'
    else:
        first_name = name.split()[0]
        try:
            first_name.encode('ascii')
        except UnicodeEncodeError:
            add_name_to_problematic_DB(first_name)
            print(first_name + ' added to problematic names and skipped (ascii)!')
            return ('Skipped')
        else:
            gender = extract_gender(first_name)
            print('first name: ' + first_name + ' gender: ' + gender)
            return (gender)

def add_name_to_problematic_DB(first_name):
    with open(r'problematic_names_DB.csv',
              'a', newline = '') as f:  # write all names you could not find at the end of the names_DB so I can manually add the gender
        writer = csv.writer(f)
        writer.writerow([first_name])
        # to do: add the row numbers from which the name came, check if the value already exists.


def extract_gender(first_name):
    with open('names_DB.csv', 'rt') as f:
        reader = csv.reader(f, delimiter = ',')
        for row in reader:
            if first_name == row[0]:  # search the first name ijn the first column of the file
                if row[4] != "Unknown":
                    return(row[4])
                else:
                    add_name_to_problematic_DB(first_name)
                    print(first_name + ' added to problematic names and skipped (Returned: unknown)')
                    return ('Skipped')
        # if you reached the end of the file and you still haven't found the name:
        add_name_to_problematic_DB(first_name)
        print(first_name + ' added to problematic names and skipped (Not found in DB)!')
        return('Skipped')




df['actor1_gender'] = df['actor_1_name'].apply(extract_first_name)

#first_names = df['director_name'][1:10]

# first_names = first_names.split(str = '')

