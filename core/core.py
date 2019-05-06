# author | uhammad Rifqi <muhammadrifqi.tb@gmail.com>

import sys
from bs4 import BeautifulSoup
import requests
import json


row = int(sys.argv[1])
response = []

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

            if (contentZippy.find(class_="video-share").find('input') is None):
                anime_link = 'Gagal Grab :<'
            else :
                anime_link = 'https:' +contentZippy.find(class_="video-share").find('input').get('value')

            dictionaries = anime_name + '--' + anime_link
            response.append(dictionaries)

print(json.dumps(response))
sys.stdout.flush()
