from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class AddContactPage(BaseAction):
    local_save_button = By.XPATH, "//*[@text='本地保存']"
    name_edit_text = By.XPATH, "//*[@text='姓名']"
    phone_edit_text = By.XPATH, "//*[@text='电话']"
    back_button = By.XPATH, "//*[@content-desc='向上导航']"

    def click_local_save(self):
        self.click(self.local_save_button)

    def input_name(self, text):
        self.input(self.name_edit_text, text)

    def input_phone(self, text):
        self.input(self.phone_edit_text, text)

    def click_back(self):
        self.click(self.back_button)