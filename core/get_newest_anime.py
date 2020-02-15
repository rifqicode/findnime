# @author Muhammad Rifqi <muhammadrifqi.tb@gmail.com>

import sys
from bs4 import BeautifulSoup
import requests
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
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


chrome_options = Options()
chrome_options.add_argument("--headless")

website = requests.get('https://www.samehada.tv/')
if website.status_code == 200:
    websiteContent = BeautifulSoup(website.content , 'html.parser')
    divContent = websiteContent.find(class_="updateanime").find_all(class_="entry-title")

    for l in divContent[0:12]:
        anime_name = l.get_text()
        link = l.find('a').get('href');

        # jump into it
        jumpIntoLink = requests.get(link);
        if jumpIntoLink.status_code == 200:
            jump = BeautifulSoup(jumpIntoLink.content , 'html.parser')

            downloadListGetFormat = jump.find(class_="download-eps").find_all('li')[1].find('a').get('href')

            popup_1 = requests.get(downloadListGetFormat)
            if popup_1.status_code == 200:
                popup_1_content = BeautifulSoup(popup_1.content , 'html.parser')

                driver = webdriver.Chrome(options=chrome_options)
                driver.get(downloadListGetFormat)
                try:
                    wait = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "showlink")))
                    driver.execute_script('changeLink()')
                    driver.close()
                finally:
                    driver.switch_to.window(driver.window_handles[0])

                    try:
                        downloadLink = driver.find_element_by_xpath("//div[@class='download-link']").find_element_by_tag_name('a').get_attribute('href')
                    finally:
                        # write into file
                        write = anime_name + " : \n" + str(downloadLink) + "\n"
                        writeFile('anime_list.txt' , str(write))
                        driver.quit()
