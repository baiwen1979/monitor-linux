# coding = utf-8

"""
@author: baiwen1979

@file: mail_sender.py

@time: 2020/07/30 16:55

@desc: 发送邮件模块

"""

import smtplib
from email.header import Header
from email.mime.text import MIMEText

from config import gconfig


class MailSender(object):
    def __init__(self):
        """ 初始化邮箱模块 """
        try:
            self.mail_host = gconfig.get_value("mail_host")  # 邮箱服务器
            self.mail_port = gconfig.get_value("mail_port")  # 邮箱服务端端口
            self.mail_user = gconfig.get_value("mail_user")  # 邮箱用户名
            self.mail_pwd = gconfig.get_value("mail_pwd")  # 邮箱密码
            self.mail_receivers = gconfig.get_value("mail_receivers").split(',')  # 收件人,以逗号分隔成列表
            smtp = smtplib.SMTP()
            smtp.connect(self.mail_host, self.mail_port)
            smtp.login(self.mail_user, self.mail_pwd)
            self.smtp = smtp
        except:
            print('发邮件---->初始化失败!请检查用户名和密码是否正确!')

    def send(self, content):
        """ 发送邮件 """
        try:
            message = MIMEText(content, 'plain', 'utf-8')
            message['From'] = Header("巡检机器人小白", 'utf-8')
            message['To'] = Header("系统警告", 'utf-8')
            subject = '各系统巡检信息'
            message['Subject'] = Header(subject, 'utf-8')
            self.smtp.sendmail(self.mail_user, self.mail_receivers, message.as_string())
            print('发送邮件成功!')
        except Exception as e:
            print('发邮件---->失败!原因:', e)

    def close(self):
        """ 关闭邮箱资源 """
        self.smtp.close()
