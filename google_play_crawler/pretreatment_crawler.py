#-*- coding:utf-8
import  time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

test_url = "https://play.google.com/store/apps/category/SHOPPING/collection/topselling_free?hl=en"

def get_app_urls(url):
    FIREFOX_PATH = "F:/WangKang/python_project/crawler_test/geckodriver.exe"
    js = "document.body.scrollTop += 10000"  # 滚动条下拉1000px

    driver=webdriver.Firefox( executable_path=FIREFOX_PATH)
    driver.get(url)
    time.sleep(2)

    see_more = driver.find_element_by_xpath("//div[@id='footer-content']/button[@id='show-more-button']")
    for i in range(0, 500):
        if(see_more.get_attribute("style") == ""):
            see_more.click()
            time.sleep(2)
        driver.find_element_by_tag_name('body').send_keys(Keys.ARROW_DOWN)  # 在这里使用模拟的下方向键
        time.sleep(0.1)
    app_list = driver.find_element_by_xpath(".//div[@id='body-content']//div[@class='main-content']//div[@class='id-card-list card-list two-cards']")
    app_urls = app_list.find_elements_by_xpath("./div[@class='card no-rationale square-cover apps small']//div[@class='details']/a[@class='card-click-target']")

    count = 0;
    for app_url in app_urls:
        count +=1
        print app_url.get_attribute("href")
    print "app url number :" + str(count)

def generate_english_urls():
    origins = open('F:\WangKang\python_project\crawler_test\data\shooping_app_urls.txt', 'r+')
    results=""
    try:
        #拼接成英文url地址。
        for app_url in origins.readlines():
            results =  results + app_url.replace("\n","") + "&hl=en\n"

        origins.write(results)

    finally:
        origins.close()

    new_file = open(r'F:\WangKang\python_project\crawler_test\data\shooping_app_urls.txt', 'w+')
    try:
        new_file.write(results)
    finally:
        new_file.close()


if __name__ == '__main__':
    # get_app_urls(test_url)
    print "start"
    generate_english_urls()
    print "end"
