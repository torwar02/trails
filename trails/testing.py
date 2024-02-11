import sqlite3
import pandas as pd
import database_info


def get_frame_csv(state):
    conn = database_info.get_db()
    cmd = \
    f"""
    SELECT * FROM {state}
    """
    df = pd.read_sql_query(cmd, conn)
    df.to_csv('trail_test_hawaii.csv',index = False)
    
get_frame_csv("Hawaii")
