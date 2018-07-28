#coding=utf-8  
import urllib.request
from bs4 import BeautifulSoup  
import os  
import re  
   
url="http://www.plantphoto.cn/sp/28212"#指定的URL    
  
def download(_url,name):#下载函数  
    if(_url==None):#地址若为None则跳过  
        pass  
    result=urllib.request.urlopen(_url)#打开链接  
    #print result.getcode()  
    if(result.getcode()!=200):#如果链接不正常，则跳过这个链接  
        pass  
    else:  
        data=result.read()#否则开始下载到本地  
        with open(name, "wb") as code:  
            code.write(data)  
            code.close()
            
  
res=urllib.request.urlopen(url)#打开目标地址  
respond=res.read()#获取网页地址源代码  
  
count=0#计数 
soup=BeautifulSoup(respond,"lxml")#实例化一个BeautifulSoup对象  
lst=[]#创建list对象  
  
for link in soup.find_all("img"):#获取标签为img的内容  
    #address=link.get('data-original')#获取标签属性为data-original的内容，即图片地址  
    address=link.get('src')
    lst.append(address)#添加到list中  
  
s=set(lst)#去重  
for address in s:  
    if(address!=None):  
        pathName="C:/Users/think/Desktop/计生项目实践/pics/pic"+str(count+1)+".jpg"#设置路径和文件名  
        download(address,pathName)#下载  
        count=count+1#计数+1  
        print ("正在下载第：",count) 
