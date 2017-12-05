# Xkcd.py - Downloads all XKCD comic image files.
import requests, os, bs4
from bs4 import BeautifulSoup
url = 'http://xkcd.com/2'
os.makedirs('xkcd', exist_ok=True) # store comics in ./xkcd
while not url.endswith('#'):
	print('Downloading the page: %s...' % url)
	res = requests.get(url)
	res.raise_for_status()
	soup = BeautifulSoup(res.text,'html.parser')
	# Find the URL of the comic image.
	comic_elem = soup.select('#comic img')
	if comic_elem == []:
		print('Could not find a comic image.')
	else:
		comic_url =  'http:'+comic_elem[0].get('src')
		# Download the image.
		print('Downloading image %s...' % (comic_url))
		res = requests.get(comic_url)
		res.raise_for_status()
		# Save the image to ./xkcd.
		image_file = open(os.path.join('xkcd', os.path.basename(comic_url)), 'wb')
		for chunk in res.iter_content(2000000):
			image_file.write(chunk)
			image_file.close()
	# Get the Prev button's url.
	prev_link = soup.select('a[rel="prev"]')[0]
	url = 'http://xkcd.com' + prev_link.get('href')

print('Done.')
