import sys, smtplib, os
import time
from HTMLTestRunner import HTMLTestRunner
import unittest
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
sys.path.append('./interface')


# ===========定义发送邮件==============
def send_mail(file_new):
    """
    :param file_new:最新的测试报告文件
    :return: 正文+附件的形式发送测试报告邮件
    """
    # 发送邮箱
    sender = 'xxxx@163.com'
    # 接收邮箱
    receiver = 'xxx@163.com,xxx@163.com'
    # 发送邮件主题
    subject = '话题接口回归测试用例报告'
    # 发送邮箱服务器
    smtpserver = 'smtp.163.com'
    # 发送邮箱用户／密码
    username = 'xxxx@163.com'
    password = 'a123456'

    # 获取报告文件
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()

    msg = MIMEMultipart()
    # 邮件标题
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = sender
    msg['To'] = receiver
    # 邮件内容
    text = MIMEText(mail_body, _subtype='html', _charset='utf-8')
    msg.attach(text)

    # 发送附件
    att = MIMEApplication(open(file_new, 'rb').read())
    att['Content-Type'] = 'application/octet-stream'
    att.add_header('Content-Disposition', 'attachment', filename=('utf-8', '', file_new))
    msg.attach(att)

    # 连接SMTP服务器
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(username, password)
    smtp.sendmail(sender, receiver.split('.'), msg.as_string())
    smtp.quit()
    print('email has send out !')


# =====查找测试报告目录，找到最新生成的测试报告文件=====
def new_report(report_path):
    """
    :param report_path:报告卢靖
    :return:返回最新的测试报告文件
    """
    lists = os.listdir(report_path)
    lists.sort(key=lambda fn: os.path.getmtime(report_path + "/" + fn))
    new_report_file = os.path.join(report_path, lists[-1])  # 找到最新生成的文件
    print(new_report_file)
    return new_report_file


if __name__ == '__main__':

    test_dir = './interface'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='*_test.py')

    now = time.strftime("%Y-%m-%d_%H_%M_%S")
    filename = './report/' + now + '_topic_result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                   title='Topic Interface Test',
                   description='用例执行结果如下:')
    runner.run(discover)
    fp.close()
    # 执行发送邮件操作
    file_path = new_report('./report/')
    send_mail(file_path)



