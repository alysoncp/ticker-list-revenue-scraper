import csv
from pprint import pprint
import requests
import bs4
from bs4 import BeautifulSoup


#Function for scraping revenue growth data from GURU FOCUS for any given ticker.
def getRevenueTable(ticker):
    #Fancy soup scraping setup stuff
    pr = requests.get('https://www.gurufocus.com/financials/'+ticker)
    soup=bs4.BeautifulSoup(pr.text, features="html.parser" )    
    
    #Nested loops to scrape data from table
    i = 1
    j = 1
    data = [ticker]
    while i <= 6:
        while j <= 3:
            try:
                figure=soup.find('table',{'id':'R1'}).find_all('tr')[i].find_all('td')[j].text
            except:
                figure = "N/A"
            try:
                data.append(float(figure))
            except:
                data.append(figure)
            j+=1
        j=1    
        i+=1
    print(ticker+" has beed scraped")    
    return data

'''
def getPE(ticker):
    #Fancy soup scraping setup stuff
    pr = requests.get('https://www.gurufocus.com/financials/'+ticker)
    soup=bs4.BeautifulSoup(pr.text, features="html.parser" )
    PE=soup.find('table',{'id':'stock_header_ratio_table'}).find_all('th')[2].text
    
    print(PE)
'''

#Function to generate headers before forst scrape
def makeHeaders():
    #As pulled from GURU FOCUS
    headers = ['Ticker', 'Revenue Growth (%) 10year', 'Revenue Growth (%) 5year', 'Revenue Growth (%) 12mo',
     'EBITDA Growth (%) 10year', 'EBITDA Growth (%) 5year', 'EBITDA Growth (%) 12mo',
     'Operating Income Growth (%) 10year', 'Operating Income Growth (%) 5year', 'Operating Income Growth (%) 12mo',
     'EPS without NRI Growth (%) 10year', 'EPS without NRI Growth (%) 5year', 'EPS without NRI Growth (%) 12mo',
     'Free Cash Flow Growth (%) 10year', 'Free Cash Flow Growth (%) 5year', 'Free Cash Flow Growth (%) 12mo',
     'Book Value Growth (%) 10year', 'Book Value Growth (%) 5year', 'Book Value Growth (%) 12mo']
               
    return headers


#------------------MAIN CODE----------------#

#Generate the headers for Pandas dataframe
headers = makeHeaders()

'''
#Import list of tickers
df = open('internet_software_tickers.csv', 'r')

with df:

    readFile = csv.reader(df)

    for tickers in readFile:
        print(tickers)
  '''      
#Or copy and paste a list of tickers with the first item being "Tickers"
tickers = ['Tickers', 'DDD', 'AYX', 'PLAN', 'AVLR', 'BB', 'BOX', 'CDAY', 'ECOM ', 'CISN', 'CLDR', 'ESTC', 'ELLI', 'GWRE', 'HUBS', 'INST', 'MIXT\n', 'LN\n', 'NEWR', 'ORCL', 'PVTL', 'RST', 'SAIL', 'CRM', 'NOW', 'SHOP', 'SMAR', 'SQ', 'DATA', 'TDC', 'TWLO', 'TYL', 'VMW', 'WK', 'FDS', 'HUYA', 'MODN', 'RHT', 'SNAP']
        

#Enter desired tickers and determine length of list
listLength = len(tickers)

#Reader loop for each ticker
i = 1
fullSheet = ['no data']*listLength
fullSheet[0] = headers

while i < listLength:
    tableRow = getRevenueTable(tickers[i])
    fullSheet[i] = tableRow
    tableRow = []
    i+=1

print(fullSheet)
 
#writeCSV(fullSheet, headers)

f = open('df.csv', 'w')

with f:

    writer = csv.writer(f)
    writer.writerows(fullSheet)



