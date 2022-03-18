from pathlib import Path
from typing import Any, Dict, List, NamedTuple
import pandas as pd
from datetime import datetime
from dateutil import parser

from trk import DB_READ_ERROR
from trk.database import DatabaseHandler

class Tracker:
    def __init__(self, db_path: Path) -> None:
        self._db_handler = DatabaseHandler(db_path) # DatabaseHandler component to facilitate direct communication with the to-do database

    def _check_last_event_status():
        pass

    def _get_min_duration(self, start_time, end_time):
        c = end_time - start_time
        minutes = c.total_seconds()/60
        return(minutes)
    def date_to_string(self,date_time):
        str_date = datetime.strftime(date_time, "%Y-%m-%d %H:%M:%S" )
        return(str_date)
        

    def get_date_item(self, date, type):
        if type == "year":
            item = date.strftime("%Y")
        if type == "week":
            item = date.isocalendar()[1]
        if type == "month":
            item = date.strftime("%m")
        if type == "today":
            item = date.strftime("%Y/%m/%d")
        return(item)

    def get_time(self,x = None):
        if x is None:
            date_time = datetime.now()
            return date_time
        else:
            date_time = parser.parse(x)            
            return date_time

    def start(self, event: str, start_time, project, client):
        """Add a new event to the database."""
        read = self._db_handler.read_events()

        number_rows = read.shape[0]
        if number_rows == 0:
            past_task = "no entries"
        else:
            number_rows = read.shape[0]-1 
            past_task = str(read.iloc[number_rows]['end_time'])
        #print(str(past_task))

        if past_task == "nan":
            str_time = None
            error = "The previous task was not stopped. Use trk stop to end the last task at current time, or trk stop -t to use a custom time"
            return str_time, error
        else:

            error = None

            if (start_time is None):
                start_time = self.get_time()
            else:
                start_time =  self.get_time(start_time)

            year = self.get_date_item(start_time, "year")
            month = self.get_date_item(start_time, "month")
            week = self.get_date_item(start_time, "week")
            date = self.get_date_item(start_time, "today")

            str_time = self.date_to_string(start_time)
            event_trk = pd.DataFrame({"start_time" :[str_time],
                "end_time": [None],
                "duration_minutes": [None],
                "task":[event],
                "project":[project],
                "client":[client],
                "year": [year],
                "month": [month],
                "week":[week],
                "date":[date]})

            db_trk = pd.concat((read, event_trk),axis= 0)
            self._db_handler.write_event(db_trk)
            return str_time, error

    def stop(self, end_time):
        """End the time for a event"""

        if (end_time is None):
            end_time = self.get_time()  
        else:
            end_time =  self.get_time(end_time) 


        read = self._db_handler.read_events()
        number_rows = read.shape[0]-1  
        
        start_time = self.get_time(read.iloc[number_rows]['start_time']) # this is already a time stamp cause of the read functionality
        print(type(start_time))
        str_start_time = self.date_to_string(start_time)
        str_end_time = self.date_to_string(end_time)

        read.at[number_rows, "end_time"] = str_end_time # record end time      

        
        task =  read.iloc[number_rows]['task']
        project =  read.iloc[number_rows]['project']
        client = read.iloc[number_rows]['client']

        minutes = self._get_min_duration(start_time, end_time)
        str_minutes = str(round(minutes, 1))

        read.at[number_rows, "duration_minutes"] = minutes              
        self._db_handler.write_event(read)     

        return task, project, client, str_start_time, str_end_time, str_minutes

    def add(self, event, start, stop, project, client):
        self.start(event, start, project, client)
        task, project, client, str_start_time, str_end_time, str_minutes = self.stop(stop)
        return task, project, client, str_start_time, str_end_time, str_minutes

    def list_unique_series(self, column):
         read = self._db_handler.read_events()
         ls_values = pd.unique(read[column])
         #print(ls_values)
         return(ls_values)


    def list_unique(self, column):
        read = self._db_handler.read_events()
        read_unique = read.drop_duplicates(subset= column)[[column]]
        return(read_unique)

    def summary(self, columns):
        read = self._db_handler.read_events()
        summary_table = read.groupby(columns)["duration_minutes"].sum().reset_index()
        return(summary_table)




        


    


        
