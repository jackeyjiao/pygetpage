from bs4 import BeautifulSoup

fp = open("http://www.yizhibo.com/member/personel/user_works?memberid=204136686")
soup1 = BeautifulSoup(fp)
soup2 = BeautifulSoup("<html>data</html>")
soup = BeautifulSoup("<div></div>")
tag = soup.div
tag.name == u'div'
tag['class'] == u'index_img fl pr'
print tag.find_all("a")