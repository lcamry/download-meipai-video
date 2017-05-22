#!/usr/bin
#-*- coding: utf-8 -*-
#DATA:2017年5月20日
#AUTHOR:lcamry
#blog：http://www.cnblogs.com/lcamry
#link:
#qq:646878467
#usag:python download-meipai-video.py http://www.meipai.com/media/730173228
import sys,os
import urllib2
import base64

try:
    from lxml import html
except ImportError:
    raise SystemExit("lxml module is wrong,please execute:pip install lxml")
class submain():
    '''
    域名收集
    '''
    def __init__(self,submain):
        self.submain = submain
        self.sublist = []
    def get_sourceurl(self):
        for i in range(0,20):
            scan_data = urllib2.urlopen(self.submain).read()
            html_data = html.fromstring(scan_data)
            submains = html_data.xpath("//span//@data-video")
            self.sublist.extend(submains)
 #       print self.sublist
    def scan_domain(self):
        self.get_sourceurl()
        return list(set(self.sublist))
if __name__ == '__main__':
    domain = sys.argv[1]
    submain = submain(domain).scan_domain()
    for line in  submain:
        if len(line) % 4 ==0:
            try:
                print base64.decodestring(line)
            except:
                continue