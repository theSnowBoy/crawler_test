#-*- coding:utf-8
from selenium import webdriver
import time
import datetime
import traceback
import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

'''
 url 格式实例： "https://play.google.com/store/apps/details?id=com.google.android.youtube&hl=en"
'''
def craw_one_app_reviews(url):
    #浏览器路径
    FIREFOX_PATH = "F:/WangKang/python_project/crawler_test/geckodriver.exe"

    driver=webdriver.Firefox( executable_path=FIREFOX_PATH)
    # url='http://www.baidu.com'

    driver.get(url)
    time.sleep(3)
    reviews = driver.find_element_by_xpath(".//div[@data-load-more-section-id='reviews']")
    apk_id = reviews.get_attribute("data-load-more-docid")

    results = []
    review_id = 1;
    for i in range(0,200): # 设置为200
        reviews.find_element_by_xpath("./button[@aria-label='See More']").click()
        time.sleep(1)
        single_reviews = reviews.find_elements_by_xpath(".//div[@class='expand-page' and @style='width: 100%; opacity: 1;']//div[@class='single-review']")

        for single_review in single_reviews:
            result = []
            if(single_review.find_element_by_xpath("./div[@class='review-header']//span[@class='author-name']").text == ''):
                print "what?"

            author = single_review.find_element_by_xpath("./div[@class='review-header']//span[@class='author-name']").text
            review_date = extract_review_date(single_review.find_element_by_xpath("./div[@class='review-header']//span[@class='review-date']").text)
            review_score = extract_review_score(single_review.find_element_by_xpath("./div[@class='review-header']//div[@class='current-rating']").get_attribute("style"))
            review_title = single_review.find_element_by_xpath("./div[@class='review-body with-review-wrapper']/span[@class='review-title']").text
            review_body = single_review.find_element_by_xpath("./div[@class='review-body with-review-wrapper']").text
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            result.extend([apk_id,review_id,url,author,review_score,review_title,review_body,review_date,timestamp])
            review_id += 1
            results.append(result)

            print '评论作者：'+ author
            print '评论日期：'+ review_date
            print '评分：'+ str(review_score)
            print '评论题目：' + review_title
            print '评论内容：'+ review_body
    return results

'''
抽取评论的评分。
举例：
score_raw = 'width: 100%;' ## 数据形式
目的在于抽取出：100
'''
def extract_review_score(review_score):
    return 5 * (float(review_score[7:-2])/100)##评分计算公式 OR 也可以采用百分制。

'''
【日期对应表】January一月； February二月； March三月； April 四月； May 五月；June 六月；July七月；August 八月；September 九月；October 十月；November 十一月；December十二月。
'''
dates = {'January':'1',
         'February':'2',
         'March':'3',
         'April':'4',
         'May':'5',
         'June':'6',
         'July':'7',
         'August':'8',
         'September':'9',
         'October':'10',
         'November':'11',
         'December':'12'}
'''
测试数据形式： "January 1, 2016"
'''
def extract_review_date(date_raw):
    date_array = date_raw.split(' ')
    year = date_array[2]
    month = dates[date_array[0]]
    day = date_array[1][:-1]
    result = "{0}-{1}-{2}".format(year,month,day)
    return result

def save_db(reviews):
    print "准备插入数据"
    import MySQLdb

    conn = MySQLdb.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        passwd='123456',
        db='app_sense',
    )    ## TODO 复用连接。

    sql = "INSERT IGNORE INTO review VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    try:
        conn.set_character_set('utf8')

        cursor = conn.cursor()
        cursor.execute('SET NAMES utf8;')
        cursor.execute('SET CHARACTER SET utf8;')
        cursor.execute('SET character_set_connection=utf8;')

        cursor.executemany(sql, reviews)
        conn.commit()
    except Exception,e :
        print "出现问题"
        print 'traceback.print_exc():'; traceback.print_exc()
    finally:
        cursor.close()
        conn.close()
        print "插入数据结束"


if __name__=='__main__':
    print "start"
    url = "https://play.google.com/store/apps/details?id=com.google.android.youtube&hl=en"
    reviews = craw_one_app_reviews(url)
    save_db(reviews)
    print "end"




