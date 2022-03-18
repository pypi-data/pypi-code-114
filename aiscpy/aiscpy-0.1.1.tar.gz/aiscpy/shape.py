'''
*******************************************
*                                         *
* author : Rodrigo Jimenez                *
* E-mail : jimenezhuancarodrigo@gmail.com *
* copyright : (c) 2022                    *
* date : 2022                             *
*                                         *
*******************************************
'''

import sqlite3

from aiscpy.core import QueryingToDB


class Shape():
    def __init__(self, name: str) -> None:
        """Querying for shape objects

        Args:
            name (str): name of the shape object or name of section

        Raises:
            TypeError: Shape must be a string
        """        
        
        if not isinstance(name, str):
            raise TypeError("Shape must be a string")
        
        self.__name = name
        self.__queryStr: str = """SELECT * FROM `W-M-S-HP_shapes_AISC` 
                                    WHERE Shape= '""" + self.__name + """' """ 
        self.__query = QueryingToDB(self.__queryStr, fetchone=True)
        
    @property    
    def query(self):
        return self.__query
