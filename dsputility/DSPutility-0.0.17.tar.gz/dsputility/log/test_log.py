from DSPlogging import log
#import pytest
import unittest
import asyncio
import os

from fastapi.testclient import TestClient
from fastapi import FastAPI, APIRouter

from pydantic import BaseModel, Field
from typing import Optional, Union, NewType, Tuple, List, Dict, DefaultDict

class TestLogWrapper01General(unittest.TestCase):
    """Test cases for decorated general/async functions
    """
    
    def setUp(self):
        """Set up for every test in this class. Test for repeating initialization to same log file (under 'a' mode).
        """
        self.file = os.path.basename(__file__)    
        self.log = log(logPath=self.logPath)

    def tearDown(self):
        """Tear down for every test in this class. Nothing to do.
        """
        pass

    @classmethod
    def setUpClass(cls):
        """Set up for all test in this class. Generating class scope log instance and class scope log file (under 'w' mode).
        """
        cls.logPath = 'general_error.log'
        cls.file = os.path.basename(__file__)    
        cls.log = log(logPath=cls.logPath)
        cls.skipChar = 24 # to skip datetime of records in log file

    @classmethod
    def tearDownClass(cls):
        """Tear down for all test in this class. Remove shared log file for every test in this class.
        """
        os.remove(cls.logPath)

    def test01_class_scope_normal1(self):
        @self.log.errlog(self.file)
        def inner_scope_normal1():
            """ this function won't cause any error being logged used to test log.headLines
            """
            x = 0
            y = x + 1

        inner_scope_normal1()
        answer = self.log.headLines
        content = self.log.readLog(skipLine=0, skipChar=0)
        self.assertEqual(content, answer)

    def test02_class_scope_normal2(self):
        @self.log.errlog(self.file)
        def inner_scope_normal2():
            """It won't cause any error being logged. Testing for log.headLines
            """
            with open(f'./{self.file}', 'r') as rf:
                rf.read()

        inner_scope_normal2()
        answer = self.log.headLines
        content = self.log.readLog(skipLine=0, skipChar=0)
        self.assertEqual(content, answer)

    def test03_class_scope_error1(self):
        @self.log.errlog(self.file)
        def inner_scope_error1():
            """It will cause NameError: name 'x' is not defined. Testing for skipLine default value of log.readLog() and logging function
            """
            y = x + 1

        inner_scope_error1()
        answer = f"|{self.log.logger.name}        |ERROR   |@{self.file}/inner_scope_error1: name 'x' is not defined\n"
        content = self.log.readLog(skipChar=self.skipChar)
        self.assertEqual(content, answer)

    def test04_class_scope_error2(self):
        @self.log.errlog(self.file) 
        def inner_scope_error2():
            """It will cause division by zero error. Testing for skipLine default value of log.readLog() and logging function
            """
            # this function cause NameError: name 'x' is not defined
            y = 3/0

        inner_scope_error2()
        answer = f"|{self.log.logger.name}        |ERROR   |@{self.file}/inner_scope_error2: division by zero\n"
        content = self.log.readLog(skipLine=self.log.nHeadLines+1, skipChar=self.skipChar)
        self.assertEqual(content, answer)

    def test05_class_scope_error3(self):
        @self.log.errlog(self.file)
        def inner_scope_error3():
            """It will cause file not exist error. Testing for skipLine default value of log.readLog() and logging function
            """
            # this function cause NameError: name 'x' is not defined
            with open('file not exist', 'r') as rf:
                rf.read()
            
        inner_scope_error3()
        answer = f"|{self.log.logger.name}        |ERROR   |@{self.file}/inner_scope_error3: [Errno 2] No such file or directory: 'file not exist'\n"
        content = self.log.readLog(skipLine=self.log.nHeadLines+2, skipChar=self.skipChar)
        self.assertEqual(content, answer)

    def test06_class_scope_async_normal1(self):
        import requests

        @self.log.errlog(self.file)
        async def inner_scope_async_normal1():
            loop = asyncio.get_event_loop()
            future  = loop.run_in_executor(None, requests.get, 'https://www.google.com')
            response = await future
            return response

        loop = asyncio.get_event_loop()
        loop.run_until_complete(inner_scope_async_normal1())
        answer = f"|{self.log.logger.name}        |ERROR   |@{self.file}/inner_scope_error1: name 'x' is not defined\n" + \
                 f"|{self.log.logger.name}        |ERROR   |@{self.file}/inner_scope_error2: division by zero\n" + \
                 f"|{self.log.logger.name}        |ERROR   |@{self.file}/inner_scope_error3: [Errno 2] No such file or directory: 'file not exist'\n"
        content = self.log.readLog(skipChar=self.skipChar)
        self.assertEqual(content, answer)

    def test07_class_scope_async_error1(self):
        import requests

        @self.log.errlog(self.file)
        async def inner_scope_async_error1():
            """It will cause 404 Client Error. Testing for logging on async function
            """
            loop = asyncio.get_event_loop()
            future  = loop.run_in_executor(None, requests.get, 'http://www.google.com/nopage')
            response = await future
            response.raise_for_status()
            return response
            
        loop = asyncio.get_event_loop()
        loop.run_until_complete(inner_scope_async_error1())
        answer = f"|{self.log.logger.name}        |ERROR   |@{self.file}/inner_scope_async_error1: 404 Client Error: Not Found for url: http://www.google.com/nopage\n"
        content = self.log.readLog(skipLine=self.log.nHeadLines+3, skipChar=self.skipChar)
        self.assertEqual(content, answer)


