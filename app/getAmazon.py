__author__ = 'oliverhuang'
import requests
from bs4 import BeautifulSoup

website = "http://www.amazon.cn/gp/feature.html/ref=sa_menu_kindle_l3_f126758?ie=UTF8&docId=126758"
# w1 = "http://www.google.com"
res = requests.get(website)
# print res.status_code
soup = BeautifulSoup(res.content)
# print res.content
res = soup.find(class_="content")
# print res
# for i in res.select("a")[-4:]:
# #get name
# print i.text,i["href"]
# for j in res.find_all(class_="price"):
# #kindle price
#     print j.text
# for k in res.select("img"):
#     print k.src
