# coding:utf-8


from nntool.tools import Tool

# 实例化
tool = Tool()
tool.mail_from_user = 'tech-tm-qa@pin-dao.cn'
tool.mail_from_user_pwd = 'Tm-qa-888888'
tool.mail_from_host = 'smtp.mxhichina.com'

tool.send_mail_msg(to_user='quanningning@pin-dao.cn', subject='测试邮件', content='测试内容')

