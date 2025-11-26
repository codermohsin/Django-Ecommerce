from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager  
from selenium.webdriver.common.by import By
import time
import random
import string

# --- Function to generate random strings ---
def random_string(length=6):
    letters = string.ascii_letters  # a-zA-Z
    return ''.join(random.choice(letters) for _ in range(length))

# --- Generate random username and email ---
username = "User" + random_string(4)
email = f"{username.lower()}@example.com"
password = "TestPassword123"

# --- Browser Options for GitHub Actions ---
options = Options()
options.add_argument("--headless=new")  # Run headless
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")

# Automatically download and use the correct Chrome WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.implicitly_wait(10)  # Wait for elements

try:
    # --- Open Signup Page ---
    driver.get("http://127.0.0.1:8000/accounts/signup/")

    # --- Fill Signup Form ---
    driver.find_element(By.CSS_SELECTOR, "#id_username").send_keys(username)
    driver.find_element(By.CSS_SELECTOR, "#id_email").send_keys(email)
    driver.find_element(By.CSS_SELECTOR, "#id_password1").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, "#id_password2").send_keys(password)

    # --- Submit Form ---
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # --- Optional: Wait and verify redirect ---
    time.sleep(3)
    print(f"Signed up with username: {username}, email: {email}")

finally:
    driver.quit()