class TestLogWrapper02FastAPI(unittest.TestCase):
    """Test cases for decorated FastAPI functions
    """
    import json

    class Json1(BaseModel):
        id: Union[int, None]
        name: str
        config: Union[Dict, None]

    def setUp(self):
        """Set up for every test in this class. Test for repeating initialization to same log file (under 'a' mode).
        """
        self.file = os.path.basename(__file__)    
        self.log = log(logPath=self.logPath)
        self.skipChar = 24 # to skip datetime of records in log file

    def tearDown(self):
        """Tear down for every test in this class. Nothing to do.
        """
        pass

    @classmethod
    def setUpClass(cls):
        """Set up for all test in this class. Generating class scope log instance and class scope log file (under 'w' mode).
        """   
        cls.logPath = 'fast_api.log'
        cls.file = os.path.basename(__file__)    
        cls.log = log(logPath=cls.logPath)
        cls.skipChar = 24 # to skip datetime of records in log file

        cls.app = FastAPI()

        @staticmethod
        @cls.app.post("/test/echo", response_model=cls.Json1)
        @cls.log.errlog(cls.file)
        async def echo(request: cls.Json1):
            """A naive POST api which is able to receive request with json. It will cause customed exception. Testing for logging async FastAPI fucntion

            :param request: api request
            :raises Exception: IllegalAccessError is a customed exception
            :return: received json
            """
            id, name, config = request.id, request.name, request.config
            if name == 'root': 
                raise Exception("IllegalAccessError", "'root' access is unauthorized.")
            return {'id':id, 'name':name, 'config':config}

        cls.client = TestClient(cls.app)
    
    @classmethod
    def tearDownClass(cls):
        """Tear down for all test in this class. Remove shared log file for every test in this class.
        """
        os.remove(cls.logPath)

    def test01_fastapi_echo_normal1(self):
        """It won't cause any error being logged. Testing for FastAPI inside class scope
        """
        import json
        answer = {"id": 1234, "name": "Johndoe John", "config": {"verbose":True, "level":3}}
        response = self.client.post("/test/echo", json=answer)
        self.assertEqual(response.json(), answer)
 
    def test02_fastapi_echo(self):
        """It will cause customed exception: IllegalAccessError. Testing for FastAPI inside class scope
        """
        import json
        answer = {"id": 0, "name": "root", "config": {"verbose":True, "level":3}}
        response = self.client.post("/test/echo", json=answer)
        answer = f"|{self.log.logger.name}             |ERROR   |@{self.file}/echo: ('IllegalAccessError', \"'root' access is unauthorized.\")\n"
        content = self.log.readLog(skipChar=self.skipChar)
        self.assertEqual(content, answer)

if __name__ == "__main__":
    unittest.main()