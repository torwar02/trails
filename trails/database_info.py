import sqlite3
import pandas as pd

def create_db(state):
    conn = sqlite3.connect("trails.db")
    cmd = """
    CREATE TABLE IF NOT EXISTS {state}(
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
    
states = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]



    

