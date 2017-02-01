#coding=utf-8
# 获取安卓市场上的评论信息。
from selenium import webdriver
import time

driver=webdriver.Firefox()
url= 'http://apk.hiapk.com/appinfo/com.tencent.mm/900'
driver.get(url)

def  get_start_info():
    start_lines = driver.find_elements_by_xpath("//div[@class='left star_detail_box']/div[@class='star_line']")
    for start_line in start_lines:
        data = start_line.find_element_by_xpath("./div[@class='star_per_line']/div[2]")
        print data.text

def get_some_comment_info():
     comment_items = driver.find_elements_by_xpath("//div[@class='comment_list']/div[@class='comment_item']")
     print "get comment items size :" + str(len(comment_items))
     for comment_item in comment_items:
         comment_content = comment_item.find_element_by_xpath("./div[1]/div[@class='comment_right']/div[@class='comment_content']")
         print comment_content.text

def get_all_comment():
    time.sleep(2)
    next_page = driver.find_element_by_xpath("//div[@id='cmtPage']/div[1]/span[@class='page_item page_next page_able']")
    next_page.click()

if __name__=='__main__':
    print "start"
    get_all_comment()
    get_some_comment_info()
