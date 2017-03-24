#coding=utf-8
from selenium import webdriver
import time
#TODO 有问题代码
# 设置代理。
profile = webdriver.FirefoxProfile()
profile.set_preference('network.proxy.type', 1)   #默认值0，就是直接连接；1就是手工配置代理。
profile.set_preference('network.proxy.http', "116.242.227.201")
profile.set_preference('network.proxy.http_port', "3128")
# profile.set_preference('network.proxy.ssl',ip)
# profile.set_preference('network.proxy.ssl_port', port)
profile.update_preferences()
driver=webdriver.Firefox(profile)
# url='http://www.baidu.com'
url = 'http://apk.hiapk.com/web/api.do?qt=1701&id=4445482&pi=100&ps=10'
driver.get(url)
print driver.find_element_by_xpath(".").text