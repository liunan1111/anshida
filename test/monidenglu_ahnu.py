#!/usr/bin/python 
# coding=UTF-8
#'''
#Created on 2017��8��24��

#@author: Administrator
# '''
import urllib2
import urllib
import cookielib 

if __name__ == '__main__':
        posturl='http://jwgl.ahnu.edu.cn/login/check.shtml'
        hosturl='http://jwgl.ahnu.edu.cn/login.shtml'   
        user_agent='Mozilla/5.0'
        headers = {'User-Agent':user_agent,
                   'Referer':hosturl}
        print '请输入学号：'
        user=input()
        print '请输入密码：'
        pw=input()
        values={'user':user,
                'pass':pw,
                'usertype':'stu'
            }
        data=urllib.urlencode(values)
        request=urllib2.Request(url=posturl,data=data,headers=headers)
        response= urllib2.urlopen(request)  
        print '------------------------'
        print response.read()
        print '登陆成功，开始自动查询成绩！'
        print '------------------------'