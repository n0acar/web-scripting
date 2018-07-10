from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
count=2156865

for i in range (2):
    count-=1
    print(count)
    score = 'http://www.sabah.com.tr/canli-skor/canli-mac?matchId='+str(count)
    browser = webdriver.Chrome(executable_path='/Users/nev/Desktop/chromedriver')
    browser.get(score)
    timeout=4
    try:
        WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='csIconInfo']")))
        soup = BeautifulSoup(browser.page_source, 'html.parser')
        commentary = soup.find('ul', id='Incident')
        ex = commentary.find_all('li')
        if len(ex) > 50:
            file = '/Users/nev/Desktop/IUI Yaz Çalışması/sabah/sabah' + str(count) + '.txt'
            f = open(file, 'w')
            for x in ex:
                yaz = x.get_text()
                n = yaz.find("'")
                f.write(yaz[n + 1:])
                f.write('\n')
            f.close()
        browser.quit()
    except TimeoutException:
        print("Timed out waiting for page to load")
        browser.quit()

