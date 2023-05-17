from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Create a new instance of the Firefox driver
driver = webdriver.Firefox()

# Go to the website
driver.get('https://www.thelancet.com/journals/lancet/issue/vol401no10388/PIIS0140-6736(23)X0019-1')

# Wait for the cookies button to load and then click it
try:
    accept_cookies_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Accept all cookies"]')))
    accept_cookies_button.click()
except Exception as e:
    print(f"Couldn't click the accept cookies button due to: {e}")

time.sleep(5)

# Wait for the Full-Text HTML link to load and then click it
try:
    full_text_html_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Full-Text HTML')))
    full_text_html_link.click()
except Exception as e:
    print(f"Couldn't click the Full-Text HTML link due to: {e}")

time.sleep(10)

# Close the browser
driver.quit()
