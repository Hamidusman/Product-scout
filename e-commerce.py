from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service = Service(executable_path="chromedriver.exe")
url = "https://automationteststore.com/"

driver = webdriver.Chrome(service=service)
driver.get(url)

# This code places a product on cart. Modifications can be implemented for better automation

WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.ID, 'filter_keyword'))
)

search_element = (driver.find_element(By.ID, 'filter_keyword')
                  .send_keys('shirt', Keys.ENTER))

product_data = driver.find_element(By.XPATH, "//*[@id='maincontainer']/div/div/div/div/div[3]/div[2]")
product_data.click()

cart_button = (driver.find_element(By.CLASS_NAME, 'cart')
               .click())

# code functions ass intended, still room for improvements

time.sleep(15)
driver.quit()