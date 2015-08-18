import bs4, requests

site = requests.get('http://missingkids.com/search')
soup = bs4.BeautifulSoup(site.text)
print site.text