import requests
from bs4 import BeautifulSoup
count=1
for i in range(432,-12,-12):
    mainscore = 'http://spor.mynet.com/canli-mac-anlatimi-ve-sonuclari.html?start=' + str(i) + '/'
    mainpage =requests.get(mainscore)
    mainsoup = BeautifulSoup(mainpage.content , 'html.parser')
    maincommentary = mainsoup.find('ul', class_='mac-list clearfix')
    print(i)
    if not maincommentary is None:
        ex=maincommentary.find_all('a')
        for it in ex:
            at = it['href']
            if at[0].isspace():
                score='http://spor.mynet.com/canli-mac-anlatimi-ve-sonuclari'+at[1:]
            else:
                score='http://spor.mynet.com/canli-mac-anlatimi-ve-sonuclari'+at

            page =requests.get(score)
            soup = BeautifulSoup(page.content,'html.parser')
            block = soup.find('ul', class_='canli-anlatim-list clearfix')
            commentary=None
            if not block is None:
                commentary = block.find_all('li', class_='clearfix')
            if not commentary is None:
                file = '/Users/nev/Desktop/IUI Yaz Çalışması/mynet/mynet' + str(count) + '.txt'
                count+=1
                f = open(file, 'w')
                for item in commentary:
                    con= item.find('div', class_='minute').get_text()
                    if con.find('NOT')==-1 and con.find('İY')==-1:
                        yaz=item.find('div', class_='action').get_text()
                        if (not yaz.isspace()) or yaz[0]!='@':
                            f.write(yaz)
                            f.write('\n')
                f.close()
