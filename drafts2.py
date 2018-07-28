'''
#coding =utf-8
import urllib.request
import re
def getHtml(url):
    page = urllib.request.urlopen(url)  ##打开页面
    html = page.read() ##获取目标页面的源码
    return html
if __name__=="__main__":
    html = getHtml("http://www.quanjing.com/category/118291.html")

    reg = "http://.+?\\.jpg"
    img = re.compile(reg)
    html = html.decode('utf-8')

    imglist = re.findall(img, html)
    print(imglist[0])
    urllib.request.urlretrieve(imglist[0], 'D:/1.jpg')

'''

#coding =utf-8
import urllib.request
import re
import requests  #这里使用requests，小脚本用它最合适！
from lxml import html    #这里我们用lxml，也就是xpath的方法


cookie = {}
raw_cookies = '__tins_2864513=%7B%22sid%22%3A%201532501993020%2C%20%22vd%22%3A%202%2C%20%22exp ires%22%3A%201532504076166%7D;__51cke__=;__51laig__=2'
#引号里面是你的cookie，用之前讲的抓包工具来获得
for line in raw_cookies.split(';'):
    key,value = line.split("=", 1)
    cookie[key] = value #一些格式化操作，用来装载cookies

#用requests，装载cookies，请求网站
    html = requests.get('http://frps.eflora.cn/',cookies=cookie)
print(html)
#    page = urllib.request.urlopen(url)  ##打开页面
#    html = page.read() ##获取目标页面的源码

if __name__=="__main__":
#    html = getHtml("http://www.quanjing.com/category/118291.html")
#    html = getHtml("http://www.plantphoto.cn/wallpaper")
    reg = "http://.+?\\.jpg"
    img = re.compile(reg)
    html = html.decode('utf-8')
    print(html)

    imglist = re.findall(img, html)
    print(imglist[0])
    urllib.request.urlretrieve(imglist[0], 'C:/Users/think/Desktop/1.jpg')




from bs4 import BeautifulSoup
import requests

url = 'https://http://www.plantphoto.cn/sp/34240'
wd_data = requests.get(url)
soup = BeautifulSoup(wd_data.text,"lxml")
titles = soup.select("div.listing_title > a[target='_blank']")
imgs = soup.select('img[width="180"]')  #图片做了反爬处理，通过js加载出来
cates = soup.select('div.p13n_reasoning_v2')

for title,img in zip(titles,imgs):
    data = {
        'title':title.get_text(),   #获取文本内容
        'img':img.get('src'),     #获取src的内容
    }
    print(data)
