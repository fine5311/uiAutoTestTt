from time import sleep


from base.base import Base
from base.web_base import WebBase
from page.init import mp_username, mp_code, mp_login_btn, mp_login_name, content_management, publish_article, \
    article_title, mp_iframe, article_contents, select_article_covers, publish_btn, successful_message
from page.page_mp_login import PageMpLogin
from tools.get_log import GetLog

log=GetLog().get_log()


class PageMpArticle(WebBase):
    # 内容管理
    def page_click_content_management(self):
        self.base_click(content_management)
        sleep(1)
#     发布文章
    def page_click_publish_article(self):
        self.base_click(publish_article)
        sleep(1)
# 文章名称
    def page_input_article_title(self,title):
        self.base_input(article_title,title)
        sleep(1)
# 文章内容
    def page_input_article_contents(self,content):
        iframe=self.base_find(mp_iframe)
        self.driver.switch_to.frame(iframe)
        self.base_input(article_contents,content)
        self.driver.switch_to.default_content()
        sleep(1)

# 选择封面
    def page_select_article_covers(self):
        self.base_click(select_article_covers)
        sleep(1)

# 图片上传
# 选择频道
    def page_select_article_channel(self,channel):

        self.web_base_click_element('请选择',channel)
        sleep(1)
# 点击发表
    def page_click_publish_btn(self):
        self.base_click(publish_btn)

# 获取发表成功信息
    def get_successful_message(self):
       return self.base_text(successful_message)

#  组合业务方法
    def page_publish(self,title,content,channel):
        self.page_click_content_management()
        self.page_click_publish_article()
        self.page_input_article_title(title)
        self.page_input_article_contents(content)
        self.page_select_article_covers()
        self.page_select_article_channel(channel)
        self.page_click_publish_btn()