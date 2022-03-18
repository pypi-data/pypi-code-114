import os.path
import sqlite3

from aiscpy.info import nameTables, nameTablesDict

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR,'shapes_AISC.db')

class QueryingToDB():
    """Class for querying to DB's AISC
    """    
    def __init__(self, query: str, fetchone:bool = False) -> None:
        """class for querying to DB's AISC

        Args:
            query (str): Intruction in str
            fetchone (bool, optional): Is the method for selection of results. Defaults to False.

        Raises:
            TypeError: TypeError
        """         
        if not isinstance(fetchone, bool):
            raise TypeError('"fetchone" not in a bool')
        
        self.__fetchoneStatus = fetchone
        
        con = sqlite3.connect(db_path)
        cur = con.cursor()
        self.__query_execute = cur.execute(query)
        self.__keysQuery = [tuple[0] for tuple in self.__query_execute.description]
        
        if(fetchone):
            self.__query_list = list(self.__query_execute.fetchone())
        else:
            self.__query_list = list(self.__query_execute.fetchall())
            
        
        con.close()
    
    def __len__(self) -> int:
        return len(self.__query_list)
    
    @property
    def query(self):
        """return the query class

        Returns:
            queryClass: queryClass
        """        
        return self.__query_execute
    
    @property
    def queryToList(self):
        return self.__query_list
    
    @property
    def fetchoneStatus(self):
        return self.__fetchoneStatus
    
    @property
    def keysQuery(self):
        return self.__keysQuery
    
    def toDict(self):
        if (self.__fetchoneStatus):
            return dict(zip(self.__keysQuery, self.__query_list))
        else:
            raise ValueError('"fetchoneStatus" is False, not supported')

def updateTablesName():
    query_str = ''' SELECT name FROM sqlite_master
                    WHERE type='table' 
                '''
    tables = QueryingToDB(query_str)
    nameTables = []
    for i in range(0, len(tables)):
        nameTables.append(tables.queryToList[i][0])
        
    return nameTables

def selectTable(type: str)->str:
    for i in nameTables:
        if(type in nameTablesDict[i]):
            return i
    raise ValueError('not found table')
