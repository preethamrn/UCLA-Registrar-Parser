# NOTE: this version doesn't work anymore!!!

import os

from lxml import html
import requests

page = requests.get('http://www.registrar.ucla.edu/schedule/detselect.aspx?termsel=16W&subareasel=PHYSICS&idxcrs=0001B')
tree = html.fromstring(page.content)
enroll_total = (tree.xpath('//span[@id="ctl00_BodyContentPlaceHolder_detselect_ctl02_ctl02_EnrollTotal"]//span[@class="bold"]/text()'))[0]
enroll_cap = (tree.xpath('//span[@id="ctl00_BodyContentPlaceHolder_detselect_ctl02_ctl02_EnrollCap"]//span[@class="bold"]/text()'))[0]

if(enroll_total < enroll_cap):
	#make the window persistent
	print "LET\'S GO!!!"
	os.system("pause")


"""
#Failed attempt at sending email :(
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

gmail_user = "preetham.in.1997@gmail.com"
#gmail_pwd = "password" #change this line
TO = 'preetham.in.1997@gmail.com'
SUBJECT = "Testing sending using gmail"
TEXT = "Testing sending mail using gmail servers"
server = smtplib.SMTP_SSL('smtp.gmail.com:465')
server.login(gmail_user, gmail_pwd)
BODY = '\r\n'.join(['To: %s' % TO,
        'From: %s' % gmail_user,
        'Subject: %s' % SUBJECT,
        '', TEXT])

server.sendmail(gmail_user, TO, BODY)
server.quit()
"""