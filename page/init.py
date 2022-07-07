
''' 自媒体后台管理 url'''
# 自媒体
from selenium.webdriver.common.by import By

url_mp ='http://pc-toutiao-python.itheima.net/#/login'


'''以下数据为自媒体模块配置数据'''
# 登录用户名
mp_username = (By.XPATH, '/html/body/div[1]/div/div/form/div[1]/div/div/input')
# 登录验证码
mp_code = (By.XPATH, '/html/body/div/div/div/form/div[2]/div/div/input')
# 登录按钮
mp_login_btn = (By.XPATH, '/html/body/div[1]/div/div/form/div[4]/div/button')
# 已登录的用户名称
mp_login_name = (By.XPATH, '/html/body/div[1]/div/div[2]/div/div[2]/div[2]/div/span')


    # 内容管理
content_management=(By.XPATH, '//*[text()="内容管理"]')
    
#     发布文章
publish_article=(By.XPATH, "//*[contains(text(),'发布文章')]")

# 文章名称
article_title=(By.CSS_SELECTOR, '[placeholder="文章名称"]')
# iframe
mp_iframe=(By.CSS_SELECTOR, '[id="publishTinymce_ifr"]')
# 文章内容
article_contents=(By.CSS_SELECTOR, '[id="tinymce"]')
        

# 选择封面
select_article_covers=(By.XPATH, '//*[text()="自动"]')

# # 选择频道
# select_article_channel=(By.CSS_SELECTOR, '[placeholder="请选择"]')
# # 频道列表
# (By.CSS_SELECTOR, '//*[text()="css"]')
# 点击发表
publish_btn=(By.XPATH, '//*[text()="发表"]')
#     发布文章成功信息
successful_message=(By.XPATH, "//*[contains(text(),'新增文章成功')]")

'''以下数据为app配置数据'''
app_username=By.XPATH, "//*[@index='1' and @class='android.widget.EditText']"
app_code=By.XPATH,"//*[@index='2' and @class='android.widget.EditText']"
app_login_btn=By.XPATH,"//*[@index='4' and @class='android.widget.Button']"

#头条app包与界面
packge_tt="com.itcast.toutiaoApp"
activity_tt=".MainActivity"

