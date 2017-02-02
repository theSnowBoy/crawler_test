import urllib2
response = urllib2.urlopen("http://apk.hiapk.com/web/api.do?qt=1701&id=4445482&pi=46&ps=10")
print response.read()