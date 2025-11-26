import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoEcommerce.settings')
import django
django.setup()

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import random
import string
import time

pytestmark = pytest.mark.django_db  # enable DB access

def random_string(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_signup_form(driver):
    username = "User_" + random_string(4)
    password = "Pass_" + random_string(8)

    driver.get("http://127.0.0.1:8000/")

    driver.find_element(By.CSS_SELECTOR, "#id_username").send_keys(username)
    driver.find_element(By.CSS_SELECTOR, "#id_password1").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, "#id_password2").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(3)

    from django.conf import settings
    assert driver.current_url.endswith(settings.LOGIN_REDIRECT_URL)
    print(f"Signup successful: {username}")
