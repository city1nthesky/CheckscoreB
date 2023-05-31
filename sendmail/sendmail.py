# -*- coding: utf-8 -*-#
# filename: sendmail.py

import time
import yagmail


#开启SMTP服务
#qq邮箱 1设置 2账户 3开启 4生成授权码
#这点很关键，别忘了去开启SMTP，否则邮件是无法发送成功的。然后你还需要点击下面生成授权码，这个授权码才是使用Python发送邮件时的真正密码。
#http://www.icodebang.com/article/318568.html

class Mail:
    """
    邮件相关类
    """

    def log(self, content):
        now_time = time.strftime(
            "%Y-%m-%d %H:%M:%S", time.localtime()
        )
        print(f'{now_time}: {content}')

    def sendmail(self, msg, title, receivers):
        """
        发送邮件
        
        Arguments:
            msg {str} -- 邮件正文
            title {str} -- 邮件标题
            receivers {list} -- 邮件接收者，数组
        """

        yag = yagmail.SMTP(
            host='smtp.qq.com', user='city_in_the_sky@qq.com',
            password='pfchxpnyfctlbbbe', smtp_ssl=True
        )

        try:
            yag.send(receivers, title, msg)
            #self.log("邮件发送成功")

        except BaseException as e:
            print (e)
            #self.log("Error: 无法发送邮件")
