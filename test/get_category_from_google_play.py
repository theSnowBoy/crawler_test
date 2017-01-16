#coding:utf-8
# 爬取google play 上相关的信息，但是发现是js,所以需要对相应的js做出反应。
from sgmllib import SGMLParser
class ListCategory(SGMLParser):
    flag = False
    getdata = False
    verbatim = 0
    article_list = []

    def start_li(self, attrs):
        if self.flag == True:
            self.verbatim += 1
        for k,v in attrs:
            if k == "class" and v == "child-submenu-link-wrapper":
                self.flag = True

    def end_li(self):
        if self.verbatim == 0:
            self.flag = False
        if self.flag == True:
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

def filtrate_data(data):
    import string
    print  data
    listName = ListCategory()
    listName.feed(data)
    for items in listName.article_list:
        print string.strip(items) # 去掉前后空格

if __name__=='__main__':
    import get_title_from_csdn
    google_play_url = "https://play.google.com/store"
    response = get_title_from_csdn.get_data_from_net(google_play_url)
    filtrate_data(response.read())