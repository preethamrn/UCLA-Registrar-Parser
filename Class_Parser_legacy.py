"""
TODO:
Check waitlist status
Make the check_status function more robust instead of just doing a substring search
Send email notification when class opens
"""

# Usage:
# Replace the classes in the classes list with any class you want to search.
# Change the quarter to the quarter you want the search.
# NOTE: The class name must be the exact short form listed on the registrar.


import os

import re

from bs4 import BeautifulSoup
import urllib

# Example: This checks the classes COM SCI M117, COM SCI 131, and COM SCI 174A for the 17W quarter
classes = ['COM SCI M117', 'COM SCI 131', 'COM SCI 174A']
quarter = '17W'

def get_class(class_name):
	subject = '+'.join(class_name.split(' ')[:-1])
	final = class_name.split(' ')[-1]
	number = ''.join(re.findall(r'[0-9]+', final))
	first = ''.join(re.findall(r'^[A-Z]+', final))
	last = ''.join(re.findall(r'[A-Z]+$', final))
	
	number = '0'*(4-len(number))+number
	first = first + '+'*(2-len(first))
	last = last + '+'*(2-len(last))
	number = number+last+first
	return (subject, number)


class_found_flag = False

for course in classes:
	(subject, number) = get_class(course)
	URL = 'http://legacy.registrar.ucla.edu/schedule/detselect.aspx?termsel={0}&subareasel={1}&idxcrs={2}'.format(quarter, subject, number)
	soup = BeautifulSoup(urllib.urlopen(URL))
	
	lectures = soup.find_all('tr', {'class','dgdClassDataHeader'})
	
	for lecture in lectures:
		class_status = lecture.nextSibling
		capacity = int(class_status.find('td', {'class', 'dgdClassDataEnrollCap'}).text)
		enrolled = int(class_status.find('td', {'class', 'dgdClassDataEnrollTotal'}).text)
		if enrolled < capacity:
			class_found_flag = True
			print course


if class_found_flag:
	os.system("pause")


"""
#Failed attempt at sending email :(
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

gmail_user = "email@abc.com" #change this line
#gmail_pwd = "password" #change this line
TO = 'email@abc.com'
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