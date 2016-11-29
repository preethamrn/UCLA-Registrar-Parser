"""
TODO:
Check waitlist status
Make the check_status function more robust instead of just doing a substring search
Send email notification when class opens
"""

# Usage:
# Replace the classes in the classes list with any class you want to search and the lecture number (0 for any lecture).
# Change the quarter to the quarter you want the search.
# NOTE: The class name must be the exact short form listed on the registrar.


import os # pausing the command prompt

import re # parse the input string using regex

# parse the registrar website
from bs4 import BeautifulSoup
import urllib

# Example: This checks the classes COM SCI 174A (any lecture) and STATS 10 (LEC 2) for the 17W quarter
classes = [('COM SCI 174A', 0), ('STATS 10', 5)]
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

def check_lecture(lecture):
	class_status = lecture.nextSibling
	capacity = int(class_status.find('td', {'class', 'dgdClassDataEnrollCap'}).text)
	enrolled = int(class_status.find('td', {'class', 'dgdClassDataEnrollTotal'}).text)
	wait_capacity = int(class_status.find('td', {'class', 'dgdClassDataWaitListCap'}).text)
	wait_enrolled = int(class_status.find('td', {'class', 'dgdClassDataWaitListTotal'}).text)
	if enrolled < capacity:
		class_found_flag = True
		print course
	elif wait_enrolled < wait_capacity:
		class_found_flag = True
		print course + ": Wait"

class_found_flag = False

for course, lec in classes:
	(subject, number) = get_class(course)
	URL = 'http://legacy.registrar.ucla.edu/schedule/detselect.aspx?termsel={0}&subareasel={1}&idxcrs={2}'.format(quarter, subject, number)
	soup = BeautifulSoup(urllib.urlopen(URL))
	
	lectures = soup.find_all('tr', {'class','dgdClassDataHeader'})
	
	if lec == 0:
		for lecture in lectures:
			check_lecture(lecture)
	else:
		try:
			check_lecture(lectures[lec-1])
		except IndexError:
			print "Error: lecture number is out of range"


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