from time import sleep

from base.app_base import AppBase
from page.init import app_username, app_code, app_login_btn


class PageAppLogin(AppBase):
    # 输入用户名
    def page_input_username(self,username):
        self.base_click(app_username)
        sleep(1)
        self.app_base_input(username)

    # 输入验证码
    def page_input_code(self,code):
        self.base_click(app_code)
        sleep(1)
        self.app_base_input(code)
    # 点击登录
    def page_click_login(self):
        self.base_click(app_login_btn)
        sleep(2)

    def page_is_exits(self):
       return self.app_base_is_exist(app_login_btn)

    def page_app_login(self,username="123456789", code="1111"):
        self.page_input_username(username)
        self.page_input_code(code)
        self.page_click_login()

