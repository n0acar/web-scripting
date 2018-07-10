from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
import time
page = 'http://www.mackolik.com/Basketbol/Canli-Sonuclar'
browser = webdriver.Chrome(executable_path='/Users/nev/Desktop/chromedriver')
browser.get(page)
timeout=50
try:
    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//div[@id='dvScores']")))
    element1 = browser.find_element_by_css_selector(".vol2[id='chkIddaa']")

    #browser.execute_script("arguments[0].setAttribute('class','vol2 selected')", element1)
    element2 = browser.find_element_by_css_selector(".mc-top-bar-menu[id='extraMenu0']")
    #browser.execute_script("arguments[0].setAttribute('class','mc-top-bar-menu-active')", element2)
    #element1.click()
    element2.click()
    time.sleep(5)
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    commentary = soup.find('div', id='dvScores')
    print(commentary)
    ex = commentary.find_all('tr', sport="2")
    print(ex)
    tList= []
    time.sleep(5)
    for x in ex:
        tList.append(x.find_all('div', class_='teamDiv'))
    for item in tList:
        print(item)
        print(item[0].get_text())
        print(item[1].get_text())
    commentary = soup.find('tr', class_='right-line-bg rate-text')
    print(commentary)

    browser.quit()
except TimeoutException:
    print("Timed out waiting for page to load")
    browser.quit()