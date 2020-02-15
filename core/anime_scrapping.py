
__author__ = "Muhammad Rifqi Imam Saputra"
__version__ = "0.1"
__maintainer__ = "Muhammad Rifqi Imam Saputra"
__email__ = "muhammadrifqi.tb@gmail.com"
__status__ = "beta"

from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

class AnimeScrapping():

    def __init__(self):
        self.website = "https://www.samehada.tv"
        self.chrome_options = Options()
        # self.chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.get(self.website)


    def writeFile(filename , text):
        file = open(filename, "a")
        file.write(text)
        file.close()
        return 'ok'


    def get_new_anime(self):
        link = []
        div_anime = self.driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div[2]/div[1]").find_elements_by_tag_name('li')

        for link in div_anime:
            link.find_element_by_tag_name('a').click()

            # phase 1
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME , "download-eps")))
            # self.driver.find_element_by_xpath("//div[@class='download-eps']").find_elements_by_tag_name('li')[1].find_element_by_tag_name('a').click()
            # self.driver.switch_to.window(self.driver.window_handles[1])
            #
            # # phase 2
            # wait = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "showlink")))
            # self.driver.execute_script('changeLink()')
            # self.driver.switch_to.window(self.driver.window_handles[2])
            #
            # # save link
            # link.append(self.driver.find_element_by_xpath("//div[@class='download-link']").find_element_by_tag_name('a').get_attribute('href'))
            # self.driver.close()
            # self.driver.close()

    def clear(self):
        clear()
