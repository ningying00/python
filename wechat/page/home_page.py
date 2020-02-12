from selenium.webdriver.common.by import By

from wechat.base.driver_base import Driver
from wechat.page.login_page import Login


class HomePage(Driver):
    """首页"""
    def login(self):
        self.driver.find_element(By.CLASS_NAME,"index_top_operation_loginBtn").click()
        return Login(self.driver)



