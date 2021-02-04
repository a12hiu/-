import pytest
from appium import webdriver

from base.base_analyze import analyze_data
from page.add_contact_page import AddContactPage
from page.contact_list_page import ContactListPage
from page.saved_page import SavedPage


class TestContact:

    def setup(self):
        # 创建一个字典，包装相应的启动参数
        desired_caps = dict()
        # 需要连接的手机的平台(不限制大小写)
        desired_caps['platformName'] = 'Android'
        # 需要连接的手机的版本号(比如 5.2.1 的版本可以填写 5.2.1 或 5.2 或 5 ，以此类推)
        desired_caps['platformVersion'] = '5.1'
        # 需要连接的手机的设备号(andoird平台下，可以随便写，但是不能不写)
        desired_caps['deviceName'] = 'huawei p30'
        # 需要启动的程序的包名
        desired_caps['appPackage'] = 'com.android.contacts'
        # 需要启动的程序的界面名
        desired_caps['appActivity'] = '.activities.PeopleActivity'

        # 连接appium服务器
        self.driver = webdriver.Remote('http://192.168.31.50:4723/wd/hub', desired_caps)

        # 创建页面
        self.add_contact_page = AddContactPage(self.driver)
        self.contact_list_page = ContactListPage(self.driver)
        self.saved_page = SavedPage(self.driver)

    def teardown(self):
        self.driver.quit()

    def test_login(self):
        print("123123")
        print("123123")

    @pytest.mark.parametrize("args", analyze_data("contact_data", "test_add_contact"))
    def test_add_contact(self, args):
        name = args["name"]
        phone = args["phone"]

        # 联系人列表 - 点击 - 添加
        self.contact_list_page.click_add_contact()
        # 添加联系人 - 点击 - 本地保存
        self.add_contact_page.click_local_save()
        # 添加联系人 - 输入 - 姓名
        self.add_contact_page.input_name(name)
        # 添加联系人 - 输入 - 电话
        self.add_contact_page.input_phone(phone)
        # 添加联系人 - 点击 - 返回
        self.add_contact_page.click_back()
        # 断言： 保存成功 - 获取 - 大标题的文字  ==  输入的用户名
        assert self.saved_page.get_title_text() == name
