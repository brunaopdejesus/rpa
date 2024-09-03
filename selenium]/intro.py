import time
from selenium import webdriver
from selenium.webdriver.common.by import By 

driver = webdriver.Firefox()
driver.get('http://www.google.com/')
time.sleep(5)
search_box = driver.find_element (By.NAME, "q")
search_box.send_keys('Happy Tree Friends')
search_box.submit()
time.sleep(5)
driver.quit()