#coding=utf-8
from selenium import webdriver
import time

#浏览器路径
FIREFOX_PATH = "F:/WangKang/python_project/crawler_test/geckodriver.exe"

driver=webdriver.Firefox( executable_path=FIREFOX_PATH)
# url='http://www.baidu.com'
url = "http://blog.csdn.net/thesnowboy_2"
driver.get(url)
print driver.find_element_by_xpath(".").text