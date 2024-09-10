from selenium import webdriver
from selenium.webdriver.common import By

import time
from selenium.webdriver.firefox.service import Service
from webdriver_mananger.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service as Firefox
from webdriver_mananger.firefox import GeckoDriverManager # type: ignore

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
from selenium.webdriver.common.keys import Keys 

url = "https://www.imdb.com"
driver.get(url)

time.sleep(3)

queryBox = driver.find_element(By.ID, "suggestion-search")
queryBox.send_keys("Rick and Morty")
queryBox.send_keys(Keys.RETURN)