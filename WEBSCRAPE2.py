'''
Created on 2019 M03 27

@author: danielmorettin
'''
'SCRAPE FOR SECOND POSSIBLE BUILD'
# Imports
from threading import Timer
import csv
import datetime
from bs4 import BeautifulSoup
import requests
from logger import my_logger
from timer import my_timer
# Access the webpage, store the source code in an object'
webpage = requests.get(
    'https://ca.pcpartpicker.com/guide/FkrxFT/excellent-amd-gamingstreaming-build')
source = webpage.content

# Create a beautifulsoup object'

page = BeautifulSoup(source)

# Get the table we are looking for using inspectelement on firefox, and
# specifying the class'
table = page.find('table', class_='xs-col-12')
# print(table)

# Find the part of the table that contains part list
partlist = table.find('tbody')


@my_timer
@my_logger
def getpartprices2():
    with open('PartPrices2.csv', 'a', encoding='utf-8') as file:
        writer = csv.writer(file)
        for part in partlist.find_all('tr', class_='tr__product'):
            # Use a try... except. If the website includes a new 'td' tag in the partlist, this will be
            # tried through the loop, if it produces an attribute error it will skip to the next 'td'
            # tag, fixing the problem of random "mail in rebates" being placed between components in the
            # table.
            try:
                # Get the type of part (What component is it?)
                component = part.find('td', class_='td__component').find('a').text
                print(component)
                # Get the name of the part
                name = part.find('td', class_='td__name').find('a').text
                print(name)
                # Get the price of the part
                price = part.find('td', class_='td__price').find('a').text
                print(price)
                # Get the retailer of the part
                retailer = part.find('td', class_='td__where').find('a')['href']
                retailer = retailer.split('/')[2]
                print(retailer)
                # Get the current date and time
                # I got this date and time with help from this link:
                # https://tecadmin.net/get-current-date-time-python/
                uglytime = datetime.datetime.now()
                time = uglytime.strftime("%Y-%m-%d %H:%M")
                print(time)
                writer.writerow([component, name, price, retailer, time, ])
            except AttributeError:
                # Attribute error will occur if the part returns 'None' which will occur when rebates
                # are available for certain components aside from the last one
                continue
    return


x = getpartprices2()
