#-*- coding:utf-8
from selenium import webdriver
import time

import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

def craw_one_app_reviews():
    #浏览器路径
    FIREFOX_PATH = "F:/WangKang/python_project/crawler_test/geckodriver.exe"

    driver=webdriver.Firefox( executable_path=FIREFOX_PATH)
    # url='http://www.baidu.com'
    url = "https://play.google.com/store/apps/details?id=com.google.android.youtube&hl=en"
    driver.get(url)
    time.sleep(3)
    reviews = driver.find_element_by_xpath(".//div[@data-load-more-section-id='reviews']")

    results = []
    for i in range(0,5):
        reviews.find_element_by_xpath("./button[@aria-label='See More']").click()
        time.sleep(1.5)
        single_reviews = reviews.find_elements_by_xpath(".//div[@class='expand-page' and @style='width: 100%; opacity: 1;']//div[@class='single-review']")

        for single_review in single_reviews:
            result = []
            if(single_review.find_element_by_xpath("./div[@class='review-header']//span[@class='author-name']").text == ''):
                print "what?"

            author = single_review.find_element_by_xpath("./div[@class='review-header']//span[@class='author-name']").text
            review_date = single_review.find_element_by_xpath("./div[@class='review-header']//span[@class='review-date']").text
            review_score = single_review.find_element_by_xpath("./div[@class='review-header']//div[@class='current-rating']").get_attribute("style")
            review_title = single_review.find_element_by_xpath("./div[@class='review-body with-review-wrapper']/span[@class='review-title']").text
            review_body = single_review.find_element_by_xpath("./div[@class='review-body with-review-wrapper']").text
            result.extend([author,review_date,review_score,review_title,review_body])
            results.append(result)
            print '评论作者：'+ author
            print '评论日期：'+ review_date
            print '评分：'+ review_score
            print '评论题目：' + review_title
            print '评论内容：'+ review_body
    print results

'''
抽取评论的评分。
举例：
score_raw = 'width: 100%;' ## 数据形式
目的在于抽取出：100
'''
def extract_review_score(review_score):
    return 5 * (float(review_score[7:-2])/100)##评分计算公式 OR 也可以采用百分制。


if __name__=='__main__':
    print "start"

    print "end"




