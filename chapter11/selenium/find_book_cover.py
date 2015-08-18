from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://inventwithpython.com')
try:
	elem = browser.find_element_by_link_text('Read It Online')
except:
	print 'Was not able to find an element with that name.'
print type(elem)
elem.click()