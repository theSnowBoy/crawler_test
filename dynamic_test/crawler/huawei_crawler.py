#-*- coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def get_driver():
    dcap = dict(DesiredCapabilities.PHANTOMJS)
    dcap["phantomjs.page.settings.userAgent"] = (
        "User-Agent,Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0"
    )
    # driver = webdriver.PhantomJS(desired_capabilities=dcap)
    driver = webdriver.PhantomJS()
    return driver
def get_urls(app_list_page):

    driver = get_driver()
    urls = []
    url_app_list = []
    url_app_list.append(app_list_page)

    driver.get(app_list_page)
    time.sleep(2)
    # 1.获得最后一页的id.
    last_url = driver.find_element_by_xpath("//div[@id='appListPage']/a[last()]").get_attribute("href")
    list_base = last_url[0:len(last_url)-2]
    last_num = int( last_url[-1] )
    print last_url[-1]

    # 2.计算中间的网页。
    for i in range(2,last_num):
        url_app_list.append(list_base + str(i))


    # 3.循环爬取urls.
    for url_app in url_app_list:
        driver.get(url_app)
        time.sleep(2)
        print driver.title
        titles = driver.find_elements_by_xpath("//div[@class='unit-main']//h4[@class='title']/a")
        for title in titles:
            urls.append(title.get_attribute("href"))

    driver.close()
    print len(urls)
    return  urls

def save_url_data(file_name, url_list):
    fh = open(file_name, 'w')
    for url in url_list:
        fh.write(url + '\n')
    fh.close()
def read_url_data(file_name):
    fh = open(file_name,"r")
    urls = fh.readlines()
    return urls

def save_db(results):
    import db.get_app_info as app_info
    print "inserting ..."
    dbHelper = app_info.DBHelper(db="test_app")
    sql = "INSERT IGNORE INTO app_huawei(app_title,download,file_size,updata_date,developer_name,version_code) VALUES (%s,%s,%s,%s,%s,%s)"
    dbHelper.insert_app_info(sql,results)

def get_one_app_data(url):
    '''
    示例：
    get_one_app_data("http://appstore.huawei.com/app/C140471")
    '''
    result = []
    driver = get_driver()
    driver.get(url)
    time.sleep(1)
    #TODO 未进行预处理
    print driver.title
    main_part = driver.find_element_by_xpath("//div[@class='unit-main detail-part']")

    title  = main_part.find_element_by_xpath("//span[@class='title']")
    download = driver.find_element_by_xpath("//span[@class='grey sub']")
    app_info = driver.find_elements_by_xpath("//ul[@class='app-info-ul nofloat']/li[@class='ul-li-detail']/span")
    result.append(title.text)
    result.append(download.text)

    for app in app_info:
        result.append(app.text)
    return result

    for data in result:
        print data

    # test ------------------------------------------------------
# 1. 获取不同 app 的链接。
# app_urls = get_urls("http://appstore.huawei.com/game/list_2_2_1")
path = "../../test/slenium_test/huawei_app_urls"
# import os
# if not os.path.exists(path):
#     os.open(path,os.O_CREAT)
#
# # 2.保存app url 连接。
# save_url_data(path,app_urls)

# 3.打开文件，读取url并且访问。
urls = read_url_data(path)
app_results = []
# for url in urls:
#     app_results.append(get_one_app_data(url))
for i in range(0,3):
    app_results.append(get_one_app_data(urls[i]))

#4.保存
save_db(app_results)










