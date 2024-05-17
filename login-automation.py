from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import  ChromeDriverManager


url = "https://practicetestautomation.com/"

service = Service(executable_path="chromedriver.exe")

driver = webdriver.Chrome(service=service)
driver.get(url)

links = driver.find_element(By.ID, "menu-item-20")
links.click()


time.sleep(10)
driver.quit()