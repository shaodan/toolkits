# coding=utf-8

import json
import requests
import datetime
import smtplib
from email.mime.text import MIMEText
# from email.mime.image import MIMEImage
# from email.mime.multipart import MIMEMultipart


token = 'ef82a23cbf461f51c12374a3474023fe12589708'
to_list=['recv_mail_address']
mail_host="smtp.gmail.com"
mail_user="your_username"
mail_pass="your_password"
mail_postfix="gmail.com"

health_table = [
    (50, 'Good', '009966'),
    (100, 'Moderate', 'ffde33'),
    (150, 'Unhealthy for Sensitive Groups', 'ff9933'),
    (200, 'Unhealthy', 'cc0033'),
    (300, 'Very Unhealthy', '660099'),
    (300, 'Hazardous', '7e0023')
]

def get_city(city='beijing'):
    res = requests.get('http://api.waqi.info/feed/%s/?token=%s' % (city, token)).text
    content = json.loads(res)
    if content['status'] == 'ok':
        data = content['data']
        aqi = int(data['aqi'])              # 空气指数，主要污染物的指标
        dominentpol = data['dominentpol']   # 主要污染物
        time = data['time']['s']            # 更新时间
        city_id = data['idx']               # 城市编号，北京1451
        allp = data['iaqi']                 # 详细指标
        for health in health_table:
            if aqi < health[0]:
                break
        content = '<html><table style="width:600px;color:rgb(237, 224, 243);text-align:center;background-color:#' + health[2]+\
            ';text-shadow:rgb(0,0,0) 1px 0px 1px;" cellpadding="0" cellspacing="0"><tr style="height:80px;"><td style="width:66%;font-size:36px;font-weight:bold;">'+health[1]+\
            '</td><td style="width:33%;font-size:28px;">'+str(aqi)+'</td></tr></table></html>'
        subject = '[AqiReport] '+ time[:-3] +' ['+dominentpol+'] '+str(aqi)
        return subject, content
    else:
        return 'Api error', cotent['data']

def send_email(subject, content):
    msg = MIMEText(content, 'html', 'utf-8')
    me = "Aqi<"+mail_user+"@"+mail_postfix+">"
    msg['Subject'] = subject
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        # server.connect(mail_host)
        server.login(mail_user, mail_pass)
        server.sendmail(me, to_list, msg.as_string())
        server.close()
        return True
    except Exception, e:
        print str(e)
        return False


def simple_feed():
    data = json.loads(('http://feed.aqicn.org/xservices/refresh:1451?').text)
    aqiv = data['aqiv']


if __name__ == '__main__':
    subject, content = get_city('beijing')
    print subject
    print content
    send_email(subject, content)
