#coding=utf-8
# 获取安卓市场上的评论信息。
from selenium import webdriver
import time
class CommentFromHiapk():
    def __init__(self):
        # 设置代理服务器。
        profile = webdriver.FirefoxProfile()
        # profile.set_preference('network.proxy.type', 1)  # 默认值0，就是直接连接；1就是手工配置代理。
        # profile.set_preference('network.proxy.http', "116.242.227.201")
        # profile.set_preference('network.proxy.http_port', "3128")
        # profile.set_preference('network.proxy.ssl',ip)
        # profile.set_preference('network.proxy.ssl_port', port)
        profile.update_preferences()
        self.driver =  webdriver.Firefox(profile)
        self.url= 'http://apk.hiapk.com/appinfo/com.tencent.mm/900'
        self.driver.get(self.url)
        self.count = 0
        self.num_comment = 0;

    def  get_start_info(self):
        start_lines = self.driver.find_elements_by_xpath("//div[@class='left star_detail_box']")
        for start_line in start_lines:
            data = start_line.find_element_by_xpath("./div[@class='star_per_line']/div[2]")
            print data.text

    def get_num_comment(self):
        time.sleep(2)
        str_count = self.driver.find_element_by_xpath("//div[@class='font16']/span[1]").text
        return  int(str_count)

    def get_some_comment_info(self):
         comment_items = self.driver.find_elements_by_xpath("//div[@class='comment_list']/div[@class='comment_item']")
         print "get comment items size :" + str(len(comment_items))
         self.count = self.count + len(comment_items)
         for comment_item in comment_items:
             comment_content = comment_item.find_element_by_xpath("./div[1]/div[@class='comment_right']/div[@class='comment_content']")
             print comment_content.text

    def get_all_comment(self):
        self.num_comment = self.get_num_comment()
        while(self.count < self.num_comment):
            if(self.count% 100 == 0):
                time.sleep(5)
            time.sleep(3)
            self.get_some_comment_info()
            next_page = self.driver.find_element_by_xpath("//div[@id='cmtPage']/div[1]/span[@class='page_item page_next page_able']")
            next_page.click()


if __name__=='__main__':
    print "start"
    comment = CommentFromHiapk()
    comment.get_all_comment()
    print "end"
