import urllib2
from bs4 import BeautifulSoup

quote_page = 'https://www.cbssports.com/nfl/stats/playersort/nfl/year-2017-season-regular-category-touchdowns'
page = urllib2.urlopen(quote_page)
soup = BeautifulSoup(page, 'html.parser')
table = soup.find('table', attrs={'class': 'data'})
table_body = table.find('tbody')

rows = table.find_all('tr')
# Loop through top 20 players skipping 3 headers
for i in range (0,20)[3:]:
    # Get all columns
    tds = rows[i].find_all('td')
    # Print data
    print "Name: %s, POS: %s, Team: %s, TD: %s" % \
          (tds[0].text, tds[1].text, tds[2].text, tds[6].text)
