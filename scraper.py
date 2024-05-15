from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path="chromedriver.exe")
url = "https://www.jumia.com.ng/"

driver = webdriver.Chrome(service=service)
driver.get(url)
time.sleep(10)

driver.quit()
