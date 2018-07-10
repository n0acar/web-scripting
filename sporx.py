import requests
from bs4 import BeautifulSoup
for i in range(1,2399):
    num = str(i)
    while len(num)<4:
        num = '0' + num
    print(num)
    score = 'http://www.sporx.com/canlianlatim/SXLIVEQ' + num + 'SXQ'
    page =requests.get(score)
    soup = BeautifulSoup(page.content , 'html.parser')
    commentary = soup.find('li', class_='commentary selected')
    if not commentary is None:
        ex=commentary.find_all('li')
        file = '/Users/nev/Desktop/IUI Yaz Çalışması/sporx/sporx' +num +'.txt'
        f=open(file, 'w')
        for item in ex:
            yaz=item.find('div', class_='min').get_text()
            if not yaz.isspace():
                f.write(item.find('div', class_='text').get_text())
                f.write('\n')
        f.close()