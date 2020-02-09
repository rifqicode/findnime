# @author Muhammad Rifqi <muhammadrifqi.tb@gmail.com>

import sys
from bs4 import BeautifulSoup
import requests
import json
import urllib2
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

def writeFile(filename , text):
    file = open(filename, "a")
    file.write(text)
    file.close()
    return 'ok'

def post(url , datas):
    headers = {
        'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
        'Cache-Control': "no-cache"
    }

    return requests.request("POST", url, data=datas, headers=headers)


website = requests.get('https://www.samehada.tv/')
if website.status_code == 200:
    websiteContent = BeautifulSoup(website.content , 'html.parser')
    divContent = websiteContent.find(class_="updateanime").find_all(class_="entry-title")

    for l in divContent[0:1]:
        link = l.find('a').get('href');

        # jump into it
        jumpIntoLink = requests.get(link);
        if jumpIntoLink.status_code == 200:
            jump = BeautifulSoup(jumpIntoLink.content , 'html.parser')

            downloadListGetFormat = jump.find(class_="download-eps").find_all('li')[1].find('a').get('href')

            popup_1 = requests.get(downloadListGetFormat)
            if popup_1.status_code == 200:
                popup_1_content = BeautifulSoup(popup_1.content , 'html.parser')

                driver = webdriver.Chrome()
                driver.get(downloadListGetFormat)

                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "showlink")))
                driver.execute_script('changeLink()')

                popup_2 = requests.get(driver.current_url);
                driver.close()

                if popup_2.status_code == 200:
                    popup_2_content = BeautifulSoup(popup_2.content , 'html.parser')
                    jump2 = popup_2_content.find(class_="download-link"),find('a').get('href')

                    popup_3 = requests.get(jump2)
                    if jump3.status_code == 200:
                        popup_3_content = BeautifulSoup(popup_3.content , 'html.parser')


                # exit()
                # writeFile('index.html' , str(go))
