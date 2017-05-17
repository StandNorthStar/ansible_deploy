#!/usr/bin/python
# coding=utf-8

def fabo(num):
    
    a,b = 0,1
    #i =0
    li = []
    for i in range(num):
        a , b = b , a + b
    
        li.append(b)
    print li

if __name__ == '__main__':
   
   a = fabo(100)
