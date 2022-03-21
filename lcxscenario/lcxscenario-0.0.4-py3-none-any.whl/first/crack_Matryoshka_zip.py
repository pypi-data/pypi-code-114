import zipfile
import re
zipname = "C:\\Users\\11502\\Desktop\\"+"11549.zip"
while True:
    if zipname != "C:\\Users\\11502\\Desktop\\Cattle.jpg":
        ts1 = zipfile.ZipFile(zipname)
        #print ts1.namelist()[0]
        res = re.search('[0-9]*',ts1.namelist()[0])
        print (res.group())
        passwd = res.group()
        ts1.extractall("C:\\Users\\11502\\Desktop\\",pwd=passwd)
        zipname = "C:\\Users\\11502\\Desktop"+ts1.namelist()[0]
    else:
        print ("find")

