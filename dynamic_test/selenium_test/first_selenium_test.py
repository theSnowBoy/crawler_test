#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# 测试使用的是phantomjs,相当于看不见的浏览器。
# 如何实现模拟点击？
def first_test():
    driver = webdriver.PhantomJS()
    web =  "https://www.baidu.com"
    driver.get(web)
    kw = driver.find_element_by_id("kw")
    kw.send_keys("hello")
    su = driver.find_element_by_id("su").click()
    time.sleep(3) # 需要有时间来接收数据
    print driver.page_source


def get_url_from_csdn():
    driver = webdriver.PhantomJS()
    home_page = "http://blog.csdn.net/TheSnowBoy_2/article/list/"
    url_list = []
    for i in range(1,13):
        time.sleep(1)
        driver.get( home_page+ str(i))
        link_titles = driver.find_elements_by_xpath("//div[@id='article_list']//span[@class='link_title']/a")
        for link_title in link_titles:
            url_list.append(link_title.get_attribute("href"))
    driver.close()
    return  url_list


def save_url_data(file_name, url_list):
    fh = open(file_name, 'w')
    for url in url_list:
        fh.write(url + '\n')
    fh.close()

def visit():
    # flush flow .
    from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
    import random
    dcap = dict(DesiredCapabilities.PHANTOMJS)
    dcap["phantomjs.page.settings.userAgent"] = (
        "User-Agent,Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0"
    )
    fh = open("./url","r")
    urls = fh.readlines()
    while (1):
        driver = webdriver.PhantomJS(desired_capabilities=dcap)
        driver.delete_all_cookies()
        for url in urls:
            time.sleep(20)
            driver.get(url)
            print "visiting url : " + url
        driver.close()
        time.sleep(50)
    fh.close()

## test.
print "start"


# url_list = get_url_from_csdn()
# save_url_data("./url", url_list)
visit()
print "end"