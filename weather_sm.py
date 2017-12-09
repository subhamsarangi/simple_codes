import requests
from bs4 import BeautifulSoup
from datetime import datetime
import csv
from weather.the_world_sm import the_world

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1'}

time_utc=datetime.utcnow().strftime("%A, %d %B %Y %I:%M%p") #current utc time
time_loc=datetime.now().strftime("%A, %d %B %Y %I:%M%p") #current local time
time_file=datetime.now().strftime("%Y%m%d-%H%M%S") #current local time for file

print('UTC  '+time_utc)
print('LOCAL  '+time_loc+'\n')

data=[]
for place in the_world:
	url='https://www.google.co.in/search?&q='+place+'+weather'
	res = requests.get(url,headers=headers)
	res.raise_for_status()
	soup = BeautifulSoup(res.text,'html5lib')
	temp=soup.find('span',{'class':'wob_t'}).text
	location=soup.find('div',{'class':'vk_gy vk_h'}).text
	time_local=soup.find('div',{'class':'vk_gy vk_sh'}).text
	data.append((location, temp,time_local))
	print (location,' : ',temp,' - ',time_local)

csvfile='weather-sm-'+time_file+'.csv'
with open(csvfile, 'w') as csv_file:
	writer = csv.writer(csv_file)
	for loc, temp, time_local in data:
		writer.writerow([loc, temp, time_local])
	
print('Done')