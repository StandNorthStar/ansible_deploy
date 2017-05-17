# coding=utf-8

'''
thread
'''

import threading
import time

#def listinfo(k):
#    
#    while True:
#       time.sleep(k)
#    #sum = 0 
#    #for i in range(k):
#    #   sum += i
#    #return sum
#
#for i in xrange(6):
#    k = []
#    k.append(i+10)
#    a = threading.Thread(target=listinfo,args=(k))
#    a.start()
#    #a.join()


##  
import urllib2
import re

def openwww(urllist):
    
    #for i in urllist:
       
       a = urllib2.urlopen(urllist)
       k = a.read()
       m = re.search("<title>.*</title>",k)
       title = m.group()
       print title
       #return title

def getzt(urllist):
     
     for i in urllist:
       a = urllib2.urlopen(i)
       b = a.getcode
       print b

if __name__ == "__main__":
    url = ('http://www.baidu.com','http://python.jobbole.com/81546/')
    #k = openwww(url)
    for i in url:
       th = threading.Thread(target=openwww, args=(i,))    
            # 因为 args 后面的参数是元祖类型。此时传送过来的 i 是一个字符串格式，所以在后面添加个逗号。
       th.start()
       th.join()
    
      
