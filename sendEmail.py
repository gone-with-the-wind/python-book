# -*- coding: utf-8 -*-

# import os

# print([x for x in os.listdir('.')])


# 输入Email地址和口令:
# from_addr = input('From: ')
# password = input('Password: ')
# # 输入收件人地址:
# to_addr = input('To: ')
# # 输入SMTP服务器地址:
# smtp_server = input('SMTP server: ')

# from_addr = "spoil2012@foxmail.com"
# password = ""
# to_addr="491883290@qq.com"
# smtp_server="smtp.qq.com"

# import smtplib
# from email.mime.text import MIMEText
# msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')

# server = smtplib.SMTP_SSL()
# server.connect(smtp_server,465)
# # server = smtplib.SMTP(smtp_server, 465) # SMTP协议默认端口是25
# server.set_debuglevel(1)
# server.login(from_addr, password)
# server.sendmail(from_addr, [to_addr], msg.as_string())
# server.quit()


import smtplib
from email.mime.text import MIMEText

class SendEmail:
    global send_user
    global email_host
    global password
    password = ""
    email_host = "smtp.qq.com"
    send_user = "spoil2012@foxmail.com"

    def send_mail(self,user_list,sub,content):
        user = "shape" + "<" + send_user + ">"
        message = MIMEText(content,_subtype='plain',_charset='utf-8')
        message['Subject'] = sub
        message['From'] = user
        message['To'] = ";".join(user_list)
        server = smtplib.SMTP_SSL(host=email_host)
        server.connect(host=email_host, port=465)
        server.login(send_user,password)
        server.sendmail(user,user_list,message.as_string())
        server.close()

if __name__ == '__main__':
    send = SendEmail()
    user_list = ['491883290@qq.com']
    sub = "测试邮件"
    content = "测试看看"
    send.send_mail(user_list,sub,content)
























 



