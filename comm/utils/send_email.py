import smtplib
from email.mime.text import MIMEText  # 引入smtplib和MIMEText
from setting import EMAIL_CONFIG

class Send_Email():

    def send_email(self):
        email_config=EMAIL_CONFIG
        host = email_config['host']  # 设置发件服务器地址
        port = email_config['port']  # 设置发件服务器端口号。注意，这里有SSL和非SSL两种形式
        sender = email_config['sender']  # 设置发件邮箱，一定要自己注册的邮箱
        pwd = email_config['pwd']  # 设置发件邮箱的密码，等会登陆会用到
        receiver = email_config['receiver']  # 设置邮件接收人，可以是扣扣邮箱
        files=email_config['files']
        body = '<h1>Hi</h1><p>test</p>'  # 设置邮件正文，这里是支持HTML的

        msg = MIMEText(body, 'html')  # 设置正文为符合邮件格式的HTML内容
        msg['subject'] = 'Test Report'  # 设置邮件标题
        msg['from'] = sender  # 设置发送人
        msg['to'] = receiver  # 设置接收人

        att = MIMEText(open(files, 'rb').read(), 'base64', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        att["Content-Disposition"] = 'attachment; filename="report.html"'
        msg.attach(att)

        try:
            s = smtplib.SMTP(host, port)  # 注意！如果是使用SSL端口，这里就要改为SMTP_SSL
            s.login(sender, pwd)  # 登陆邮箱
            s.sendmail(sender, receiver, msg.as_string())  # 发送邮件！
            print('Done')
            s.quit()
        except smtplib.SMTPException:
            print('Error')


if __name__ == '__main__':
    email = Send_Email()
    email.send_email()