from time import sleep

import pytest

from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.read_json import get_app_login


class TestAppLogin:

    def setup_class(self):
        self.driver = GetDriver().get_app_driver()
        self.app_login = PageIn(self.driver).get_page_app_login()
        sleep(2)
    def teardown_class(self):
        pass

    def setup(self):
        pass

    def teardown(self):
        GetDriver().quit_app_driver()

    @pytest.mark.parametrize("username,code", get_app_login("app_login.json"))
    def test_app_login(self,username,code):
        self.app_login.page_app_login(username,code)
        try:
            assert  True == self.app_login.page_is_exits()
            print("登录成功")
        except Exception as e:
            log.error("错误信息：{}".format(e))
            self.app_login.base_get_img()
            raise


