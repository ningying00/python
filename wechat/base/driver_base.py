from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


class Driver:
    base_url = ""

    def __init__(self, driver: WebDriver = None, reuse=False):
        if driver is None:
            if reuse:
                self.options = webdriver.ChromeOptions()
                self.options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
                self.driver = webdriver.Chrome(options=self.options)
            else:
                self.driver = webdriver.Chrome()

            if self.base_url != "":
                self.driver.get(self.base_url)

        else:
            self.driver = driver
        self.driver.implicitly_wait(2)

    def close(self):
        sleep(20)
        self.driver.quit()
