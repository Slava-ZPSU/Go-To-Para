from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

class BrowserOpener:
    def __init__(self):
        self.__driver = None
        self.__url = 'https://workspace.google.com/products/meet/'
        self.__options = Options()

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, url):
        self.__url = url

    @property
    def driver(self):
        return self.__driver

    @driver.setter
    def driver(self, driver):
        self.__driver = driver

    def open_url(self):
        self.__driver.get(self.__url)

    def start_browser(self):
        self.__options.set_preference("media.navigator.permission.disabled", True)
        self.__options.set_preference("media.navigator.streams.fake", True)
        self.__driver = webdriver.Firefox(options=self.__options)  # або webdriver.Chrome(), залежно від вашого браузера
    def close_browser(self):
        self.__driver.quit()
        print('Browser closed')

    def enter_data_by_id(self, input_id, data):
        input_element = self.__driver.find_element(By.ID, input_id)
        input_element.send_keys(data)
        print('input')

    def enter_data_by_class(self, input_class, data):
        input_element = self.__driver.find_element(By.CLASS_NAME, input_class)
        input_element.send_keys(data)
        print('input')

    def click_button_by_id(self, button_id):
        button = self.__driver.find_element(By.ID, button_id)
        button.click()
        print('click')

    def click_button_by_class(self, button_class):
        button = self.__driver.find_element(By.CLASS_NAME, button_class)
        button.click()
        print('click')