from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
from xlwt import Workbook

import time

wb = Workbook()
page= wb.add_sheet('Sheet 1')
rc=0
for id in range(1,8593):
    profile = 'https://ipk.adimadim.org/profil/IPK' + str(id)
    browser = webdriver.Chrome(executable_path='/Users/nev/Desktop/chromedriver')
    browser.get(profile)
    timeout = 4

    try:
        WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//section[@id='footer']")))
        psoup = BeautifulSoup(browser.page_source, 'html.parser')
        browser.close()
        pcommentary = psoup.find('ul', class_='list-group')
        if not pcommentary is None:
            ex = pcommentary.find_all('li')
            table = psoup.find('table', class_='table table-striped table-bordered')
            if not table is None:
                rc+=1
                page.write(rc, 0, str(id))
                page.write(rc, 1, ex[0].get_text())
                page.write(rc, 2, ex[1].get_text())
                job=ex[2].get_text()
                a= job.find(':')
                b= job.find('Meslek')
                c= job[b:].find(':')
                #if jobs don't contain - between its words then go for this code
                # if job[a+2:b].contains('-'):
                #     page.write(rc, 3, 'no data')
                # else:
                page.write(rc, 3, job[a+2:b-2])
                # if job[b+c+2:].contains('-'):
                #     page.write(rc, 3, 'no data')
                # else:
                page.write(rc, 4, job[b+c+2:])
                distance=ex[3].get_text()
                a = distance.find(':')
                page.write(rc, 5, distance[a+2:-2])
                sports = ex[4].get_text()
                a = sports.find(':')
                page.write(rc, 6, sports[a+2:])
                parkours = ex[5].get_text()
                a = parkours.find(':')
                page.write(rc, 7, parkours[a+2:])
                tabbody= table.find('tbody')
                links = tabbody.find_all('a')
                effect=psoup.find('div', class_='social-effect')
                don=effect.find_all('strong')
                tdon=don[0].get_text()
                tper=don[1].get_text()
                page.write(rc, 8, tdon)
                page.write(rc, 9, tper)
                cc = 10
                sorted = []
                for it in links:
                    at = it['href']
                    a = at.find('CC')
                    code = int(at[a+2:])
                    sorted.append(code)
                    sorted.sort()
                for ncode in sorted:
                    campaign = 'https://ipk.adimadim.org/kampanya/CC' + str(ncode)
                    browser = webdriver.Chrome(executable_path='/Users/nev/Desktop/chromedriver')
                    browser.get(campaign)
                    timeout = 10
                    try:
                        WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//div[@id='campaign-circle']")))
                        csoup = BeautifulSoup(browser.page_source, 'html.parser')
                        browser.close()
                        ccommentary = csoup.find('ul', class_='list-group')
                        run = ccommentary.find_all('li')
                        a= run[0].get_text().find(':')
                        ele=run[0].get_text()
                        rname=ele[a+1:].lstrip('')
                        page.write(rc, cc, rname)
                        cc+=1
                        a = run[1].get_text().find(':')
                        ele = run[1].get_text()
                        ndon = ele[a+1:].lstrip('')
                        page.write(rc, cc, ndon)
                        cc+=1
                        circles = csoup.find('div', class_='col-lg-3 col-md-3 col-sm-3 text-center')
                        campaign = circles.find_all('h2')
                        personalcam= campaign[0]
                        x=personalcam.get_text()
                        for char in x:
                            if char.isspace():
                                x = x.replace(char, '')
                        a=x.find('/')
                        page.write(rc, cc, x[:a])
                        cc+=1
                        page.write(rc, cc, x[a+1:-2])
                        cc += 1
                        cc += 1  # space for the formula
                        page.write(rc, cc, 'CC' + str(ncode))
                        cc+=1
                        if len(run)==7:
                            a = run[3].get_text().find(':')
                            ele = run[3].get_text()
                            teams = ele[a + 1:]
                            page.write(rc, cc, teams)
                        else:
                            page.write(rc, cc, 'no teams')
                        cc+=1
                        projectcam = campaign[1]
                        y = projectcam.get_text()
                        for char in y:
                            if char.isspace():
                                y = y.replace(char, '')
                        a = y.find('/')
                        print(y[:a])
                        page.write(rc, cc, y[:a])
                        cc += 1
                        page.write(rc, cc, y[a + 1:-2])
                        cc += 1
                        cc += 1
                    except TimeoutException:
                        print("Timed out waiting for page to load campaign")
                        print(at)
                        browser.close()
    except TimeoutException:
        print("Timed out waiting for page to load")
        print(rc)
        browser.close()
wb.save('/Users/nev/Desktop/ECON Exp Ex.xls')
