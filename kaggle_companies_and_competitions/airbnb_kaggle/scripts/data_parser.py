import pandas as pd
import numpy as np


def get_user_data():
    users_info_path = "../train_users_2.csv"
    user_data = pd.read_csv(users_info_path).fillna('_missing_val_')
    return user_data

def get_sessions_data(): 
    sessions_info_path = "../sessions.csv"
    sessions_data = pd.read_csv(sessions_info_path).fillna('_missing_val_')
    return sessions_data




#user_made_res = user_data['date_first_booking'].tolist()
#user_made_res = [int(i != "_missing_val_") for i in user_made_res]


        

#print user_made_res

#print user_data.gender.unique()
#print user_data['gender'].tolist() #.gender.tolist()
#print user_data[[3]].tolist() 


