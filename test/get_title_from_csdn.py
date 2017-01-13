#coding:utf-8

#测试基本的爬虫功能。爬取CSDN某个用户，某页的题目。
from sgmllib import SGMLParser
class ListName(SGMLParser):
    flag = False
    getdata = False
    verbatim = 0
    article_list = []

    def start_span(self, attrs):
        if self.flag == True:
            self.verbatim += 1
        for k,v in attrs:
            if k == "class" and v == "link_title":
                self.flag = True

    def end_span(self):
        if self.verbatim == 0:
            self.flag = False
        if self.flag == True:  # 退出子层span了，层数减 1
            self.verbatim -= 1

    def start_a(self,attrs):
        if self.flag == False:
            return
        self.getdata = True

    def end_a(self):
        if self.getdata:
            self.getdata = False

    def handle_data(self, text):
        if self.getdata:
            self.article_list.append(text)

def get_data_from_net(my_url):
    import urllib2
    user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0"
    headers = {"User-Agent" : user_agent}
    request = urllib2.Request(my_url,None,headers)
    response = urllib2.urlopen(request)
    # print response.read()
    return response

def filtrate_data(data):
    import string
    listName = ListName()
    listName.feed(data)
    for items in listName.article_list:
        print string.strip(items) # 去掉前后空格

if __name__=='__main__':
    my_url = "http://blog.csdn.net/thesnowboy_2"
    my_url2 = "http://blog.csdn.net/TheSnowBoy_2/article/list/"
    for i in range(1,11):
        response = get_data_from_net(my_url2 + str(i))
        filtrate_data(response.read())