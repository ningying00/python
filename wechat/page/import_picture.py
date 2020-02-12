import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# options = webdriver.ChromeOptions()
# options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
# driver = webdriver.Chrome(options=options)
# #driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
# driver.implicitly_wait(4)
# 添加成员
# 直接定位添加成员
# driver.find_element(*addmemberbutton).click()
# time.sleep(10)
# addmemberbutton = By.CSS_SELECTOR, "#js_contacts121 > div > div.member_colRight > div > div.js_party_info > div.js_has_member > div:nth-child(1) > a.qui_btn.ww_btn.js_add_member"
#
#
# # 直接显示等待
# # WebDriverWait(driver,10).until(expected_conditions.element_to_be_clickable(addmemberbutton))
# # driver.find_element(addmemberbutton).click()
#
# def wait_addmemberbutton(driver):
#     addmemberbutton = By.CSS_SELECTOR, "#js_contacts121 > div > div.member_colRight > div > div.js_party_info > div.js_has_member > div:nth-child(1) > a.qui_btn.ww_btn.js_add_member"
#     size = len(driver.find_elements(By.ID, "username"))
#     if size < 1:
#         driver.find_element(*addmemberbutton)
#     return size >= 1
#
#
# WebDriverWait(driver, 10).until(wait_addmemberbutton)

# t首页通讯录入口

# 素材库上传图片
class TestImportPicture:
    def setup(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        self.driver = webdriver.Chrome(options=self.options)

    def test_import(self):
        self.wait = WebDriverWait(self.driver, 10, 0.5)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.find_element(By.ID, 'menu_manageTools').click()
        self.driver.find_element(By.CSS_SELECTOR, ".manageTools_cnt_items > li:nth-child(5)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".qui_tabNav > li:nth-child(3)").click()
        self.driver.find_element(By.CLASS_NAME, "js_upload_file_selector").click()
        self.driver.find_element(By.ID, "js_upload_input").send_keys("E:\PythonSDET11\wechat\page\test.jpg")
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "material_picCard_cnt_pic")))
        self.driver.find_element(By.CSS_SELECTOR, 'a[d_ck="submit"]').click()
