from page.page_app_login import PageAppLogin
from page.page_mp_article import PageMpArticle
from page.page_mp_login import PageMpLogin


class PageIn():
    def __init__(self, driver):
        self.driver = driver

    def page_get_page_mp_login(self):
        return PageMpLogin(self.driver)

    def page_page_mp_publish(self):
        return PageMpArticle(self.driver)

    def get_page_app_login(self):
        return PageAppLogin(self.driver)

