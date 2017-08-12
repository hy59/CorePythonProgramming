# -*- coding: utf-8 -*-

# use smtplib to send email
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from subprocess import check_output


def SendMail(self):
    reciver = '11111@qq.com' # 第三方 SMTP 服务
    mail_host = 'smtp.qq.com' # 设置服务器
    mail_user = '11111@qq.com' # 用户名
    mail_pass = '' # 口令， QQ邮箱是输入授权码，在QQ邮箱设置里用验证过的手机发送短信获得，不含空格
    sender = mail_user
    recivers = [reciver] # 接收邮件， 可设置为你的QQ邮箱或其他邮箱

    message = MIMEText('Hello')
    message['From'] = Header(mail_user, 'utf-8')
    message['To'] = Header(str(recivers), 'utf-8')

    subject = 'my test'
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, recivers, message.as_string())
        smtpObj.quit()
        print('邮件发送成功！')
    except smtplib.SMTPException as e:
        print(e)


