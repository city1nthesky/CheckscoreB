# -*- coding: UTF-8 -*-
# filename: myrequest.py

import requests
from bs4 import BeautifulSoup
#import time
#from sendmail import Mail

#import smtplib
#from email.mime.text import MIMEText
#from email.header import Header

def getHTMLText(url):
    try:
        kv = {'User-agent':'Mozilla/5.0'}
        r = requests.get(url, timeout=30, headers=kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def getuserid(url):
    uText = ""
    html = getHTMLText(url)

    return html
