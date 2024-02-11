import sqlite3
import pandas as pd

def make_db(state):
    conn = sqlite3.connect("trails.db")
    cmd = f"""
    CREATE TABLE IF NOT EXISTS {state_name_code_name_dict[state]}(
    name VARCHAR(255),
    coords VARCHAR(255),
    distance VARCHAR(255),
    climb VARCHAR(255),
    descent VARCHAR(255),
    avg_time TIME,
    activities VARCHAR(255),
    difficulty VARCHAR(255),
    grade VARCHAR(255),
    altitude_start VARCHAR(255),
    altitude_end VARCHAR(255)
    );
    """
    cursor = conn.cursor()
    cursor.execute(cmd)
    cursor.close()
    conn.close()
    
def get_db():
    conn = sqlite3.connect("trails.db")
    return conn
    
def add_trails(df,state):
    conn = get_db()
    df.to_sql(state, conn, if_exists = "append", index = False)
    
states = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "idaho-3166", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "new-hampshire", "new-jersey", "new-mexico", "new-york", "north-carolina", "north-dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "rhode-island", "south-carolina", "south-dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "west-virginia", "Wisconsin", "Wyoming"]

state_name_code_name_dict = {
    'Alabama': 'Alabama',
    'Alaska': 'Alaska',
    'Arizona': 'Arizona',
    'Arkansas': 'Arkansas',
    'California': 'California',
    'Colorado': 'Colorado',
    'Connecticut': 'Connecticut',
    'Delaware': 'Delaware',
    'Florida': 'Florida',
    'Georgia': 'Georgia',
    'Hawaii': 'Hawaii',
    'idaho-3166': 'Idaho',
    'Illinois': 'Illinois',
    'Indiana': 'Indiana',
    'Iowa': 'Iowa',
    'Kansas': 'Kansas',
    'Kentucky': 'Kentucky',
    'Louisiana': 'Louisiana',
    'Maine': 'Maine',
    'Maryland': 'Maryland',
    'Massachusetts': 'Massachusetts',
    'Michigan': 'Michigan',
    'Minnesota': 'Minnesota',
    'Mississippi': 'Mississippi',
    'Missouri': 'Missouri',
    'Montana': 'Montana',
    'Nebraska': 'Nebraska',
    'Nevada': 'Nevada',
    'new-hampshire': 'NewHampshire',
    'new-jersey': 'NewJersey',
    'new-mexico': 'NewMexico',
    'new-york': 'NewYork',
    'north-carolina': 'NorthCarolina',
    'north-dakota': 'NorthDakota',
    'Ohio': 'Ohio',
    'Oklahoma': 'Oklahoma',
    'Oregon': 'Oregon',
    'Pennsylvania': 'Pennsylvania',
    'rhode-island': 'RhodeIsland',
    'south-carolina': 'SouthCarolina',
    'south-dakota': 'SouthDakota',
    'Tennessee': 'Tennessee',
    'Texas': 'Texas',
    'Utah': 'Utah',
    'Vermont': 'Vermont',
    'Virginia': 'Virginia',
    'Washington': 'Washington',
    'west-virginia': 'WestVirginia',
    'Wisconsin': 'Wisconsin',
    'Wyoming': 'Wyoming'
}


state_dictionary = {'Alabama': 11, 'Alaska': 11, 'Arizona': 49, 'Arkansas': 16, 'California': 152, 'Colorado': 69, 'Connecticut': 56, 'Delaware': 4, 'Florida': 18, 'Georgia': 17, 'Hawaii': 5, 'idaho-3166': 31, 'Illinois': 51, 'Indiana': 10, 'Iowa': 8, 'Kansas': 3, 'Kentucky': 9, 'Louisiana': 2, 'Maine': 27, 'Maryland': 16, 'Massachusetts': 146, 'Michigan': 55, 'Minnesota': 36, 'Mississippi': 3, 'Missouri': 11, 'Montana': 41, 'Nebraska': 3, 'Nevada': 16, 'new-hampshire': 41, 'new-jersey': 40, 'new-mexico': 25, 'new-york': 60, 'north-carolina': 26, 'north-dakota': 7, 'Ohio': 29, 'Oklahoma': 4, 'Oregon': 38, 'Pennsylvania': 54, 'rhode-island': 9, 'south-carolina': 6, 'south-dakota': 7, 'Tennessee': 16, 'Texas': 50, 'Utah': 62, 'Vermont': 25, 'Virginia': 27, 'Washington': 92, 'west-virginia': 18, 'Wisconsin': 25, 'Wyoming': 19}




    

