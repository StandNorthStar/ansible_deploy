#!/usr/bin/python
# coding = utf-8

def genf(num):
   
    for n in range(num): 
        yield n
        n = n + 1
        print n 

if __name__ == "__main__":

   a = 5
   #for i in range(a):
   b = genf(5)
   b.next()
