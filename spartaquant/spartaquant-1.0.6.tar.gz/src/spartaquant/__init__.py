# **********************************************************************************************************************
# SpartaQuant is a modular platform both for Python developers and decision makers
# This API requires an access token that can be generated in your SpartaQuant settings section
# Make sure you already have an account or get one at https://www.spartaquant.com
# For more information regarding this API, check the webpage https://spartaquant.pro/publicAPI

# Author: Benjamin Meyer
# **********************************************************************************************************************

import os
import getpass
import requests
import inspect
import json
import base64
import pickle
import sqlite3

class spartaquant():
    '''
        To use this API you can start with the following lines:

        import spartaquant as sq
        sq = sq.spartaquant()

        Then, you can retrieve information using the following method, for instance
            sq.getDataDB() to get all the available SpartaQuant objects
            sq.getFunctionsDB() to get all the available SpartaQuant functions
            etc...
    '''

    def __init__(self, bAuthenticate=True):
        self.URL_BASE = None
        self.VALID_ACCESS_KEY = None
        if bAuthenticate:
            self.authenticate()

    def authenticate(self):
        '''
            API authentication
        '''
        bInternalJupyterDesktop = False
        # try:
        #     self.URL_BASE, self.USER_ID = self.getDBAuthFunc()
        #     bInternalJupyterDesktop = True
        # except Exception as e:
        #     pass
        if not bInternalJupyterDesktop:
            accessKey = getpass.getpass(prompt="Enter your access key")
            return self.authenticateFunc(accessKey)

    def authenticateFunc(self, accessKey):
        '''
            API authentication function
        '''
        def printError():
            print("Authentication failed. Make sure you have entered the correct accessKey")

        try:
            mainUrl = self.decodeMainUrl(accessKey)
        except:
            printError()
            return
            
        validateUrl = mainUrl+'validateMainUrlExternalApi'
        newJson = dict()
        json_data = dict()
        json_data['accessKey'] = accessKey
        newJson['jsonData'] = json.dumps(json_data)
        newJsonB = json.dumps(newJson)
        try:
            res = requests.post(validateUrl, data=newJsonB, verify=False)
            statusCode = res.status_code
            if int(statusCode) == 200:
                resJson = json.loads(res.text)
                res = resJson['res']
                if res == 1:
                    self.VALID_ACCESS_KEY = accessKey
                    self.URL_BASE = self.decodeMainUrl(accessKey)
                    print("You are logged "+str(chr(0x2713)))
                else:
                    printError()
            else:
                printError()
        except:
            printError()
        
    def authenticateAPI(self, accessKey):
        self.VALID_ACCESS_KEY = accessKey
        self.URL_BASE = self.decodeMainUrl(accessKey)

    def decodeMainUrl(self, accessKey):
        return self.decodeFunc(self.decodeFunc(accessKey).split('__sq__')[0])

    def decodeb64(self, thisStr):
        return base64.b64decode(thisStr).decode('utf-8')
        
    def decodeFunc(self, thisStr):
        return self.decodeb64(self.decodeb64(self.decodeb64(thisStr)))

    def getDBAuthFunc(self):
        try:
            currentDirPath = os.path.dirname(os.path.abspath(__file__))
            currentDirPath = os.path.dirname(currentDirPath)
            currentDirPath = os.path.dirname(currentDirPath)
            currentDirPath = os.path.dirname(currentDirPath)
            currentDirPath = os.path.dirname(currentDirPath)
            dbPath = currentDirPath+'\desktop.sqlite3'
            conn = sqlite3.connect(dbPath)  
            data  = conn.execute("SELECT * FROM config").fetchall()
            nbRow = len(data)
            conn.close()
            if nbRow > 0:
                return self.decodeMainUrl(data[-1][0]), base64.b64decode(data[-1][1]).decode('utf-8')
            else:
                return None
        except:
            return None

    def sendRequests(self, funcName, *args):
        if self.URL_BASE is None or self.VALID_ACCESS_KEY is None:
            print("Authentication failed. You may need to re-import the SpartaQuant module")

        thisUrl = self.URL_BASE+"jupyterAPI"
        newJson = dict()
        argsSerialized = []
        for thisArg in args:
            data_bin = pickle.dumps(thisArg)
            serializedObj = str(base64.b64encode(data_bin), "utf-8")
            argsSerialized.append(serializedObj)
        
        newJson['jsonData'] = json.dumps({
            'accessKey': self.VALID_ACCESS_KEY,
            'funcName': funcName,
            'args': argsSerialized
        })
        newJsonB = json.dumps(newJson)
        res = requests.post(thisUrl, data=newJsonB, verify=False)
        resJson = json.loads(res.text)
        if int(resJson['res']) == 1:
            return pickle.loads(base64.b64decode(resJson['serializedObj']))
        else:
            print("Could not proceed the request")
            return {'res': -1}

    def getUUID(self):
        funcName = str(inspect.stack()[0][0].f_code.co_name)
        return self.sendRequests(funcName)

    def getDataDB(self):
        funcName = str(inspect.stack()[0][0].f_code.co_name)
        return self.sendRequests(funcName)

    def getData(self, apiId, dispoDate=None):
        funcName = str(inspect.stack()[0][0].f_code.co_name)
        return self.sendRequests(funcName, apiId, dispoDate)

    def getDispoDates(self, apiId):
        funcName = str(inspect.stack()[0][0].f_code.co_name)
        return self.sendRequests(funcName, apiId)

    def getDataDates(self, thisDates, formula, bBusiness=True, formatDate='%Y%m%d'):
        funcName = str(inspect.stack()[0][0].f_code.co_name)
        return self.sendRequests(funcName, thisDates, formula, bBusiness, formatDate)

    def getDates(self, startDate, endDate, freq='b', bBusiness=True, orderBased='desc', formatDate='%Y%m%d'):
        funcName = str(inspect.stack()[0][0].f_code.co_name)
        return self.sendRequests(funcName, startDate, endDate, freq, bBusiness, orderBased, formatDate)

    def getFunctionsDB(self):
        funcName = str(inspect.stack()[0][0].f_code.co_name)
        return self.sendRequests(funcName)

    def getMTD(self, thisDate=None, formatDate="%Y%m%d"):
        funcName = str(inspect.stack()[0][0].f_code.co_name)
        return self.sendRequests(funcName, thisDate, formatDate)

    def getQTD(self, thisDate=None, formatDate="%Y%m%d"):
        funcName = str(inspect.stack()[0][0].f_code.co_name)
        return self.sendRequests(funcName, thisDate, formatDate)

    def getYTD(self, thisDate=None, formatDate="%Y%m%d"):
        funcName = str(inspect.stack()[0][0].f_code.co_name)
        return self.sendRequests(funcName, thisDate, formatDate)

    def putExec(self, str2Eval, name):
        funcName = str(inspect.stack()[0][0].f_code.co_name)
        return self.sendRequests(funcName, str2Eval, name)

    def runFunction(self, functionName, *args):
        funcName = str(inspect.stack()[0][0].f_code.co_name)
        return self.sendRequests(funcName, functionName, *args)

    def createFunction(self, functionObj):
        functionSource = inspect.getsource(functionObj)
        funcName = str(inspect.stack()[0][0].f_code.co_name)
        return self.sendRequests(funcName, functionSource)

    def updateFunction(self, functionName2Create, functionObj):
        functionSource = inspect.getsource(functionObj)
        funcName = str(inspect.stack()[0][0].f_code.co_name)
        return self.sendRequests(funcName, functionName2Create, functionSource)

    def putXlsData(self, xlsId, data_df, sheetName, cellStart='A1'):
        funcName = str(inspect.stack()[0][0].f_code.co_name)
        return self.sendRequests(funcName, xlsId, data_df, sheetName, cellStart)

    def createXls(self, nameFile, extension='xlsx'):
        funcName = str(inspect.stack()[0][0].f_code.co_name)
        return self.sendRequests(funcName, nameFile, extension)

    def getXlsDB(self):
        funcName = str(inspect.stack()[0][0].f_code.co_name)
        return self.sendRequests(funcName)

    def getXlsData(self, xlsId, sheetName=None, formula=None, dispoDate=None):
        funcName = str(inspect.stack()[0][0].f_code.co_name)
        return self.sendRequests(funcName, xlsId, sheetName, formula, dispoDate)

    def getXlsDispoDates(self, xlsId):
        funcName = str(inspect.stack()[0][0].f_code.co_name)
        return self.sendRequests(funcName, xlsId)

    def getXlsData(self, xlsId, sheetName=None, formula=None, dispoDate=None):
        funcName = str(inspect.stack()[0][0].f_code.co_name)
        return self.sendRequests(funcName, xlsId, sheetName, formula)

    def getExternalDB(self):
        funcName = str(inspect.stack()[0][0].f_code.co_name)
        return self.sendRequests(funcName)

    def getExternalData(self, authDBId, tableName=None, formula=None):
        funcName = str(inspect.stack()[0][0].f_code.co_name)
        return self.sendRequests(funcName, authDBId, tableName, formula)

    def putExternalData(self, authDBId, tableName, formula):
        funcName = str(inspect.stack()[0][0].f_code.co_name)
        return self.sendRequests(funcName, authDBId, tableName, formula)

    def testFunction(self, functionObj, *args):
        print("test function")
        print("args")
        print(len(args))
        print(args)
        try:
            functionObj.__call__(args)
        except Exception as e:
            print("Error")
            print(e)
        # functionSource = inspect.getsource(functionObj)
        # funcName = str(inspect.stack()[0][0].f_code.co_name)
        return "Function tested"
   