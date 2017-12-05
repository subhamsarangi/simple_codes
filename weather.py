import requests
from bs4 import BeautifulSoup
from datetime import datetime
import csv

usa=['nyc','chicago','boston','minnesota','philadelphia','sioux+falls','bemidji','washington+dc','miami','mississipi','tennessee','houston','el+paso','albuquerque','los+angeles','san+francisco','san+diego','las+vegas','aspen','denver','oklahoma+city','omaha','seattle']

india=['kolkata','jhargram','bengaluru','delhi','mumbai','chennai','pune','patna']

western_europe=['berlin','munich','hamburg','frankfurt','cologne','rome','milan','tuscany','sicilly','naples','modena','turin','lombardy','amsterdam','paris','versailles','normandy','london','devonshire','glasgow','dublin','wales','york','lancashire','madrid','barcelona','sevilla','lisbon','reykjavik','oslo','stockholm','helsinki']
the_world=india+usa+western_europe
l=len(the_world)
data=[]
time=datetime.utcnow().strftime("%A, %d. %B %Y %I:%M%p")
for place in the_world:
	url='https://www.google.co.in/search?&q='+place+'+weather'
	res = requests.get(url)
	res.raise_for_status()
	soup = BeautifulSoup(res.text,'html5lib')
	temp=soup.find('span',{'class':'wob_t'}).text
	print ((soup.head.contents[3].text)[:-16],' : ',temp)
	data.append((place, temp))

with open('weather_now.csv', 'a') as csv_file:
	writer = csv.writer(csv_file)
	for place, temp in data:
		writer.writerow([place, temp, time])
	
print('Done')