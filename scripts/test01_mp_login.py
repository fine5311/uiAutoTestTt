import pytest

from page.page_in import PageIn

from tools.get_driver import GetDriver
from page.init import url_mp
from tools.read_json import get_mp_login
from tools.get_log import GetLog

log=GetLog().get_log()

class TestMpLogin:

    def setup_class(self):
        # 获取driver

        self.driver = GetDriver().get_web_driver(url_mp)
        # driver.find_element()
        self.mp = PageIn(self.driver).page_get_page_mp_login()

    def teardown_class(self):
        GetDriver().quit_web_driver()
        # pass

    def setup(self):
        pass

    @pytest.mark.parametrize("username,code,expect", get_mp_login("mp_login.json"))
    def test_mp_login(self, username, code, expect):
        # print(username, code, expect)
        self.mp.page_login(username, code)
        try:
            assert expect == self.mp.page_login_name()
        except Exception as e:
            log.error("错误信息：{}".format(e))
            # 输出错误信息
            print("错误原因",e)
#           输出错误截图
            self.mp.base_get_img()
#             抛出异常
            raise


if __name__ == '__main__':
    pytest.main(['-s','test01_mp_login.py'])
