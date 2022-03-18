import configparser
from pathlib import Path
import pandas as pd
from typing import Any, Dict, List, NamedTuple
from datetime import datetime

from trk import DB_READ_ERROR, DB_WRITE_ERROR, CSV_ERROR, SUCCESS

DEFAULT_DB_FILE_PATH = Path.home().joinpath(
    "." + Path.home().stem + "_time_tracker.csv"
)

def get_database_path(config_file: Path) -> Path:
    """Return the current path to the to-do database."""
    config_parser = configparser.ConfigParser()
    config_parser.read(config_file)
    return Path(config_parser["General"]["database"])

def init_database(db_path: Path) -> int:
    """Create the to-do database."""
    try:
        # db_path.write_text("[]")  # Empty to-do list
        data_entry = pd.DataFrame({"start_time":[],
        "end_time": [],
        "duration_minutes":[],
        "task":[],
        "project":[],
        "client":[],
        "year": [],
        "month": [],
        "week":[],
        "date":[]  
              })

        data_entry.to_csv(db_path)
        return SUCCESS
    except OSError:
        return DB_WRITE_ERROR

class DatabaseHandler:
    def __init__(self, db_path: Path) -> None:
        self._db_path = db_path

    

    def read_events(self):
        try:
            self.db_trk = pd.read_csv(self._db_path)
            self.db_trk["start_time"] = pd.to_datetime(self.db_trk["start_time"], format =  "%Y-%m-%d %H:%M:%S" )
            self.db_trk["end_time"] = pd.to_datetime(self.db_trk["end_time"], format =  "%Y-%m-%d %H:%M:%S" )
            return(self.db_trk)

        except OSError:
            print("ERROR Happened")


    def write_event(self, event) :
        try:
            
            event.to_csv(self._db_path, index = False)
            return(event)
        except OSError:  # Catch file IO problems
            return DB_WRITE_ERROR