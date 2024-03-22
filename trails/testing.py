import sqlite3
import pandas as pd
import database_info


def get_frame_csv(state):
    conn = database_info.get_db_new()
    cmd = \
    f"""
    SELECT * FROM {state}
    """
    df = pd.read_sql_query(cmd, conn)
    df.to_csv('parks_wyoming.csv',index = False)
#
get_frame_csv("Wyoming")

#for key, value in database_info.state_name_code_name_dict.items():
#    database_info.make_db(key)


# Making your own machine learning models (depending on the structure of your network)
#opencv -- image processing tool, usually if not simple classification
#segmenting pixels into different types of train
#potentially sentiment analysis
