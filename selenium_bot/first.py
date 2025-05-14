# import time
# from selenium import webdriver
#
# driver = webdriver.Chrome()
# try:
#     driver.get("https://github.com/Abdurahmon17/")
#     assert "GitHub" in driver.title
#     time.sleep(5)
#     driver.close()
# except Exception as e:
#     print(e)
# finally:
#     driver.close()



from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Chrome drayverini ishga tushirish
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Sahifani ochish
driver.get("https://www.axcapital.ae/buy/dubai/properties-for-sale")
time.sleep(3)

# Elementni topish va bosish
elements = driver.find_elements(By.CLASS_NAME, "property-card")
if elements:
    elements[0].click()

time.sleep(10)

# Brauzerni yopish
driver.quit()
