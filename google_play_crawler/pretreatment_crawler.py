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


    for i in range(0, 200):
        driver.find_element_by_tag_name('body').send_keys(Keys.ARROW_DOWN)  # 在这里使用模拟的下方向键
        time.sleep(0.1)
    app_list = driver.find_element_by_xpath(".//div[@id='body-content']//div[@class='main-content']//div[@class='id-card-list card-list two-cards']")
    app_urls = app_list.find_elements_by_xpath("./div[@class='card no-rationale square-cover apps small']//div[@class='details']/a[@class='card-click-target']")
    count = 0;
    for app_url in app_urls:
        # if(app_url.get_attribute("aria-hidden") == "true"):
        count +=1
        print app_url.get_attribute("href")
    print "app url number :" + str(count)

if __name__ == '__main__':
    get_app_urls(test_url)
