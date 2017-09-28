#BeautifulSoup4 web scraping with python 2.6
import urllib2
from bs4 import BeautifulSoup
import csv
from datetime import datetime

quote_page = [
'http://www.bloomberg.com/quote/SENSEX:IND', 
'http://www.bloomberg.com/quote/BSE500:IND',
'http://www.bloomberg.com/quote/nifty:IND']
data = []
for pg in quote_page:
	# query the website and return the html to a variable
	page = urllib2.urlopen(pg)
	# parse the html using beautiful soup and store in a variable
	soup = BeautifulSoup(page, 'html.parser')
	# Take out the <div> of name and get its value
	name_box = soup.find('h1', attrs={'class': 'name'})
	# strip() is used to remove starting and trailing
	name = name_box.text.strip()
	print(name)
	# get the index price
	price_box = soup.find('div', attrs={'class':'price'})
	price = price_box.text
	print(price)
	# save the data in tuple
	data.append((name, price))
	# open a csv file with append, so old data will not be erased
	with open('index.csv', 'a') as csv_file:
 		writer = csv.writer(csv_file)
		# The for loop
 		for name, price in data:
 			writer.writerow([name, price, datetime.now()])
