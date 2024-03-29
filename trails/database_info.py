import sqlite3
import pandas as pd

def make_db(state):
    """
    This function should be only run ONCE and is used to create a SQL database
    corresponding to an individual state for scraping trail data. In the final version
    of the project, this was only done with California trails.
    """
    conn = sqlite3.connect("trails.db")
    cmd = f"""
    CREATE TABLE IF NOT EXISTS {state_name_code_name_dict[state]}(
    name VARCHAR(255),
    coords VARCHAR(255),
    Distance VARCHAR(255),
    'Avg time' VARCHAR(255),
    Climb VARCHAR(255),
    Descent VARCHAR(255),
    Activities VARCHAR(255),
    'Riding Area' VARCHAR(255),
    'Difficulty Rating' VARCHAR(255),
    'Dogs Allowed' VARCHAR(255),
    'Local Popularity' VARCHAR(255),
    'Altitude start' VARCHAR(255),
    'Altitude end' VARCHAR(255),
    Grade VARCHAR(255)
    );
    """
    cursor = conn.cursor()
    cursor.execute(cmd)
    cursor.close()
    conn.close()
    
def make_db_parks(state):
    """
    This function should be only run ONCE per state and is used to create a SQL database
    corresponding to an individual state for scraping park data.
    """
    conn = sqlite3.connect("trails_new.db")
    cmd = f"""
    CREATE TABLE IF NOT EXISTS {state_name_code_name_dict[state]}(
    Name VARCHAR(255),
    Location VARCHAR(255),
    Coords VARCHAR(255),
    'Trails (view details)' SMALLINT(255),
    'Total Distance' VARCHAR(255),
    'State Ranking' VARCHAR(255),
    'Access Road/Trail' SMALLINT(255),
    White SMALLINT(255),
    Green SMALLINT(255),
    Blue SMALLINT(255),
    Black SMALLINT(255),
    'Double Black Diamond' SMALLINT(255),
    Proline SMALLINT(255)
    );
    """
    cursor = conn.cursor()
    cursor.execute(cmd)
    cursor.close()
    conn.close()
    
def get_db():
    """
    This helper function accesses the `trails.db` SQL database which houses information
    on hiking trails available in California. To be used in `add_trails()`
    """
    conn = sqlite3.connect("trails.db")
    return conn
    
def add_trails(df,state):
    """
    This helper function is used in `scraper.py` to add information about trails to `trails.db`
    Inputs:
    ``df``: A `pandas` data frame that contains scraped information from TrailForks. Note that the
    format must align with the layout specified in `make_db_parks` via the use of scraping functions
    within `scraper.py`.
    ``state``: The name of the state in question. This is entered as an input to `state_scraper()` in `scraper.py`
    """
    conn = get_db()
    df.to_sql(state, conn, if_exists = "append", index = False)
    
def get_db_new():
    """
    This helper function accesses the `trails_new.db` SQL database which houses information
    on different parks in the US. To be used in `add_trails_new()`
    """
    conn = sqlite3.connect("trails_new.db")
    return conn
    
def add_trails_new(df,state):
    """
    This helper function is used in `scraper_parks.py` to add information about trails to `trails_new.db`
    Inputs:
    ``df``: A `pandas` data frame that contains scraped information from TrailForks. Note that the
    format must align with the layout specified in `make_db` via the use of scraping functions
    within `scraper_parks.py`.
    ``state``: The name of the state in question. This is entered as an input to `state_scraper()` in `scraper_parks.py`
    """
    conn = get_db_new()
    df.to_sql(state, conn, if_exists = "append", index = False)
    
###ADDITIONAL TABLES/LISTS
    
states = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "idaho-3166", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "new-hampshire", "new-jersey", "new-mexico", "new-york", "north-carolina", "north-dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "rhode-island", "south-carolina", "south-dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "west-virginia", "Wisconsin", "Wyoming"]
#State names formatted to align with TrailForks URLs

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
#Mapping between above list and spaceless string for state name


state_dictionary = {'Alabama': 11, 'Alaska': 11, 'Arizona': 49, 'Arkansas': 16, 'California': 152, 'Colorado': 69, 'Connecticut': 56, 'Delaware': 4, 'Florida': 18, 'Georgia': 17, 'Hawaii': 5, 'idaho-3166': 31, 'Illinois': 51, 'Indiana': 10, 'Iowa': 8, 'Kansas': 3, 'Kentucky': 9, 'Louisiana': 2, 'Maine': 27, 'Maryland': 16, 'Massachusetts': 146, 'Michigan': 55, 'Minnesota': 36, 'Mississippi': 3, 'Missouri': 11, 'Montana': 41, 'Nebraska': 3, 'Nevada': 16, 'new-hampshire': 41, 'new-jersey': 40, 'new-mexico': 25, 'new-york': 60, 'north-carolina': 26, 'north-dakota': 7, 'Ohio': 29, 'Oklahoma': 4, 'Oregon': 38, 'Pennsylvania': 54, 'rhode-island': 9, 'south-carolina': 6, 'south-dakota': 7, 'Tennessee': 16, 'Texas': 50, 'Utah': 62, 'Vermont': 25, 'Virginia': 27, 'Washington': 92, 'west-virginia': 18, 'Wisconsin': 25, 'Wyoming': 19}

#Number of pages on TrailForks per state for trails. See `scraper.py` to see how this was generated.

state_parks_dictionary = {'Alabama': 1, 'Alaska': 1, 'Arizona': 3, 'Arkansas': 2, 'California': 8, 'Colorado': 4, 'Connecticut': 7, 'Delaware': 1, 'Florida': 2, 'Georgia': 2, 'Hawaii': 1, 'idaho-3166': 2, 'Illinois': 10, 'Indiana': 1, 'Iowa': 1, 'Kansas': 1, 'Kentucky': 1, 'Louisiana': 1, 'Maine': 3, 'Maryland': 1, 'Massachusetts': 7, 'Michigan': 5, 'Minnesota': 3, 'Mississippi': 1, 'Missouri': 2, 'Montana': 2, 'Nebraska': 1, 'Nevada': 1, 'new-hampshire': 3, 'new-jersey': 3, 'new-mexico': 2, 'new-york': 5, 'north-carolina': 3, 'north-dakota': 1, 'Ohio': 4, 'Oklahoma': 1, 'Oregon': 3, 'Pennsylvania': 3, 'rhode-island': 1, 'south-carolina': 1, 'south-dakota': 1, 'Tennessee': 2, 'Texas': 4, 'Utah': 3, 'Vermont': 2, 'Virginia': 2, 'Washington': 6, 'west-virginia': 2, 'Wisconsin': 3, 'Wyoming': 1}

#Number of pages on TrailForks per state for parks. See `scraper_parks.py` to see how this was generated.

    

