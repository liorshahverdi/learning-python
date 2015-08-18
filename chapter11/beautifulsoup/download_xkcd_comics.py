# download_xkcd_comics - pretty self explanatory, kind of excessive but what the hell
# were scraping right

import requests, os, bs4

url = 'http://xkcd.com'		#starting url
os.makedirs('xkcd', exist_ok=True)
while not url.endswith('#'):
	#TODO: Download the page

	#TODO: Find the URL of the comic page.

	#TODO: Download the image

	#TODO: Save image to folder.

	#TODO: Get the Prev button's url.

print 'Done.'