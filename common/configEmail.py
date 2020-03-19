# -*- coding: utf-8 -*-
# @Time    : 2020/3/6 13:32
# @Author  : Mysunshine
# @File    : configEmail.py
# 这个文件是主要配置发送邮件的主题，正文等，将测试报告发送并抄送到相关人邮箱的逻辑

import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import base64


class SendMail(object):
    # 初始化函数，创建对象时，类一定要传入这些参数
    def __init__(self, username, passwd, recv, title, content,
                 file=None, ssl=False,
                 email_host='smtp.qq.com', port=25, ssl_port=465):
        """

        :param username:用户名
        :param passwd:密码
        :param recv:收件人，多个收件人要写成list['a','b']
        :param title:邮件主题
        :param content:邮件内容
        :param file:附件路径，如果不在当前目录下，那么要写绝对路径，默认没有附件
        :param ssl:是否安全链接，默认为普通
        :param email_host:smtp服务器地址，默认为163服务器
        :param port:非安全链接端口，默认为25
        :param ssl_port:安全链接端口，默认为465
        """
        self.username = username
        self.passwd = passwd
        self.recv = recv
        self.title = title
        self.content = content
        self.file = file
        self.ssl = ssl
        self.email_host = email_host
        self.port = port
        self.ssl_port = ssl_port

    def send_mail(self):
        # 创建一个带有附件的实例
        msg = MIMEMultipart()
        # 处理附件
        if self.file:
            # 只取文件名，不取路径，os.path.split()作用是将路径和文件名称分开
            file_name = os.path.split(self.file)[-1]
            try:
                f = open(self.file, 'rb').read()

            except Exception as e:
                raise Exception('附件打不开！！', e)

            else:
                # 这个可以发送复杂的附件，比如附件为表格
                att = MIMEText(f, 'base64', 'utf-8')
                att["Content-Type"] = 'application/octet-stream'
                # 这行是把附件的格式进行一些处理，不知道为啥要这么写，但是如果不写接收到的附件已经不是表格样式了
                new_file_name = '=?utf-8?b?' + base64.b64encode(file_name.encode()).decode() + '?='
                # 这里是处理文件名为中文名的， 必须这么写
                att["Content-Disposition"] = 'attachment; filename="%s"' %(new_file_name)
                msg.attach(att)
        # 邮件正文
        msg.attach(MIMEText(self.content))
        # 邮件主题
        msg['Subject'] = self.title
        # 发件者
        msg['From'] = self.username
        # 收件者账号列表
        msg['To'] = ','.join(self.recv)
        # 如果安全链接端口为465，否则端口为25
        if self.ssl:
            self.smtp = smtplib.SMTP_SSL(self.email_host, port=self.ssl_port)
        else:
            self.smtp = smtplib.SMTP(self.email_host, port=self.port)
        # 登录邮箱
        self.smtp.login(self.username, self.passwd)
        try:
            # 参数分别是发送者，接收者，第三个是把上面的发送邮件的内容变成字符串
            self.smtp.sendmail(self.username, self.recv, msg.as_string())
            pass
        except Exception as e:
            print("出错了", e)

        else:
            print("发送成功！")
        self.smtp.quit()


if __name__ == "__main__":
    m = SendMail(
        username='2974835299@qq.com',
        # passwd是授权码
        passwd='jkpunzizckxkdfhg',
        recv=['3035386062@qq.com'],
        title='测试邮件',
        content='测试发送邮件',
        file=r'C:\\Users\\朱颖娇\\Desktop\\接口测试模板.xlsx',
        ssl=True,
    )
    m.send_mail()




