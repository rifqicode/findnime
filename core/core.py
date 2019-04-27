import sys
from bs4 import BeautifulSoup
import requests
import json

# author | uhammad Rifqi <muhammadrifqi.tb@gmail.com>
# page = int(sys.argv[1]) + 1
# row = int(sys.argv[2])
page = 2
row = 2
response = []

for i in range(1,int(page)):
    website = ''
    if i > 0:
        website = requests.get('https://www.samehadaku.tv/page/' + str(i))
    else :
        website = requests.get('https://www.samehadaku.tv/')

    if website.status_code == 200:
        html = BeautifulSoup(website.content , 'html.parser')
        getContents = html.find_all(class_="post-title")
        getContents = getContents[0:int(row)]

        for x in getContents:
            # attribute
            link = x.find('a').get('href')
            anime_name = x.find('a').getText()
            anime_link = ''

            openLink = requests.get(link)
            if openLink:
                # open one
                content = BeautifulSoup(openLink.content , 'html.parser')
                contentList = content.find('div' , class_="download-eps")

                if len(contentList.find_all('li')) > 1:
                    linkList = contentList.find_all('li')[1].find_all('a')
                else :
                    linkList = contentList.find_all('li')[0].find_all('a')

                # open two
                linkDownload = linkList[3].get('href')
                openLink2 = requests.get(linkDownload)
                content2 = BeautifulSoup(openLink2.content , 'html.parser')
                contentList2 = content2.find('div' , class_="download-link")
                # open three
                linkDownload2 = contentList2.find('a').get('href')
                openLink3 = requests.get(linkDownload2)
                content3 = BeautifulSoup(openLink3.content , 'html.parser')
                contentList3 = content3.find('div' , class_="download-link")
                # content download zippyshare
                zippyshare = contentList3.find('a').get('href')
                openZippy = requests.get(zippyshare)
                contentZippy = BeautifulSoup(openZippy.content , 'html.parser')

                if (contentZippy.find(class_="afterglow") is None):
                    anime_link = 'Gagal Grab :<'
                else :
                    anime_link = 'https:' + contentZippy.find(class_="afterglow").find('source').get('src')

                dictionaries = anime_name + '--' + anime_link
                response.append(dictionaries)

print(json.dumps(response))
sys.stdout.flush()
