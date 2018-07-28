#-*-coding:utf-8-*- 
import requests  #这里使用requests，小脚本用它最合适！
from lxml import html    #这里我们用lxml，也就是xpath的方法

#豆瓣模拟登录，最简单的是cookie，会这个方法，80%的登录网站可以搞定
cookie = {} 

raw_cookies = '__tins_2864513=%7B%22sid%22%3A%201532501993020%2C%20%22vd%22%3A%202%2C%20%22exp ires%22%3A%201532504076166%7D;__51cke__=;__51laig__=2'
#引号里面是你的cookie，用之前讲的抓包工具来获得

for line in raw_cookies.split(';'):
    key,value = line.split("=", 1)
    cookie[key] = value #一些格式化操作，用来装载cookies

#重点来了！用requests，装载cookies，请求网站
page = requests.get('http://frps.eflora.cn/',cookies=cookie)

#对获取到的page格式化操作，方便后面用XPath来解析
tree = html.fromstring(page.text)

#XPath解析，获得你要的文字段落！
intro_raw = tree.xpath('//span[@id="intro_display"]/text()')

#简单的转码工作，这步根据需要可以省略
for i in intro_raw:
    intro = i.encode('utf-8')

print(intro_raw) #妹子的签名就显示在屏幕上啦

#接下来就是装载邮件模块，因为与本问题关联不大就不赘述啦~
