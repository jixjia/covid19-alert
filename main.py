'''
Author:         Jixin Jia (Gin)
Date:           19-Feb-2020
Version:        1.0

Description:
This program collects COVID-19 worldwide stats from
https://www.worldometers.info/coronavirus/ and send updates to desired
mobile phone in SMS
'''
from bs4 import BeautifulSoup
import requests
import datetime
import logging
from modules import SMSNotification
from modules import config

# Initiate SMS Notification
sms = SMSNotification()
keys = ['Total', 'Deaths', 'Recovered']
results = {}
statement = ''

# Main program
current_dt = datetime.datetime.now().strftime("%d-%b-%Y %H:%M")

# Make GET request to target URL
r = requests.get(config.BASE_URL)
soup = BeautifulSoup(r.text, 'html.parser')

# Extract summary stats
stats = soup.select('.maincounter-number')

for elem in enumerate(stats):
    value = elem[1].text.strip()
    results[keys[elem[0]]] = value

# Extract country breakdown
table = soup.find('table', attrs={'id': 'main_table_countries'})
table_body = table.find('tbody')
rows = table_body.find_all('tr')

for row in rows:
    cells = row.find_all('td')
    cell = [elem.text.strip() for elem in cells]
    # Parse countries of interest
    if cell[0] in config.countries:
        results[cell[0]] = cell[1] if cell[1] else 0
        results[cell[0] +
                '-new'] = cell[2].replace('+', 'new') if cell[2] else 'new 0'

# Create SMS message
for i in results:
    if '-new' in i:
        statement += '({}) '.format(str(results[i]))
    else:
        statement += '{}:{} '.format(i, str(results[i]))

message = '<Covid-19 Update> {} Updated: {} (UTC)'.format(
    statement[:-1], current_dt)
print(message)
logging.info(message)

# Send SMS
try:
    for to_number in config.TO:
        sms.send(to_number, message)
except Exception as e:
    error = 'Twilio failed ->', e.args
    logging.info(error)
    print(error)
