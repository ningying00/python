from selenium.webdriver.common.by import By

from wechat.base.driver_base import Driver
from wechat.page.admin_address_page import AdminAddressPage


class AdminHomePage(Driver):
    """后台首页"""

    # def __init__(self):
    #     super(Driver,self).__init__()
    #     self.url = "https://work.weixin.qq.com/wework_admin/frame"

    def goto_add_member(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.find_element(By.CLASS_NAME, "index_service_cnt_item_title").click()
        return AdminAddressPage(self.driver).add_member()

    def goto_import_address_book(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.find_element(By.CSS_SELECTOR, '.js_service_list>:nth-child(2)').click()
        return AdminAddressPage(self.driver).import_file()

    def join_member(self):
        pass



