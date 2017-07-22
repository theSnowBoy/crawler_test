#coding:utf-8
#purpose : 1.selenium使用。 2.完成模拟点击的测试。

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains #引入ActionChains鼠标操作类
from selenium.webdriver.common.keys import Keys #引入keys类操作

cap = webdriver.DesiredCapabilities.PHANTOMJS
cap["phantomjs.page.settings.resourceTimeout"] = 1000
# cap["phantomjs.page.settings.loadImages"] = False
# cap["phantomjs.page.settings.localToRemoteUrlAccessEnabled"] = True
driver = webdriver.PhantomJS(desired_capabilities=cap)
driver.get('https://play.google.com/store')
driver.find_element_by_id("action-dropdown-parent-类别").click()
mtype = driver.find_elements_by_xpath('//div[@class="dropdown-submenu"]//a[@class="child-submenu-link"]') #elements
for item in mtype:
    print item.text
