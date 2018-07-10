import requests
from bs4 import BeautifulSoup
for i in range(110,116):
    mainscore = 'http://www.sportsmole.co.uk/football/live-commentary/page-' + str(i) + '/'
    mainpage =requests.get(mainscore)
    mainsoup = BeautifulSoup(mainpage.content , 'html.parser')
    maincommentary = mainsoup.find('div', id='content')
    print(i)
    if not maincommentary is None:
        ex=maincommentary.find_all('a')
        for it in ex[3:-2]:
            at = it['href']
            score= 'http://www.sportsmole.co.uk' + at
            page = requests.get(score)
            soup = BeautifulSoup(page.content, 'html.parser')
            commentary = soup.find('div', id='article_body')
            file = '/Users/nev/Desktop/IUI Yaz Çalışması/goal/goal' + at[-10:-5] + '.txt'
            f = open(file, 'w')
            if not commentary is None:
                parray1 = commentary.find_all('p')
                #parray2 = commentary.find_all('div', class_='livecomm')
            if len(parray1)>1:
                for p in parray1:
                    pure = p.get_text()
                    if len(pure)>=2:
                        if pure[0].isdigit() and pure[1] != '.' and pure[2] != '.' and pure[1] != ':' and pure[2] != ':'and pure[1:3] != 'am' and pure[1:3] != 'pm' and pure[2:4] != 'am' and pure[2:4] != 'pm' and pure[3:5] != 'am' and pure[3:5] != 'pm':
                            a = pure.find('mins')
                            if a==-1:
                                b = pure.find('min')
                                f.write(pure[b+3:]+'\n')
                            else:
                                f.write(pure[a+4:]+'\n')
            f.close()