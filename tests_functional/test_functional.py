from lib2to3.pgen2 import driver
import time
from django.test import LiveServerTestCase
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from rest_framework import status

class HostTest(LiveServerTestCase):

    def test_landing_page_in_chrome(slef):

        driver = webdriver.Chrome()
        driver.get('http://127.0.0.1:8000/')
        time.sleep(5)
        assert "Contacts List API" in driver.title

    def test_landing_page_in_firefox(self):

        options = webdriver.FirefoxOptions()
        options.headless = True
        driver = webdriver.Firefox(executable_path="./geckodriver")

        driver.get('http://127.0.0.1:8000/')

        time.sleep(5)
        assert "Contacts List API" in driver.title
       


class ContactModelsTest(LiveServerTestCase):

    def test_contacts(self):
        driver = webdriver.Chrome()

        driver.get('http://127.0.0.1:8000')

        contacts = driver.find_element_by_id('operations-tag-contacts')

        assert contacts in driver.page_source

class LoginFormTest(LiveServerTestCase):
    
    def test_login_with_chrome(self):
        options = Options()
        options.headless = True
        driver = webdriver.Chrome(executable_path="./chromedriver")

        driver.get(('%s%s' %(self.live_server_url, '/accounts/login/')))

        time.sleep(3)

        user_name = driver.find_element_by_name('username')
        user_password = driver.find_element_by_name('password')

        time.sleep(3)

        submit = driver.find_element_by_id('submit-id-submit')

        user_name.send_keys('admin')
        user_password.send_keys('admin')

        submit.send_keys(Keys.RETURN)

        assert 'admin' in driver.page_source

    def test_login_with_firefox(self):
        driver = webdriver.Firefox(executable_path="./geckodriver")

        driver.get('http://localhost:8000/accounts/login/')

        wait = WebDriverWait(driver, 10)

        
        user_name = driver.find_element_by_name('username')
        user_password = driver.find_element_by_name('password')

        time.sleep(3)

        submit = driver.find_element_by_id('submit-id-submit')

        user_name.send_keys('ivar')
        user_password.send_keys('ivar')

        submit.send_keys(Keys.RETURN)

        # wait.until(EC.visibility_of_element_located((By.ID, "submit-id-submit")))  

        assert 'ivar' in driver.page_source
    
        