from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import os

username = os.environ["USERNAME"]
password = os.environ["PASSWORD"]

# Set up headless Chrome
options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

try:
    # Step 1: Open login page
    driver.get("https://solugenix.talentoz.com/Weblogin.aspx")
    time.sleep(2)

    # Step 2: Fill username and password
    driver.find_element(By.ID, "txt_name").send_keys(username)
    driver.find_element(By.ID, "txt_pass").send_keys(password)

    # Step 3: Click Sign In
    driver.find_element(By.ID, "btn_submit").click()
    time.sleep(4)

    # Step 4: Go to Home page (if not auto)
    driver.get("https://solugenix.talentoz.com/Home.aspx")
    time.sleep(4)

    # Step 5: Click "Check In"
    driver.find_element(By.XPATH, "//div[text()='Check In']").click()
    time.sleep(2)

    print("Check-in successful.")
finally:
    driver.quit()
