import requests
import schedule
import time
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.header import Header

def weather_spider():
    url = 'http://www.weather.com.cn/weather/101020100.shtml'
    res = requests.get(url)
    res.encoding = 'utf-8'
    data = BeautifulSoup(res.text, 'html.parser')
    wea = data.find('p', class_='wea').text
    tem = data.find(class_='tem').text
    return wea,tem

# 连接服务器，登陆邮箱
def send_mail(wea,tem):
    mainhost = 'smtp.qq.com'
    qq_mail = smtplib.SMTP()
    account = '1024013820@qq.com'
    password = 'mbkqgpbbpebbbcib'
    qq_mail.connect(mainhost,25)
    qq_mail.login(account,password)

    reciever = '1024013820@qq.com'

    # 编写邮件
    content = '今天的天气是'+ wea + '\n' + '温度是' + tem
    message = MIMEText(content,'plain','utf-8')
    subject = '今日天气'
    message['Subject'] = Header(subject,'utf-8')

    # 发送邮件
    try:
        qq_mail.sendmail(account,reciever,message.as_string())
        print('邮件发送成功！')
    except:
        print('邮件发送失败！')
        qq_mail.quit()

def job():
    print('开始一次任务')
    tem,wea = weather_spider()
    send_mail(tem,wea)
    print('任务完成')

schedule.every().day.at('07:30').do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

