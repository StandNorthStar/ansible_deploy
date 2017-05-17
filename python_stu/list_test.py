#! coding=utf-8

'''
实现对列表的操作
 
'''
class Listinfo(object):
   
     def __init__(self,listinfo):
         
         self.lst = listinfo
 
     # 往列表里面添加一个值
     def add_key(self,keyname):

         self.keyname = keyname
         if not isinstance(keyname,str) and isinstance(keyname,int):
            print "The keyname value is error !"

         addlst = self.lst.append(keyname)
         return addlst

     # 根据 num 获取列表里的值
     def get_key(self,num):
         
         self.num = num
         
         if not isinstance(num,int):
            print "th num value is not int .ERROR"
           
         sellst = self.lst[num]
         return sellst

     # 合并列表
     def update_list(self,lst_1):
         
         if not isinstance(lst_1,list):
            print "Is not List .Are you sure ?"
          
         newlst = self.lst + lst_1
         return newlst

if __name__ == "__main__":
   listinfo = Listinfo([1,54,87,34,54,223])

   a = listinfo.add_key(1.2)
   print a

   b = listinfo.get_key(2)
   print b 

   c = listinfo.update_list(['aa','bb','cc'])
   print c
