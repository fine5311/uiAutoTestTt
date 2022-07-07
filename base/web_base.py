from time import sleep

# from selenium import webdriver
import allure
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

from base.base import Base
from tools.get_log import GetLog

log=GetLog().get_log()


class WebBase(Base):
    # 根据显示文本点击元素,频道选择
    def web_base_click_element(self,placeholder_text,click_text):
        loc=By.CSS_SELECTOR,'[placeholder="{}"]'.format(placeholder_text)
        self.base_click(loc)
        sleep(1)
        loc=By.XPATH,'//*[text()="{}"]'.format(click_text)
        self.base_click(loc)
# #     切换iframe
#     def switch_iframe(self,idframe1):
#         self.driver.switch_to.frame(idframe1)
#         self.driver.swit







