import pytest

from page.page_in import PageIn

from tools.get_driver import GetDriver
from page.init import url_mp
from tools.read_json import get_mp_login, get_mp_publish
from tools.get_log import GetLog

log = GetLog().get_log()


class TestMpLogin:

    def setup_class(self):
        # 获取driver

        self.driver = GetDriver().get_web_driver(url_mp)
        # driver.find_element()
        pageIn= PageIn(self.driver)
        pageIn.page_get_page_mp_login().page_login()
        self.mp=pageIn.page_page_mp_publish()





    def teardown_class(self):
        GetDriver().quit_web_driver()
        # pass

    def setup(self):
        pass
    def teardown(self):
        self.mp.page_click_content_management()

    @pytest.mark.parametrize("title,content,channel", get_mp_publish("mp_publish.json"))
    def test_mp_publish(self, title, content, channel):
        self.mp.page_publish(title, content, channel)
        try:
         assert self.mp.get_successful_message() =="新增文章成功"
        except Exception as  e :
            log.error("错误信息：{}".format(e))
            print("错误原因", e)
            #           输出错误截图
            self.mp.base_get_img()
            #             抛出异常
            raise

# if __name__ == '__main__':
#     pytest.main(['-s','test01_mp_login.py'])
