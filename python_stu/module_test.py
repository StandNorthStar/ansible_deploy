#!coding=utf-8

import time
import datetime

print time.time()

# 
print datetime.datetime.now().date()

print datetime.datetime.now()

# 获取前一个月的时间
dangqian = datetime.datetime.now()
premonth = datetime.date(day=dangqian.day,month=dangqian.month,year=dangqian.year)
end = premonth - datetime.timedelta(days=1)
print "zhe yue %s ; shangyue %s" % (premonth,end)

# ------- os ----------
import os
os.system("ping www.baidu.com -c 1")

# 这个没完成 ～～～～ 
def kouzhang(dirpath):
       
    path = dirpath
    
    a = os.listdir(path)
    for i in a:
       if not os.path.isdir(path+ '/' +i) and not i[0] == '.':
          m = i.split('.')[1]
          #print m
          return m

import pickle
import random


# 把对象保存到文件里，序列化对象
@property
def xulie(dirname,info):
    
    '''
    要求：把对象序列化到随机的文件中。
    思路：先找到这个随机的文件。
    判断目录下是否文件，如果是文件就把这个文件的路径写入到一个列表中。最后从这个列表里随机找一个文件序列化。

    '''
    path = dirname
    xinxi = info
    
    files = os.listdir(path)
    xlfile = []
    
    for i in files:
      wj = path+'/'+i
      if os.path.isfile(wj):
         xlfile.append(wj)

    k = random.choice(xlfile)
    tt = open(k,'w')
    
    # dump() 必须在之前打开这个文件
    pickle.dump(xinxi,tt)    #  pickle.dumps(object,file)
    tt.close()
    print k
         
if __name__ == "__main__":

   kouzhang('/root/')
   #print  type(kouzhang('/root'))
   
   test = "hahahaha,heiheiheihei" 
   xulie('/root/test',test)  

