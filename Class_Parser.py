"""
TODO:
Make easier to use (so you don't have to copy the entire URL link and can actually search for classes based on Course ID)
Check waitlist status
Make the check_status function more robust instead of just doing a substring search
Send email notification when class opens
"""

# Usage:
# Open Chrome dev console go to the Network tab
# Click on the class you want to search for and copy the GetCourseSummary URL and paste into the URLs list
# You will be notified when the class has Spots Left

import urllib
import os
from bs4 import BeautifulSoup

def check_status(class_status):
	return 'Spots Left' in class_status.text

# remove any URLs below and add your class URLs here. 
# For example: This currently checks COMSCI 111, 180, and 188 in 17W quarter.
URLs = ['https://sa.ucla.edu/ro/Public/SOC/Results/GetCourseSummary?model=%7B%22Term%22%3A%2217W%22%2C%22SubjectAreaCode%22%3A%22COM+SCI%22%2C%22CatalogNumber%22%3A%220111++++%22%2C%22IsRoot%22%3Atrue%2C%22SessionGroup%22%3A%22%25%22%2C%22ClassNumber%22%3A%22%25%22%2C%22SequenceNumber%22%3Anull%2C%22Path%22%3A%22COMSCI0111%22%2C%22MultiListedClassFlag%22%3A%22n%22%2C%22Token%22%3A%22MDExMSAgICBDT01TQ0kwMTEx%22%7D&FilterFlags=%7B%22enrollment_status%22%3A%22O%2CW%2CC%2CX%2CT%2CS%22%2C%22advanced%22%3A%22y%22%2C%22meet_days%22%3A%22M%2CT%2CW%2CR%2CF%22%2C%22start_time%22%3A%228%3A00+am%22%2C%22end_time%22%3A%226%3A00+pm%22%2C%22meet_locations%22%3Anull%2C%22meet_units%22%3Anull%2C%22instructor%22%3Anull%2C%22class_career%22%3Anull%2C%22impacted%22%3Anull%2C%22enrollment_restrictions%22%3Anull%2C%22enforced_requisites%22%3Anull%2C%22individual_studies%22%3Anull%2C%22summer_session%22%3Anull%7D&_=1479294508576','https://sa.ucla.edu/ro/Public/SOC/Results/GetCourseSummary?model=%7B%22Term%22%3A%2217W%22%2C%22SubjectAreaCode%22%3A%22COM+SCI%22%2C%22CatalogNumber%22%3A%220180++++%22%2C%22IsRoot%22%3Atrue%2C%22SessionGroup%22%3A%22%25%22%2C%22ClassNumber%22%3A%22%25%22%2C%22SequenceNumber%22%3Anull%2C%22Path%22%3A%22COMSCI0180%22%2C%22MultiListedClassFlag%22%3A%22n%22%2C%22Token%22%3A%22MDE4MCAgICBDT01TQ0kwMTgw%22%7D&FilterFlags=%7B%22enrollment_status%22%3A%22O%2CW%2CC%2CX%2CT%2CS%22%2C%22advanced%22%3A%22y%22%2C%22meet_days%22%3A%22M%2CT%2CW%2CR%2CF%22%2C%22start_time%22%3A%228%3A00+am%22%2C%22end_time%22%3A%226%3A00+pm%22%2C%22meet_locations%22%3Anull%2C%22meet_units%22%3Anull%2C%22instructor%22%3Anull%2C%22class_career%22%3Anull%2C%22impacted%22%3Anull%2C%22enrollment_restrictions%22%3Anull%2C%22enforced_requisites%22%3Anull%2C%22individual_studies%22%3Anull%2C%22summer_session%22%3Anull%7D&_=1479294590178','https://sa.ucla.edu/ro/Public/SOC/Results/GetCourseSummary?model=%7B%22Term%22%3A%2217W%22%2C%22SubjectAreaCode%22%3A%22COM+SCI%22%2C%22CatalogNumber%22%3A%220188++++%22%2C%22IsRoot%22%3Atrue%2C%22SessionGroup%22%3A%22%25%22%2C%22ClassNumber%22%3A%22%25%22%2C%22SequenceNumber%22%3Anull%2C%22Path%22%3A%22COMSCI0188%22%2C%22MultiListedClassFlag%22%3A%22n%22%2C%22Token%22%3A%22MDE4OCAgICBDT01TQ0kwMTg4%22%7D&FilterFlags=%7B%22enrollment_status%22%3A%22O%2CW%2CC%2CX%2CT%2CS%22%2C%22advanced%22%3A%22y%22%2C%22meet_days%22%3A%22M%2CT%2CW%2CR%2CF%22%2C%22start_time%22%3A%228%3A00+am%22%2C%22end_time%22%3A%226%3A00+pm%22%2C%22meet_locations%22%3Anull%2C%22meet_units%22%3Anull%2C%22instructor%22%3Anull%2C%22class_career%22%3Anull%2C%22impacted%22%3Anull%2C%22enrollment_restrictions%22%3Anull%2C%22enforced_requisites%22%3Anull%2C%22individual_studies%22%3Anull%2C%22summer_session%22%3Anull%7D&_=1479296573078']

class_found_flag = False

for URL in URLs:
	soup = BeautifulSoup(urllib.urlopen(URL))

	class_statuses = soup.find_all('div', {'class','statusColumn'})[1:]
	for class_status in class_statuses:
		if(check_status(class_status)):
			print URL[305:315] + " : " + class_status.text
			class_found_flag = True

if(class_found_flag):
	os.system("pause")


"""
# Get the json given the class ID you want
# that gives partial info about the URL containing enrollment details

base_URL = 'https://sa.ucla.edu/ro/Public/SOC/Results?t=17W&sBy=subject&sName=Computer+Science+%28COM+SCI%29&subj=COM+SCI&crsCatlg=Enter+a+Catalog+Number+or+Class+Title+%28Optional%29&catlg=&cls_no=&btnIsInIndex=btn_inIndex';

class_ids = ['COMSCI0111', 'COMSCI0180']

soup = BeautifulSoup(urllib.urlopen(base_URL))

for class_id in class_ids:
	result = soup.find(id=class_id)
	print json.loads(result.findNext('script').text[77:-16])
"""

"""
#Failed attempt at sending email because of gmail's security measures
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