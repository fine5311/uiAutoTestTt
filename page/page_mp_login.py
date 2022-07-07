from time import sleep

import pytest

from base.base import Base
from base.web_base import WebBase
from page.init import mp_username, mp_code, mp_login_btn, mp_login_name
from tools.get_log import GetLog

log=GetLog().get_log()


class PageMpLogin(WebBase):


    # 输入用户名
    def page_input_name(self, username):

        self.base_input(mp_username, username)

    # 输入验证码
    def page_input_code(self, code):
        self.base_input(mp_code, code)

    # 点击登录
    def page_click_login_btn(self):
        sleep(1)
        self.base_click(mp_login_btn)
        sleep(1)
    # 获取已登陆用户名
    def page_login_name(self):
        return self.base_text(mp_login_name)

    # 组合业务
    def page_login(self, username='13911111111', code='246810'):
        log.info("正在调用自媒体登录业务登录功能，账号：{}，验证码：{}".format(username,code))
        self.page_input_name(username)
        self.page_input_code(code)
        self.page_click_login_btn()
        # return self.page_login_name()
