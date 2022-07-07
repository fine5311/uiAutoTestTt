# import appium.webdriver
from time import sleep

import appium
from selenium import webdriver as  BW
from appium import  webdriver

from page.init import packge_tt, activity_tt


class GetDriver:
    # 1.声明变量
    __web_driver = None
    __app_driver = None

    # 获取driver
    @classmethod
    def get_app_driver(cls):
        if cls.__app_driver is None:
            desired_caps = dict()
            desired_caps['platformName'] = 'Android'
            desired_caps['platformVersion'] = '5.1'
            desired_caps['deviceName'] = '192.168.56.101:5555'
            desired_caps['appPackage'] = packge_tt
            desired_caps['appActivity'] = activity_tt
            desired_caps['unicodeKeyboard'] = True

            desired_caps['resetKeyboard'] = True
            cls.__app_driver=appium.webdriver.Remote("http://localhost:4723/wd/hub",desired_caps)
        return cls.__app_driver

    @classmethod
    def quit_app_driver(cls):
        if cls.__app_driver is not None:
            cls.__app_driver.quit()
            # 置空操作
            cls.__app_driver = None



    @classmethod
    def get_web_driver(cls, url):
        if cls.__web_driver is None:
            cls.__web_driver = BW.Chrome()
            cls.__web_driver.maximize_window()
            cls.__web_driver.get(url)


        return cls.__web_driver

    @classmethod
    def quit_web_driver(cls):
        if cls.__web_driver is not None:
            cls.__web_driver.quit()
            # 置空操作
            cls.__web_driver = None
if __name__ == '__main__':
     GetDriver().get_app_driver()