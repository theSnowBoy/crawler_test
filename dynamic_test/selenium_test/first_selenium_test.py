#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# 测试使用的是phantomjs,相当于看不见的浏览器。
# 如何实现模拟点击？
driver = webdriver.PhantomJS()
web =  "https://www.baidu.com"
driver.get(web)
kw = driver.find_element_by_id("kw")
kw.send_keys("hello")
su = driver.find_element_by_id("su").click()
time.sleep(3) # 需要有时间来接收数据
print driver.page_source
