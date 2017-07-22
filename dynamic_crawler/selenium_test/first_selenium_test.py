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

USER_AGENTS = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
]

def visit():
    # flush flow .
    from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
    import random
    visit_times = 0;
    dcap = dict(DesiredCapabilities.PHANTOMJS)

    fh = open("./url","r")
    urls = fh.readlines()
    while (1):
        dcap["phantomjs.page.settings.userAgent"] = (random.choice(USER_AGENTS))  # 随机生成user-agent
        driver = webdriver.PhantomJS(desired_capabilities=dcap)
        driver.delete_all_cookies()
        for url in urls:
            time.sleep(20)
            driver.get(url)
            print "visiting url : " + url
            visit_times += 1
            print "visit count is : " + str(visit_times)
        driver.close()
        time.sleep(50)
    fh.close()

## test.
print "start"
url_list = get_url_from_csdn()
save_url_data("./url", url_list)
visit()
print "end"