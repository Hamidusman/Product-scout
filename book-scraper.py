from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


service = Service(executable_path="chromedriver.exe")
url = "https://www.audible.com/search"

driver = webdriver.Chrome(service=service)
driver.get(url)

WebDriverWait(driver, 15). until(
    EC.presence_of_element_located((By.CLASS_NAME, 'productListItem'))
)

item_element = driver.find_elements(By.CLASS_NAME, "productListItem")
title = []
author = []
ratings = []

for item in item_element:
    title.append(item.find_element(By.XPATH, './/h3[contains(@class, "bc-heading")]')
                 .text)
    author.append(item.find_element(By.XPATH, './/li[contains(@class, "authorLabel")]')
                  .text)
    ratings.append(item.find_element(By.XPATH, './/li[contains(@class, "ratingsLabel")]')
                   .text)

book_df = pd.DataFrame(
            {'title': title, 'author': author, 'ratings': ratings}
           )

time.sleep(10)
driver.quit()

book_df.to_csv('book_df', index=False)