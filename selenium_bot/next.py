import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager


def setup_driver():
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver


def fill_form(wait, form_fields, name, email, phone):
    print("Filling form...")
    form_fields['name'].send_keys(name)
    form_fields['email'].send_keys(email)
    form_fields['phone'].send_keys(phone)
    form_fields['submit'].submit()
    time.sleep(2)


def wait_for_alert_and_confirm(wait, driver, form_id):
    try:
        confirm_btn = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'swal2-confirm')))

        # Screenshotni olishdan oldin kutish
        time.sleep(1)
        take_screenshot(driver, f"screenshots/form{form_id}.png")

        confirm_btn.click()
        time.sleep(2)
    except Exception as e:
        print(f"No alert appeared or error while confirming: {e}")


def close_popup_if_exists(wait):
    try:
        close_btn = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'popup-modal__close-btn')))
        close_btn.click()
        time.sleep(2)
    except:
        print("Popup close button not found or already closed.")


def scroll_to_element(driver, element):
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(2)


def get_form_fields(wait, form_xpath_base):
    return {
        "name": wait.until(EC.presence_of_element_located((By.XPATH, f"{form_xpath_base}/div[1]/input"))),
        "email": wait.until(EC.presence_of_element_located((By.XPATH, f"{form_xpath_base}/div[2]/input"))),
        "phone": wait.until(EC.presence_of_element_located((By.XPATH, f"{form_xpath_base}/div[3]/div/input"))),
        "submit": wait.until(EC.presence_of_element_located((By.XPATH, f"{form_xpath_base}/button")))
    }


def take_screenshot(driver, path):
    # screenshots papkasini yaratish agar mavjud bo'lmasa
    os.makedirs(os.path.dirname(path), exist_ok=True)
    driver.save_screenshot(path)
    print(f"Screenshot saved to {path}")


def main():
    driver = setup_driver()
    wait = WebDriverWait(driver, 30)
    driver.get("https://sales-inquiries.ae/axcapital/al-jazi/")
    print("Started Process")

    # Form 1 - Popup
    wait.until(EC.visibility_of_element_located((By.ID, "popupModal")))
    form1_fields = get_form_fields(wait, '//*[@id="popupModal"]/div/div/div/div[1]/form')
    fill_form(wait, form1_fields, "Test_5", "exem_5@gmail.com", "+998941152480")
    wait_for_alert_and_confirm(wait, driver, 1)
    close_popup_if_exists(wait)

    # Form 2 - About brochure
    scroll_target = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "about-brochure__form")))
    scroll_to_element(driver, scroll_target)
    form2_fields = get_form_fields(wait, '/html/body/div[1]/section[3]/div[3]/div[2]/form')
    fill_form(wait, form2_fields, "Anvar_7", "new_7@gmail.com", "+998902177320")
    wait_for_alert_and_confirm(wait, driver, 2)

    # Form 3 - Footer request
    scroll_target = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "footer-request-a-call__form")))
    scroll_to_element(driver, scroll_target)
    form3_fields = get_form_fields(wait, '/html/body/div[1]/div[2]/section[2]/div/div/div/div[2]/form')
    fill_form(wait, form3_fields, "Anvar_8", "new_9@gmail.com", "+998905175920")
    wait_for_alert_and_confirm(wait, driver, 3)

    print("Ended Process")
    print("Page Title:", driver.title)
    driver.quit()


if __name__ == "__main__":
    main()
