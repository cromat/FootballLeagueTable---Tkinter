from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

html_page = urlopen("http://www.ns-novska.hr/Natjecanja.aspx?id=2")
soup = BeautifulSoup(html_page)
for link in soup.findAll('a'):
    print (link.get('href'))