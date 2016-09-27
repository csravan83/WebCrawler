import requests
from bs4 import BeautifulSoup
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('http://www.imdb.com/?ref_=nv_home')
elem = driver.find_element_by_id('navbar-query')
elem.send_keys('dexter')
elem.send_keys(Keys.RETURN)

xp = '//*[@id="main"]/div/div[2]/table/tbody/tr[1]/td[2]/a'
elem1 = driver.find_element_by_xpath(xp)
elem1.click()

rev_xpath = '//*[@id="title-overview-widget"]/div[3]/div[2]/div[1]/div[2]/span/a[1]'
elem2 = driver.find_element_by_xpath(rev_xpath)
elem2.click()

url = driver.current_url
req = requests.get(url)
rev_soup = BeautifulSoup(req.text, "html.parser")
x = []
res = []
f = 'rev1.csv'
f1 = open(f, mode='w')
wr = csv.writer(f1, dialect='excel')

for i in range(1,10):
    x = (rev_soup.find("div", {"id": "tn15content"}).findAll('p'))[i]
    wr.writerow([x])

f1.close()
