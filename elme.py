from selenium import webdriver
from bs4 import BeautifulSoup
import time
# 登陆界面
driver = webdriver.Chrome()
url = 'https://wordpress-edu-3autumn.localprod.forc.work/wp-login.php'
driver.get(url)
time.sleep(2)
login_name = driver.find_element_by_id('user_login')
login_name.send_keys('spiderman')
time.sleep(1)
password = driver.find_element_by_name('pwd')
password.send_keys('crawler334566')
time.sleep(1)
submit = driver.find_element_by_id('wp-submit')
submit.click()
time.sleep(2)
# 选择文章并发表评论
text_link = driver.find_element_by_partial_link_text('同九义何汝秀')
text_link.click()
time.sleep(1)
comment = driver.find_element_by_name('comment')
comment.send_keys('selenium is good')
sub = driver.find_element_by_class_name('submit')
sub.click()
time.sleep(10)
driver.close()
