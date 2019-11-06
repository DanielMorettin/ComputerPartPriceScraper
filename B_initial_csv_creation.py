'''
Created on 2019 M02 17

@author: danielmorettin
'''
import csv
'IF YOU RUN THIS IT WILL OVERWRITE THE CURRENT FILE UNLESS YOU HAVE RENAMED IT'

'Open the file, create the writer, write the first row of labels'
with open('PartPricesNew.csv', 'w', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Part Type', 'Part name', 'Price (CAD$)',
                     'Retailer', 'Date Scraped'])
