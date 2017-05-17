#coding=utf-8


'''
有问题啊，日志写入文件错误。
 
'''

import logging
import urllib2

loggin.basicConfig(
               level = logging.debug,
               datefmt = '/5a,%Y %b %d %H:%M:%S',
               filename = '/tmp/test.log',
               filemode = 'a'
    	)

def func(filepath):
    
    '''
    打开文件   --->   返回文件内容
    '''

    #
    # try:
    #   wf = open(filepath,'r')
    #   data = wf.read()
    #   return data

    #except: IOError
    #logging.info(wf)
    #logging.info(wf)


def func_test(urllist):

	for url in urllist:

	   try:
	   	 a = urllib2.urlopen(url)
	   	 data = a.read()
	   	 print type(data)
         #logging.debug(data)

       except: IOError ,a 
       	 #logging.error('The erro url: %s' % url)
       	 print a

       #finally
 

     
if __name__ == '__main__':
    
    #func('/root/mjswitch.yml') 
    #func('/root')
    test = ['www.bhha.com','http://www.baidu.com','class.co','http://www.163.com']
    func_test(test)


    

