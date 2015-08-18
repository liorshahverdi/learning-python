from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('https://gabrielecirulli.github.io/2048/')
try:
	elem = browser.find_element_by_class_name('grid-container')
except:
	print 'Was not able to find an element with that name.'
print type(elem)

while True:
	elem.send_keys(Keys.LEFT)
	elem.send_keys(Keys.RIGHT)
	elem.send_keys(Keys.UP)
	elem.send_keys(Keys.DOWN)