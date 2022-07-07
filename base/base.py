from time import sleep, time

# from selenium import webdriver
import allure
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

from tools.get_log import GetLog

log=GetLog().get_log()


class Base:
    # 初始化 driver
    def __init__(self, driver):
        log.info("正在初始化driver：{}".format(driver))
        self.driver = driver

    # 查找方法封装
    def base_find(self, loc, timeout=30, poll=0.5):
        """
        :param loc: 元组或列表，内容为元素定位信息
        :param timeout:  等待时间 30s
        :param poll:   查找元素频率 默认0.5
        :return:
        """
        log.info("正在查找元素：{}".format(loc))
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_element(loc[0],loc[1]))

    # 输入方法封装
    def base_input(self, loc, value):
        """

        :param loc: 元组或列表，内容为元素定位信息
        :param value: 需要输入的值
        :return:
        """
        # 获取元素
        # print(loc,value)
        el = self.base_find(loc)
        log.info(el)
        # 清空
        sleep(1)
        # el.clear()
        log.info("正在对元素：{}执行清空".format(loc))
        el.send_keys(Keys.CONTROL, 'a')
        el.send_keys(Keys.DELETE)
        # # 输入
        log.info("正在对元素：{} 执行输入：{}".format(loc,value))
        el.send_keys(value)

    # 点击方法封装
    def base_click(self, loc):
        log.info("正在对元素：{} 执行点击".format(loc))
        self.base_find(loc).click()

    # 获取文本
    def base_text(self, loc):
        log.info("正在查找元素：{} 文本：{}".format(loc,self.base_find(loc).text))
        return self.base_find(loc).text

    # 获取截图
    def base_get_img(self):
       log.error("断言出错，将错误截图写入allure报告")
       self.driver.get_screenshot_as_file('./images/err{}.png'.format(time))
    # 将图片写入报告
       self.__base_write_img()





    def __base_write_img(self):
        #         获取图片文件流
        with open("./images/err.png", 'rb') as f:
            #  调用allure.attach附加方法


             allure.attach(f.read(), '异常截图', allure.attachment_type.PNG)

