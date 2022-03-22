__author__ = "HSD, Hemant S Dhanwar"
__email__ = "ashuhemantsingh@gmail.com"
__status__ = "planning"

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
import pandas as pd
import getpass
import datetime

def get_pass(path_to_file):
    f = open(path_to_file, 'r')
    password = f.read()
    return password

def email_with_attachhment(username, path2key, mail_to, path):
    #username = "HemantDhanwar@lucidmotors.com"
    
    password = get_pass(path2key)
    mail_from = username
    #mail_from = "HemantDhanwar@lucidmotors.com"
    #mail_to = "kirankumarj@lucidmotors.com"
    mail_subject = "Disk Utilisation report"
    mail_body = "please check attachment"
    latest_date = datetime.datetime.now()
    current_time = datetime.datetime.now()
    latest_date = str(latest_date)
    latest_date = latest_date[0:10]
    latest_date=latest_date.split('-')
    #time_ = str(current_time)
    #time_ = current_time[11:16]
    filename = "/Output D-{}-{}-{} T.csv".format(latest_date[1], latest_date[2], latest_date[0])
    mail_attachment=path+filename
    mail_attachment_name=filename

    mimemsg = MIMEMultipart()
    mimemsg['From']=mail_from
    mimemsg['To']=mail_to
    mimemsg['Subject']=mail_subject
    mimemsg.attach(MIMEText(mail_body, 'plain'))

    with open(mail_attachment, "rb") as attachment:
        mimefile = MIMEBase('application', 'octet-stream')
        mimefile.set_payload((attachment).read())
        encoders.encode_base64(mimefile)
        mimefile.add_header('Content-Disposition', "attachment; filename= %s" % mail_attachment_name)
        mimemsg.attach(mimefile)
        connection = smtplib.SMTP(host='smtp.office365.com', port=587)
        connection.starttls()
        connection.login(username,password)
        connection.send_message(mimemsg)
        connection.quit()

def mail(From, path2key, to, msg='', subject = 'Test Subject'):
    username = From#"HemantDhanwar@lucidmotors.com"
    password = get_pass(path2key)
    #mail_from = "HemantDhanwar@lucidmotors.com"
    #mail_to = "kirankumarj@lucidmotors.com, tamilvannan@lucidmotors.com"
    #mail_subject = "Test Subject"
    mail_body = msg#"This is a test message"

    mimemsg = MIMEMultipart()
    mimemsg['From'] = From
    mimemsg['To'] = to
    mimemsg['Subject'] = subject
    mimemsg.attach(MIMEText(mail_body, 'plain'))
    connection = smtplib.SMTP(host='smtp.office365.com', port=587)
    connection.starttls()
    connection.login(username,password)
    connection.send_message(mimemsg)
    connection.quit()

def get_directory_size(directory):
    total = 0
    try:
        for i in os.scandir(directory):
            if i.is_file():
                total += i.stat().st_size
            elif i.is_dir():
                total += get_directory_size(i.path)
    except NotADirectoryError:
        return os.path.getsize(directory)
    except FileNotFoundError:
        return 0
    except PermissionError:
        return 0
    return total

def disk_usage(path, output_path, SAVE = True):
    #path = 'C:/'
    output = {}
    os.chdir(path)
    folder = os.listdir()
    dir_size = []
    #print(folder)
    #print()
    latest_date = datetime.datetime.now()
    current_time = datetime.datetime.now()
    latest_date = str(latest_date)
    latest_date = latest_date[0:10]
    latest_date=latest_date.split('-')
    #time_ = str(current_time)
    #time_ = current_time[11:16]
    filename = "/Output D-{}-{}-{} T.csv".format(latest_date[1], latest_date[2], latest_date[0])

    for i in folder:
        sz = get_directory_size(path+i)
        size_mb = sz/pow(2,20)
        if size_mb > 1000:
            gb = (sz/pow(2,20))/1024
            #print(i,':',gb,'Gb')
            #dir_size.append(sz/pow(2,20)))
            dir_size.append(str(round(gb,2))+'Gb')
        else:
            mb = sz/pow(2,20)
            #print(i,':',mb,'Mb')
            #dir_size.append(sz/pow(2,20)))
            dir_size.append(str(round(mb,2))+'Mb')
    output = {'Folder Names|':folder, '|Space occupied':dir_size, 'USER':getpass.getuser()}
    df = pd.DataFrame(output)
    print(df)
    if SAVE:
        
        if output_path.endswith('/') or output_path.endswith('\\'):
            df.to_csv(output_path+filename,index=False)
        else:
            df.to_csv(output_path+filename,index=False)
            
name ='''
            **   ** ****** **       **    **     **     **  **********
            **   ** **     ** *   * **  **  **   ** *   **      **
            ******* *****  **  * *  ** ********  **   * **      **
            **   ** **     **   *   ** **    **  **    ***      **
            **   ** ****** **       ** **    **  **     **      **
'''
def author():
    print(name)

if __name__=='__main__':
    print(name)
    #siz = get_directory_size('C:/')
    disk_usage("C:/", "D:/", SAVE = True)
    T_siz = 476
    #if T_siz - siz < 200:
    #email_with_attachhment('HemantDhanwar@lucidmotors.com', 'D:\\H_Work_SPACE\\key.txt', 'HemantDhanwar@lucidmotors.com,kirankumarj@lucidmotors.com, shravankumar@lucidmotors.com', 'D:\\')
