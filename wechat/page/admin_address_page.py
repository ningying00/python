from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from wechat.base.driver_base import Driver


class AdminAddressPage(Driver):
    """后台通讯录"""

    # def __init__(self):
    #     super(Driver, self).__init__()
    #     self.url = "https://work.weixin.qq.com/wework_admin/frame#contacts"

    def add_member(self, username=1, account=1, phone=1):
        """添加用户"""
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")

        # 点击添加成员按钮
        def wait_addmemberbutton(driver):
            addmemberbutton = By.CSS_SELECTOR, 'js_has_member>div:nth-of-type(1)>a:nth-of-type(1)'
            size = len(self.driver.find_elements(By.ID, "username"))
            if size < 1:
                self.driver.find_element(*addmemberbutton)
            return size >= 1

        WebDriverWait(self.driver, 20).until(wait_addmemberbutton)
        # add_pade = self.driver.execute_script("return document.documentElement.outerHTML")
        self.driver.find_element(By.ID, 'username').send_keys(username)
        self.driver.find_element(By.ID, 'memberAdd_acctid').send_keys(account)
        # 定位性别
        # self.
        self.driver.find_element(By.ID, 'memberAdd_phone').send_keys(phone)
        self.driver.find_element(By.CSS_SELECTOR, '.js_btn_save').click()
        result_pade = self.driver.execute_script("return document.documentElement.outerHTML")
        return result_pade

    def search(self):
        pass

    def import_file(self):
        pass

    def edit_user(self,username):
        """编辑成员"""
        self.driver.implicitly_wait(2)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        user=(By.CSS_SELECTOR,".js_list>:nth-child(1)>:nth-child(2)")
        WebDriverWait(self.driver, 10, 0.5).until(expected_conditions.presence_of_element_located(user))
        self.driver.find_element(*user).click()
        self.driver.find_element(By.CLASS_NAME,"js_edit").click()
        self.driver.find_element(By.NAME,"username").clear()
        self.driver.find_element(By.NAME,"username").send_keys(username)
        save=(By.CLASS_NAME,".js_member_editor_form>div:nth-child(3)>a:nth-child(1)")
        WebDriverWait(self.driver,10,0.5).until(expected_conditions.presence_of_element_located(save))
        self.driver.find_element(*save).click()
