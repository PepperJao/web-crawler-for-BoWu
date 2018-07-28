#coding=utf-8
import requests
import os
from bs4 import BeautifulSoup
import time

class bot():
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    index_url='http://www.plantphoto.cn'
    root='C:/users/think/desktop/pics1'

    def mkdir(self,path):
        path = path.strip()
        isExists = os.path.exists(os.path.join(self.root, path))
        if not isExists:
            print(u'建了一个名字叫做'+ path+ u'的文件夹！')
            os.makedirs(os.path.join(self.root, path))
            return True
        else:
            print(u'名字叫做'+ path+ u'的文件夹已经存在了！')
            return False
    
    def request(self,url):
        headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        content=requests.get(url,headers=headers)
        return content
    
    #保存图片
    def save(self,img_url,number):
        name=str(number)+'_'+img_url[-14:]
        #如果图片存在，跳过
        if os.path.exists(name):
            print('跳过图片：'+name)
            return
        time.sleep(1)
        img=self.request(img_url)
        f=open(name,'ab')
        f.write(img.content)
        f.close()
        print('保存图片：'+name)
    
    def start(self,url):
        start_time=time.time()
        page=1
        while True:
            #运行1小时后结束程序
            current_time=time.time()
            if current_time-start_time > 3600:
                exit()

            soup_html=self.request(url+'/?attr=&sort=&page='+str(page))
            if soup_html.status_code != requests.codes.ok:
                exit()
            soup_index=BeautifulSoup(soup_html.text,'lxml')
            article_list=soup_index.find('div',id='article-list').find_all('div',class_='article')   #获取图片信息
            for article in article_list:
                a=article.find('a')
                href=self.index_url+a['href']
                p=a.find('p')
                title=p.get_text()
                
                page_html=self.request(href)
                soup_page=BeautifulSoup(page_html.text,'lxml')
                article_info=soup_page.find('div',id='article-Info').find_all('img')
                self.mkdir(title)
                #切换目录
                os.chdir(os.path.join(self.root, title))
                pic_count=1
                #本页图片列表
                for img in article_info:
                    img_src=self.index_url+img['src']
                    self.save(img_src,pic_count)
                    pic_count+=1
            #翻页
            page+=1

b=bot()
b.start('http://www.plantphoto.cn')
