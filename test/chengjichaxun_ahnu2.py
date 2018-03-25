#!/usr/bin/python 
# coding=UTF-8
#'''

#@author: Administrator
# '''
import urllib2
import urllib
import cookielib 
import re
from bs4 import BeautifulSoup
import time

if __name__ == '__main__':
        posturl='http://jwgl.ahnu.edu.cn/login/check.shtml'
        hosturl='http://jwgl.ahnu.edu.cn/'   
        cj = cookielib.LWPCookieJar()   
        cookie_support = urllib2.HTTPCookieProcessor(cj)   
        opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)   
        urllib2.install_opener(opener)
        user_agent='Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
        headers = {'User-Agent':user_agent
                   }
#         print '请输入学号：'
        putstr=u'请输入学号：'
        print putstr
        user=raw_input()
#         print '请输入密码：'
        putstr2=u'请输入密码：'
        print putstr2
        pw=raw_input()
        values={'user':user,
                'pass':pw,
                'usertype':'stu'
            }
        data=urllib.urlencode(values)
        request=urllib2.Request(url=posturl,data=data,headers=headers)
#         response= urllib2.urlopen(request)  
        response=opener.open(request)
#         print '------------------------'
#         print type(response.read())
        dict=response.read()
#         print unicode(str,'utf-8')
        strip=dict[12:19]
        if strip=='success':
            login=u'登陆状态：登陆成功'
            print login
        else:
            login2=u'登陆状态：登陆失败'
            print login2
            time.sleep(20)
            quit()
#         print '------------------------'
        print u'请输入如2015-2016:'
        year=raw_input()
        print u'请输入0-2中的一个数字，0代表全年，其他代表第1或第2学期:'
        term=raw_input()
        url='http://jwgl.ahnu.edu.cn/query/cjquery/index?action=ok&xkxn='+year+'&xkxq='+term
        user_agent='Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
        headers = {'User-Agent':user_agent,
                   'Referer':hosturl}
        request=urllib2.Request(url=url,headers=headers)
        response= urllib2.urlopen(request)
        content=response.read()
        soup=BeautifulSoup(content,"html.parser")
#         print soup.prettify()
#         child1= soup.table.contents[3]
#         print child1
#         child2= soup.table.contents[3].cotntets.string
#         print child2
#         print '------------------------'
#         print type(soup.table.tr.td.string)
#         print soup.table.tr.td.string
#         print '------------------------'
#         print len(soup.table.contents)
        l=len(soup.table.contents)
        try:
            for i in range(1,int(l/2)):
                arr=[]
                for child in soup.table.contents[2*i+1]:
        #             print child
                    arr.append(child.string)                   
                for item in arr:
                    try:
                        arr.remove('\n')
                    except:
                        pass
                cnt=0
                for item in arr:
                    if cnt==1or cnt==2or cnt==4or cnt==6or cnt==7:
                        print '\t'+item,
#                         print type(item)#<class 'bs4.element.NavigableString'>
                    cnt=cnt+1
                print '\n'
        except:
            pass
        time.sleep(100)