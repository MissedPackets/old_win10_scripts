from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

#
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions

options = FirefoxOptions()
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)
#headless

#
f = open("tune_hist.txt", "r")
prompt=f.read()
# WANTED TEXT/INPUT

#PROXY
from random import randint
f=(randint(1,95))
port = (f":412{f}") #randomize proxy's last 2 digits.
myProxy="68.183.129.76" + port

print(myProxy)

webdriver.DesiredCapabilities.FIREFOX['proxy']=({'proxyType': ProxyType.MANUAL,
'httpProxy': myProxy,
# 'ftpProxy': myProxy,
# 'sslProxy': myProxy,
# "noProxy":None,
"proxyType":"MANUAL",
# "autodetect":False
# set this value as desired
})

#

# driver = webdriver.Firefox()
options = FirefoxOptions()
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)
driver.get('https://www.wordtune.com/')
input_text=f'{prompt}'
# select = Select(driver.find_element_by_id('widget-textarea'))
element = driver.find_element_by_id("widget-textarea")
element.send_keys(input_text)
element = driver.find_element_by_id("widget-rewrite-button").click()

# select by visible text
# select.select_by_visible_text('gptneox_20B')
time.sleep(2.52) #depending on the length of text, it'll take a longer time if it is lengthy

print(driver.find_element_by_id("landingPageDemoWidget").text)

f = open("RE_Tuned_words.txt", "a")
f.write('\n\n=---------X-----------=\n\n' + driver.find_element_by_id("landingPageDemoWidget").text)
f.close()

driver.quit()