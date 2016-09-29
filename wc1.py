import requests
from bs4 import BeautifulSoup
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def striphtml(data):
    p = re.compile(r'<.*?>')
    return p.sub('', data)

driver = webdriver.Chrome()
driver.get('https://www.snapdeal.com/')
elem = driver.find_element_by_id('inputValEnter')
elem.send_keys('iphone5s')
elem.send_keys(Keys.RETURN)
time.sleep(2)

xp = '//*[@id="347830397"]/div[3]/div[1]/a'
sn_url = driver.find_element_by_xpath(xp).get_attribute("href")

try:
    driver.get(sn_url)
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "ReviewHeader"))
    )
    xp1 = '//*[@id="ReviewHeader"]/div/div[1]/ul/li[1]/div/div/a'
    elem2 = driver.find_element_by_xpath(xp1).click()

    url = driver.current_url
    req = requests.get(url)
    rev_soup = BeautifulSoup(req.text, "html.parser")
    x = []
    # res = []
    f = 'reviews.csv'
    f1 = open(f, mode='w')
    wr = csv.writer(f1, dialect='excel')
    reviews_array = rev_soup.findAll("div", {"class": "user-review"})
    print len(reviews_array)
    for a_review in reviews_array:
        # x = (rev_soup.find("div", {"id": "defaultReviewsCard"}).findAll('p'))[i]
        # x = (rev_soup.find("div", {"class": "commentreview"})).findAll('p')[i]
        wr.writerow([striphtml(str(a_review.findAll('p')[0]))])
    f1.close()

finally:
    driver.quit()
