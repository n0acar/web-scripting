from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
count=111264723
for i in range (100):
    count-=1
    score = 'https://www.iddaa.com/macdetay/futbol/-/-/'+str(count)+'/mac-merkezi'
    browser=webdriver.Chrome(executable_path='/Users/nev/Desktop/chromedriver')
    browser.get(score)

    timeout=4
    try:
        WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='overview']")))
        soup = BeautifulSoup(browser.page_source, 'html.parser')
        commentary = soup.find('div', class_='overview')
        ex = commentary.find_all('li')
        if len(ex)>35:
            file = '/Users/nev/Desktop/IUI Yaz Çalışması/iddaa/iddaa' + str(count) + '.txt'
            f = open(file, 'w')
            for x in ex:
                min = x.find('div', class_='minute')
                if min.get_text()[0].isdigit():
                    yaz = x.find('div', class_='text').get_text()
                    n = yaz.find(')')
                    if n == -1:
                        f.write(yaz[1:])
                        f.write('\n')
                    else:
                        f.write(yaz[n + 1:])
                        f.write('\n')
            f.close()
        browser.quit()
    except TimeoutException:
        print("Timed out waiting for page to load")
        print(count)
        browser.quit()

