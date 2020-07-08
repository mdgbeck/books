from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('https://inventwithpython.com')

try:
    elem = browser.find_element_by_class_name('cover-thumb')
    print('Found <%s> element with that class name!' % (elem.tag_name))
except:
    print('Was not able to find an element with that name')

b2 = webdriver.Firefox()
b2.get('https://nostartch.com')

html_elem = b2.find_elements_by_tag_name('html')
html_elem.send_keys(Keys.END)
html_elem.send_keys(Keys.HOME)
