from bs4 import BeautifulSoup
from urllib2 import urlopen,Request
import time, urllib2

ua = {#'User-Agent':'Mozilla/5.0 (compatible; Googlebot/2.1; +Googlebot - Webmaster Tools Help)',
      'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36',
      'Connection':'Keep-Alive',
      'Accept-Language':'zh-CN,zh;q=0.8',
      'Accept-Encoding':'gzip,deflate,sdch',
      'Accept':'*/*',
      'Accept-Charset':'GBK,utf-8;q=0.7,*;q=0.3',
      'Cache-Control':'max-age=0'
      }

def get_url_content(url):
    i_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",\
                 "Referer": "http://www.yizhibo.com/l/CRgbmReqm0Cizr46.html"}
    req = Request(url, headers=i_headers)
    return urlopen(req).read()

def get_content_by_proxy(url, proxy):
    opener = urllib2.build_opener(urllib2.ProxyHandler({'http':proxy}), urllib2.HTTPHandler(debuglevel=1))
    urllib2.install_opener(opener)

    i_headers = {"User-Agent": ua , \
                                        "Referer": 'http://www.baidu.com'}

    req = urllib2.Request(url, headers=i_headers)
    content = urllib2.urlopen(req).read()
    return content

with open('links.txt') as fp:
    for line in fp:
        html = get_content_by_proxy(line,'http://172.32.1.75:3128')
        soup = BeautifulSoup(html, features='lxml')
        vlink = soup.find('video')
        print(vlink['src'])
        time.sleep(30)
