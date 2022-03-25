import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from commonchi.lib.newReport import new_report
from time import sleep

# cxx增加   2022.1.22修改
# 定义发送邮件
#def send_mail(new_report_html,new_report_xls,product_name,receiver,sender,username,password,smtpserver,port):
def send_mail(path_xls,path_html,cf,receiver=['cuixiaoxia@chinasofti.com']):
    product_name = cf.get("product_name", "product_name")
    username = cf.get("email","username")  # 发件箱用户名
    password = cf.get("email","password")  # 发件箱密码
    sender = cf.get("email","user")  # 发件人邮箱
    smtpserver = cf.get("email","host_server")  # 发件服务器
    port = cf.get("email","port")  # 端口
    new_report_html = new_report(path_html)
    new_report_xls = new_report(path_xls)

    # 编辑邮件的内容
    #读文件
    f = open(new_report_html, 'rb')  #xml
    mail_body = f.read()
    mail_bod_2 = open(new_report_xls, 'rb').read()  #xlsx
    f.close()
    # 邮件正文是MIMEText
    body = MIMEText(mail_body, 'html', 'utf-8')
    # 邮件对象
    #msg = MIMEMultipart() #-----------
    msg = MIMEMultipart()   #采用related定义内嵌资源的邮件体
    msg['Subject'] = Header(product_name+"自动化测试报告", 'utf-8').encode()#主题
    msg['From'] = Header(u'API自动化 <%s>'%sender)                #发件人
    #msg['To'] = Header(u'test测试发送 <%s>'%receiver)            #收件人
    msg['To'] = ','.join(receiver)
    msg['date'] = time.strftime("%a,%d %b %Y %H:%M:%S %z")
    msg.attach(body)
    # 附件1
    att = MIMEText(mail_body, "base64", "utf-8")
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = 'attachment; filename="test_report.html"'  #filename是附件的重新命名
    msg.attach(att)

    #附件2

    att_2 = MIMEText(mail_bod_2, "base64", "utf-8")
    att_2["Content-Type"] = "application/octet-stream"
    att_2["Content-Disposition"] = 'attachment; filename="report.xlsx"'  #filename是附件的重新命名
    msg.attach(att_2)

    # 发送邮件
    try:
        smtp = smtplib.SMTP()    #若163邮箱非SSL,公司邮箱也用这个
        #smtp.set_debuglevel(1)
        smtp.connect(smtpserver)  # 连服务器
        smtp.login(username, password)
    except:
        smtp = smtplib.SMTP_SSL(smtpserver, port)  #如QQ邮件，SSL
        smtp.login(username, password)  # 登录
    smtp.sendmail(sender, msg['To'].split(','), msg.as_string())  # 发送  msg['To'].split(',')可以实现多人发送
    smtp.quit()
    print("邮件已发出！注意查收。")
    sleep(2)






# #!/usr/bin/env python
# # _*_ coding:utf-8 _*_
# __author__ = 'JACK'
#
# import os, sys
#
# sys.path.append(os.path.dirname(os.path.dirname(__file__)))
# from cases.ussm import setting
# import smtplib
# from common.lib.newReport import new_report
# import configparser
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
#
#
# def send_mail(file_new):
#     """
#     定义发送邮件
#     :param file_new:
#     :return: 成功：打印发送邮箱成功；失败：返回失败信息
#     """
#     f = open(file_new, 'rb')
#     mail_body = f.read()
#     f.close()
#     # 发送附件
#     con = configparser.ConfigParser()
#     con.read(setting.TEST_CONFIG, encoding='utf-8')
#     report = new_report(setting.TEST_REPORT)
#     sendfile = open(report, 'rb').read()
#     # --------- 读取config.ini配置文件 ---------------
#     HOST = con.get("user", "HOST_SERVER")
#     SENDER = con.get("user", "FROM")
#     RECEIVER = con.get("user", "TO")
#     USER = con.get("user", "user")
#     PWD = con.get("user", "password")
#     SUBJECT = con.get("user", "SUBJECT")
#
#     att = MIMEText(sendfile, 'base64', 'utf-8')
#     att["Content-Type"] = 'application/octet-stream'
#     att.add_header("Content-Disposition", "attachment", filename=("gbk", "", report))
#
#     msg = MIMEMultipart('related')
#     msg.attach(att)
#     msgtext = MIMEText(mail_body, 'html', 'utf-8')
#     msg.attach(msgtext)
#     msg['Subject'] = SUBJECT
#     msg['from'] = SENDER
#     msg['to'] = RECEIVER
#
#     try:
#         server = smtplib.SMTP()
#         server.connect(HOST)
#         server.starttls()
#         server.login(USER, PWD)
#         server.sendmail(SENDER, RECEIVER, msg.as_string())
#         server.quit()
#         print("邮件发送成功！")
#     except Exception as  e:
#         print("失败: " + str(e))
