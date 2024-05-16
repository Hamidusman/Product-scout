from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service = Service(executable_path="chromedriver.exe")
url = "https://www.jumia.com.ng/"

driver = webdriver.Chrome(service=service)
driver.get(url)

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, 'q'))
)
search_field = driver.find_element(By.NAME, 'q')
search_field.clear()
search_field.send_keys("Dell Inspiron 15", Keys.ENTER)

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'prd.card_full'))
)
products = driver.find_elements(By.CLASS_NAME, 'prd.card_full')
price = driver.find_element(By.CLASS_NAME, 'curr').text.replace('₦', '')

time.sleep(10)

driver.quit()
