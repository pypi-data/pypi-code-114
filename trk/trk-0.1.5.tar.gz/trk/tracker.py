
import pandas as pd
from datetime import datetime

class Tracker:

    '''Represents a time tracker'''

    def __init__(self):
        self.tracker = pd.DataFrame({"time_start" :[],"time_end": [],"task":[],"project":[],"client":[]})
        
    def start_entry(self, task_name , project_name = None, client_name = None):
        time_start = datetime.now()
        self.data_entry = pd.DataFrame({"time_start" :[time_start],
        "time_end": [None],
        "task":[task_name],
        "project":[project_name],
        "client":[client_name]})

        self.tracker = pd.concat((self.tracker, self.data_entry), axis = 0)
        return(self.tracker)

    def end_entry(self):

        number_rows = self.tracker.shape[0]-1
        time_end = datetime.now()
        self.tracker.at[number_rows, "time_end"] = datetime.now()
        return(self.tracker)

    def show_tracker(self):
       return(self.tracker)

    def save_tracker(self):

        self.tracker.to_csv("/mnt/c/Users/nicho/Documents/timetracker.csv", index= False)
        pass
