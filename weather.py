import urllib2
from bs4 import BeautifulSoup

quote_page = 'https://www.wunderground.com/history/airport/KNYC/2015/1/11/MonthlyHistory.html'
page = urllib2.urlopen(quote_page)
soup = BeautifulSoup(page, 'html.parser')
table = soup.find('table', attrs={'id': 'obsTable'})
table_body = table.find('tbody')

rows = table.find_all('tbody')
# Loop through top 20 players skipping 3 headers
for row in rows[1:]:    
    # Get all columns
    tds = row.find_all('td')
    # Print data
    print "Day: %s, Average Temp: %s" % \
          (tds[0].text.strip(), tds[2].text.strip())
