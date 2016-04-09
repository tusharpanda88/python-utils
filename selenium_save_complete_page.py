from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
from lxml import html
import os
import urllib2
from bs4 import BeautifulSoup as bsp
from selenium.webdriver.support.ui import WebDriverWait
import timeit
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://google.in")
time.sleep(2)
ActionChains(driver) \
	.key_down(Keys.CONTROL) \
	.key_down('s') \
	.key_up(Keys.CONTROL) \
	.key_up('s') \
	.perform()

#element = driver.find_element_by_id('lst-ib')
#ActionChains(driver) \
#    .key_down(Keys.CONTROL) \
#    .click(element) \
#    .key_up(Keys.CONTROL)

raw_input("ctrl+s triggered...")

#htmltext  = (driver.page_source).encode('utf-8')
#f = open("google1", "w")
#print >> f, htmltext
#f.close()
time.sleep(5)

driver.close()
print "Exiting.."

