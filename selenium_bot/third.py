from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://www.axcapital.ae/")

time.sleep(2)
driver.find_element(By.XPATH, "//a[text()='Properties on map']").click()
time.sleep(10)
