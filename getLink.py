from bs4 import BeautifulSoup
from urllib2 import urlopen,Request
import time , urllib2

# if has Chinese, apply decode()
#html = urlopen("http://www.yizhibo.com/member/personel/user_works?memberid=204136686").read().decode('utf-8')
#html = open("index.html")

req = Request("http://www.yizhibo.com/member/personel/user_works?memberid=204136686")
response = urlopen(req)
html = response.read()

soup = BeautifulSoup(html, features='lxml')

links = soup.find_all('a',{"class":"index_img_hover pa dn"})

for a in links:
    print('http://www.yizhibo.com' + a['href'])
