# coding=UTF-8
# '''
# Created on 2017年8月24日
# 
# @author: Administrator
# '''
import urllib2
import os
import re

if  __name__ == '__main__':
    url='http://www.ahnu.edu.cn/'
    user_agent='Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
    headers = {'User-Agent':user_agent}
    request=urllib2.Request(url=url,headers=headers)
    response= urllib2.urlopen(request)
    content= response.read()
        
        #2.根据抓取的网页源代码，抓取所需内容
#     pattern =re.compile('.*?')
#     items= re.findall(pattern, content)
    path = 'anshida'
    if not os.path.exists(path):
        os.makedirs(path)
    file_path=path+'/'+'anshida'+'.txt'
    f=open(file_path,'wb')
    f.write(content)
    f.close()