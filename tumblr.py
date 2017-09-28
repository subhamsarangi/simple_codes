# Xkcd.py - Downloads all XKCD comic image files.
import requests, os, bs4
from bs4 import BeautifulSoup
url = 'http://ibuzoo.tumblr.com/tagged/paes'
os.makedirs('tumblrgod', exist_ok=True)
print('Downloading the page: %s...' % url)
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text,'html.parser')
comic_elem=soup.select('a.photoset_photo')
comic_url = comic_elem.get('href')
print('Downloading image %s...' % (comic_url))
res = requests.get(comic_url)
res.raise_for_status()
image_file = open(os.path.join('god', os.path.basename(comic_url)), 'wb')
for chunk in res.iter_content(2000000):
	image_file.write(chunk)
	image_file.close()

print('Done.')