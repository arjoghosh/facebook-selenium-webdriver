# Author : Arjo Ghosh আর্য্য ঘোষ

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
x=input("Enter username :\t")
x=x.strip()
y=input("Enter password :\t")
browser = webdriver.Firefox()
browser.get('http://facebook.com')
action = webdriver.ActionChains(browser)
emailElem = browser.find_element_by_id('email')
emailElem.send_keys(x)
passwordElem = browser.find_element_by_id('pass')
passwordElem.send_keys(y)
signinButton = browser.find_element_by_id('u_0_m')
signinButton.click()
