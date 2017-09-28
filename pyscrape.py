#BeautifulSoup4 web scraping with python 3.5

from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
from datetime import datetime

quote_page = 'https://www.bloomberg.com/quote/SENSEX:IND'
page = urlopen(quote_page) # open url
soup = BeautifulSoup(page, 'html.parser') # parse html
print (soup.head.contents[5].text) # title of page being scraped
name_box = soup.find('h1', attrs={'class': 'name'})
name = name_box.text.strip()
print (name)

price_box = soup.find('div', attrs={'class':'price'})
price = price_box.text
print (price)

print("\nPrevious price: ")
prev_close_val = soup.findall(class = {'cell__value'})
prev_val = prev_close_val.text
print (prev_close_val)

# ln=ln(soup.head.contents)
# for i in range(ln):
#	print(soup.head.contents[i])
