class Head():
    def __init__(self,name,path,title):
        self.path=path
        self.name=name
        self.title=title
        f = open(path+"\\"+name, "w")
        f.write('<!DOCTYPE html>\n<html>\n    <head>\n        <meta charset="utf-8">\n		<title>'+title+'</title>')
        f.close()
        global a,b
        a=name
        b=path
class Bgimg():
    def __init__(self,path):
        self.path=path
        f = open(b+"\\"+a, "a")
        f.write('\n    <body background='+path+'></body>')
        f.close()
class HtmlPrint():
    def __init__(self,text,pack):
        self.pack=pack
        self.text=text
        if pack=="center":
            f = open(b+"\\"+a, "a")
            f.write("\n    <center>" + text + "</center>")
            f.close()
        else :
            f = open(b+"\\"+a, "a")
            f.write(text)
            f.close()
class HtmlPrints():
    def __init__(self,Fontsize,color,text,pack):
        self.size=Fontsize
        self.color=color
        self.text=text
        self.pack=pack
        f = open(b+"\\"+a, "a")
        f.write('\n    <h1 align="'+pack+'"<font color="'+color+'" size="'+Fontsize+'">'+text+'</font></h1>')
        f.close()
class texturl():
    def __init__(self,url,text):
        self.url=url
        self.text=text
        f = open(b+"\\"+a, "a")
        f.write('\n    <a href="'+url+'">'+text+'</a>')
class webStart():
    def __init__(self,port,py,allpath):
        self.py=py
        self.allpath=allpath
        self.port=port
        import os
        if py[0]=="3":
            os.system("cd "+allpath + " && python -m http.server " + port)
        else:
            os.system("cd" + allpath + " && python -m SimpleHTTPServer" + port)

def Tali():
    f = open(b+"\\"+a, "a")
    f.write('\n    </body>\n</html>')
    f.close()
class 打印():
    def __init__(self,text):
        self.text=text
        print(text)