from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import action_chains, keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


"""class DeletePhotos:
    def __init__(self, username, password):
        self.username = str(username)
        self.password = str(password)

    def delete(self):
        chrome_options = Options()
        chrome_options.add_argument("--kiosk")
        browser = webdriver.Chrome('chrome_driver.exe', chrome_options=chrome_options)
        browser.get('http://www.icloud.com')
        WebDriverWait(browser, 60).until(expected_conditions.frame_to_be_available_and_switch_to_it("auth-frame"))
        WebDriverWait(browser, 60).until(expected_conditions.presence_of_element_located((By.ID, "appleId"))).send_keys(
            self.username)
        action_chains.ActionChains(browser).send_keys(keys.Keys.TAB, self.password, keys.Keys.ENTER).perform()
        browser.get('https://www.icloud.com/#photos')
        WebDriverWait(browser, 60).until(expected_conditions.frame_to_be_available_and_switch_to_it("photos"))
        WebDriverWait(browser, True)"""


class Locate:
    def __init__(self, latitude='none', longitude='none'):
        self.url = str(latitude + ' ' + longitude)

    def locate_phone(self):
        chrome_options = Options()
        chrome_options.add_argument("--kiosk")
        browser = webdriver.Chrome('chrome_driver.exe', chrome_options=chrome_options)
        browser.get('https://www.google.co.in')
        WebDriverWait(browser, 60).until(
            expected_conditions.presence_of_element_located((By.NAME, "q"))).send_keys(self.url)
        WebDriverWait(browser, 60).until(
            expected_conditions.presence_of_element_located((By.NAME, "btnK"))).send_keys(keys.Keys.ENTER)
        WebDriverWait(browser, True)
