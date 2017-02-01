#coding=utf-8
from selenium import webdriver
import time

driver=webdriver.Firefox()
url='http://www.baidu.com'
driver.get(url)
kw = driver.find_element_by_id("kw")
kw.send_keys("hello")
su = driver.find_element_by_id("su").click()
time.sleep(3) # 需要有时间来接收数据