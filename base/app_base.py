from time import sleep

from selenium.webdriver.support.wait import WebDriverWait

from base.base import Base
from tools.get_log import GetLog
from tools.keyboard_keys import number_CODE

log = GetLog().get_log()


class AppBase(Base):
    # 查找元素
    def app_base_is_exist(self, loc):
        try:
            self.base_find(loc)

            return False
        except Exception as e:

            return True

    #     app输入通过键盘
    def app_base_input(self, value):
        # el=self.base_find(loc)
        for i in list(value):
            self.driver.press_keycode(number_CODE[i])
