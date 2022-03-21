#!/usr/bin/env python3
# coding = utf8
"""
@ Author : ZeroSeeker
@ e-mail : zeroseeker@foxmail.com
@ GitHub : https://github.com/ZeroSeeker
@ Gitee : https://gitee.com/ZeroSeeker
"""
from email.mime.text import MIMEText
import smtplib
import envx


def make_con_info(
        env_file_name: str = 'mail.env'
):
    # ---------------- 固定设置 ----------------
    inner_env = envx.read(file_name=env_file_name)
    con_info = {
        "from_name": inner_env.get('from_name'),
        "smtp_host": inner_env.get('smtp_host'),
        "smtp_port": inner_env.get('smtp_port'),
        "smtp_username": inner_env.get('smtp_username'),
        "smtp_password": inner_env.get('smtp_password'),
        "ssl": inner_env.get('ssl'),
    }
    # ---------------- 固定设置 ----------------
    return con_info


class Basic:
    def __init__(
            self,
            from_name: str = None,
            smtp_host: str = None,
            smtp_port: int = None,
            smtp_username: str = None,
            smtp_password: str = None,
            ssl: bool = None,
            con_info: dict = None
    ):
        """
        初始化
        :param from_name: 发信人
        :param smtp_host: 发信域名
        :param smtp_port: SMTP服务端口号：25或80或465(SSL加密)
        :param smtp_username: 发信邮箱
        :param smtp_password: 发信密钥
        :param ssl: 是否对发信过程使用加密
        :param con_info: 配置信息
        """
        print(con_info)
        if smtp_host is None:
            self.smtp_host = con_info.get('smtp_host')
        else:
            self.smtp_host = smtp_host

        if smtp_port is None:
            self.smtp_port = con_info.get('smtp_port')
        else:
            self.smtp_port = smtp_port

        if smtp_username is None:
            self.smtp_username = con_info.get('smtp_username')
        else:
            self.smtp_username = smtp_username

        if smtp_password is None:
            self.smtp_password = con_info.get('smtp_password')
        else:
            self.smtp_password = smtp_password

        if from_name is None:
            self.from_name = con_info.get('from_name', self.smtp_username)
        else:
            self.from_name = from_name

        if ssl is None:
            self.ssl = con_info.get('ssl', True)
        else:
            self.ssl = ssl

        # self.server = smtplib.SMTP()
        # self.server.connect(self.smtp_host, self.smtp_port)

        if self.ssl is True:
            self.server = smtplib.SMTP_SSL(
                host=smtp_host,
                port=smtp_port
            )  # 传输过程加密
        else:
            self.server = smtplib.SMTP(
                host=smtp_host,
                port=smtp_port
            )  # 传输过程不加密
        self.server.connect(
            host=self.smtp_host,
            port=self.smtp_port
        )
        self.server.login(
            user=self.smtp_username,
            password=self.smtp_password
        )

    def send_text(
            self,
            sub: str = None,
            content: str = None,
            to_addrs: list = None,  # 收信人，如果为空，就会给自己发
            from_name: str = None
    ):
        if sub is None:
            sub = 'sub'
        if content is None:
            content = 'content'
        msg = MIMEText(
            _text=content,
            _subtype='plain'
        )
        msg['Subject'] = sub  # 标题
        if from_name is None:
            msg['From'] = "%s<%s>" % (self.from_name, self.smtp_username)  # 发信人信息
        else:
            msg['From'] = "%s<%s>" % (from_name, self.smtp_username)  # 发信人信息

        if to_addrs is None:
            local_to_addrs = [self.smtp_username]
        else:
            local_to_addrs = to_addrs
        res = self.server.sendmail(
            from_addr=self.smtp_username,
            to_addrs=local_to_addrs,
            msg=msg.as_string()
        )
        return res


def send_text(
        sub: str = None,  # 标题
        content: str = None,  # 内容
        to_addrs: list = None,  # 收件人列表
        con_info: dict = None,
        env_file_name: str = 'mail.env',  # 环境文件
):
    # ---------------- 固定设置 ----------------
    if con_info is None:
        con_info = make_con_info(env_file_name=env_file_name)
    else:
        pass
    # ---------------- 固定设置 ----------------
    basics = Basic(con_info=con_info)
    res = basics.send_text(
        to_addrs=to_addrs,
        sub=sub,
        content=content,
    )
    return res
