#!/bin/python
# -*- coding: utf-8 -*-

from HTMLParser import HTMLParser
import urllib
import urllib2
import cookielib 
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


USERNAME='HY12030001'
PASSWORD='123456'




# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.isForm = False
        self.curSectionName = None

        self.inputAttr = {}
        self.selection = {}   # {key, [selectedIdex, option, option...]}


    def handle_starttag(self, tag, attrs):
        tag = tag.lower()
        if tag == 'form':
            self.isForm = True
            # print "Encountered a start tag:", tag
            # print attrs
        elif tag == 'select' and self.isForm:
            attrs = dict(attrs)
            if 'name' in attrs:
                self.curSectionName = attrs['name']
                self.selection[self.curSectionName] = [0]
        elif tag == 'option':
            self._handle_option(attrs)

    def handle_endtag(self, tag):
        if self.isForm:
            tag = tag.lower()
            if tag == 'form':
                self.isForm = False
            elif self.curSectionName is not None and tag == 'select':
                self.curSectionName = None
                # print "Encountered an end tag :", tag

    def handle_startendtag(self, tag, attrs):
        if self.isForm:
            tag = tag.lower()
            if tag == 'input':
                self._handle_input(attrs)
            
            
            # print tag, attrs

    def handle_data(self, data):
        pass
        # if self.isForm:
            # print "Encountered some data  :", data



    def _handle_input(self, attrs):
        attrs = dict(attrs)
        if 'name' not in attrs:
            return
        name = attrs['name']

        t = attrs['type']
        if t == 'radio':
            if name not in self.selection:
                self.selection[name] = [0]
            self.selection[name].append(attrs['value'])
            if 'checked' in attrs:
                self.selection[name][0] = len(self.selection[name]) - 1
        elif t == 'checkbox':
            print 'now can not suppor checkbox'
        else:
            self.inputAttr[name] = attrs['value'] if 'value' in attrs else ''
            if t == 'hidden' and name == '__VIEWSTATE':
                print 'hidden', name, self.inputAttr[name]

    def _handle_option(self, attrs):
        attrs = dict(attrs)
        curSection = self.selection[self.curSectionName]
        curSection.append(attrs['value'])
        if 'selected' in attrs:
            curSection[0] = len(curSection) - 1

    def getPostMap(self):
        m = self.inputAttr.copy()
        for k, v in self.selection.iteritems():
            print k, v
            m[k] = v[v[0]]
        return m



cookie = cookielib.CookieJar()  
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))

# get seetion id
response = opener.open('http://www.sjtuce.net/xxpt/jrjxpjLogin.aspx')
html = response.read()
parser = MyHTMLParser()
parser.feed(html)

# login
data = parser.getPostMap()
data['user'] = USERNAME
data['Password'] = PASSWORD

response = opener.open('http://www.sjtuce.net/xxpt/jrjxpjLogin.aspx', urllib.urlencode(data))  
print response.geturl()
html = response.read()  
print 'cookie:'
for item in cookie: 
    print item.name, item.value
# print html

def s2i(s):
    n = 0
    try:
        n = int(s)
    except Exception, e:
        pass
    return n

def doPingjiaKechengRiqi(data):
    # 选择了一个上课日期
    # data post 数据
    url = 'http://www.sjtuce.net/xxpt/jrJxjhpjNew.aspx'

    response = opener.open(url, urllib.urlencode(data))
    print 'new url:', response.geturl()
    print 'cookie:'
    for item in cookie: 
        print item.name, item.value
    html = response.read()
    parser = MyHTMLParser()
    parser.feed(html)
    data = parser.getPostMap()

    # 添加具体评分
    if s2i(data['_ctl0:MainContent:dgNetzy:_ctl2:rbd']) == 5:
        return

    print '---------------------------'
    print data
    print '+++++++++++++++++++++++++++'

    # 去掉刷新本栏
    del data['_ctl0:MainContent:Button5']

    data['_ctl0:MainContent:dgNetzy:_ctl2:rbd'] = 5
    data['_ctl0:MainContent:dgNetzy:_ctl3:rbd'] = 5
    data['_ctl0:MainContent:dgNetzy:_ctl4:rbd'] = 5
    data['_ctl0:MainContent:dgNetzy:_ctl5:rbd'] = 5
    data['_ctl0:MainContent:dgNetzy:_ctl6:rbd'] = 5
    data['_ctl0:MainContent:dgNetzy:_ctl7:rbd'] = 5
    data['_ctl0:MainContent:dgNetzy:_ctl8:rbd'] = 5
    data['_ctl0:MainContent:dgNetzy:_ctl9:rbd'] = 5
    data['_ctl0:MainContent:dgNetzy:_ctl10:rbd'] = 5
    data['_ctl0:MainContent:dgNetzy:_ctl11:rbd'] = 5
    # 0:正面 1:中性 2:负面
    data['_ctl0:MainContent:rbdBzType'] = 0
    # 评价内容
    data['_ctl0:MainContent:cZySummary'] = '很好'

    response = opener.open(url, urllib.urlencode(data))
    print 'new url:', response.geturl()
    print 'cookie:'
    for item in cookie: 
        print item.name, item.value
    

def doPingjiaKecheng(data):
    # 选择了一个课程
    # data post 数据
    url = 'http://www.sjtuce.net/xxpt/jrJxjhpjNew.aspx'
    response = opener.open(url, urllib.urlencode(data))
    print 'new url:', response.geturl()
    print 'cookie:'
    for item in cookie: 
        print item.name, item.value
    html = response.read()
    parser = MyHTMLParser()
    parser.feed(html)

    data = parser.getPostMap()
    for v in parser.selection['_ctl0:MainContent:dplCs'][1:]:
        if s2i(v) > 0:
            copydata = data.copy()
            copydata['_ctl0:MainContent:dplCs'] = v
            doPingjiaKechengRiqi(copydata)


def doPingjia():
    # get do 教学评价
    url = 'http://www.sjtuce.net/xxpt/jrJxjhpjNew.aspx'
    response = opener.open(url)
    print 'new url:', response.geturl()
    print 'cookie:'
    for item in cookie: 
        print item.name, item.value
    html = response.read()
    parser = MyHTMLParser()
    parser.feed(html)

    data = parser.getPostMap()
    # 选择课程
    for v in parser.selection['_ctl0:MainContent:dplKc'][1:]:
        copydata = data.copy()
        copydata['_ctl0:MainContent:dplKc'] = v
        doPingjiaKecheng(copydata)

    


doPingjia()
