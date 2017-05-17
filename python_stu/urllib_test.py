#!coding=utf-8

'''
哈哈
'''

import urllib2

# 获取请求网页状态码
def get_httpcode(url):
    
    codeurl = url
    openurl = urllib2.urlopen(codeurl)
    code = openurl.getcode()
    if not isinstance(code,int):
       print "This value is error"
    return code 

# 获取网页的内容
def get_htmlcontent(url):
    
    get_url = url
    openurl = urllib2.urlopen(get_url)
    data = openurl.read()
    if not isinstance(data,str):
       print "data value is not str"

    return data

if __name__ == "__main__":
   
    test_url = "http://www.baidu.com"
    a = get_httpcode(test_url)
    print a
    
    w = open('/data/tt','w')
    b = get_htmlcontent(test_url)

    w.write(b)
    w.close()





