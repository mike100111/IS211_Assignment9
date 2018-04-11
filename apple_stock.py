import urllib2
from bs4 import BeautifulSoup

quote_page = 'https://finance.yahoo.com/quote/AAPL/history?p=AAPL'
page = urllib2.urlopen(quote_page)
soup = BeautifulSoup(page, 'html.parser')
table = soup.find('table', attrs={'data-test': 'historical-prices'})
table_body = table.find('tbody')

rows = table_body.find_all('tr')
# Loop through top 20 players skipping 3 headers
for i in range (0,20):
    # Get all columns
    tds = rows[i].find_all('td')    
    # Print data
    print str(i+1) + ")Date: %s, Close Price: %s" % \
          (tds[0].text, tds[4].text)
