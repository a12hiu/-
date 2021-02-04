import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait


class Direction:
    UP = "up"
    DOWN = "down"
    LEFT = "left"
    RIGHT = "right"


class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, feature):
        """
        根据某个元组类型的特征来定位元素，同时会让这个元素有等待的效果
        :param feature:
        :return:
        """
        return WebDriverWait(self.driver, 10, 1).until(lambda x: x.find_element(*feature))

    def click(self, feature):
        """
        根据某个元组类型的特征，定位并点击这个元素
        :param feature:
        :return:
        """
        self.find_element(feature).click()

    def input(self, feature, text):
        """
        根据某个元组类型的特征，定位并输入这个元素的内容为 text
        :param feature:
        :return:
        """
        self.find_element(feature).send_keys(text)

    def clear(self, feature):
        """
        根据某个元组类型的特征，定位并输入这个元素的内容为 text
        :param feature:
        :return:
        """
        self.find_element(feature).clear()

    def get_text(self, feature):
        """
        根据某个元组类型的特征，定位并返回这个元素的文字内容
        :param feature:
        :return:
        """
        return self.find_element(feature).text

    def scroll_page_one_time(self, direction=Direction.UP):
        """
        :param direction:
            "up":("Direction" obj) 从下往上
            "down":("Direction" obj) 从上往下
            "left":("Direction" obj) 从右往左
            "right":("Direction" obj) 从左往右
        """
        screen_size = self.driver.get_window_size()
        screen_width = screen_size["width"]
        screen_height = screen_size["height"]

        center_x = screen_width * 0.5
        center_y = screen_height * 0.5
        bottom_x = center_x
        bottom_y = screen_height * 0.75
        top_x = center_x
        top_y = screen_height * 0.25
        left_x = screen_width * 0.25
        left_y = center_y
        right_x = screen_width * 0.75
        right_y = center_y

        if direction == Direction.UP:
            self.driver.swipe(bottom_x, bottom_y, top_x, top_y, 3000)
        elif direction == Direction.DOWN:
            self.driver.swipe(top_x, top_y, bottom_x, bottom_y, 3000)
        elif direction == Direction.LEFT:
            self.driver.swipe(right_x, right_y, left_x, left_y, 3000)
        elif direction == Direction.RIGHT:
            self.driver.swipe(left_x, left_y, right_x, right_y, 3000)
        else:
            raise Exception("请输入正确的参数 'up/down/left/right'")

    def find_element_with_scroll(self, feature, direction=Direction.UP):
        """
        :param feature:
            要找的元素的特征
        :param direction:
            "up": 从下往上
            "down": 从上往下
            "left": 从右往左
            "right": 从左往右
        :return: 如果存在则返回元素，如果不存在则抛出异常
        """
        while True:
            try:
                return self.driver.find_element(*feature)
            except NoSuchElementException:
                old_page_source = self.driver.page_source
                self.scroll_page_one_time(direction)
                time.sleep(2)
                if self.driver.page_source == old_page_source:
                    raise Exception("没有找到对应的元素 with " + str(feature))
