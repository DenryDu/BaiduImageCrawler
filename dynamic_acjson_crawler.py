#*
#* Author: DenryDu 
#* Time: 2020/06/23 16:14:04
#* Description: quickly and stably crawl images from baidu images, using /acjson path
#*
import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urlencode
import json
import os
from tqdm import tqdm

class exitLoop(Exception):
    pass
#date为百度图片的链接的一些基本信息，通过f12可以查看，我们刷新图片，就可以看到出现新的网页代码，可以提取出这些信息，
class Crawler(object):
    """ crawler for baidu image """
    def __init__(self):
        """
        init function, set date for object

        """
        self.date={
            "tn": "resultjson_com", 
            "ipn":"rj", "ct": 201326592, 
            "fp": "result", 
            "queryWord": "name", 
            "cl": 2, 
            "lm": -1, 
            "ie": "utf-8", 
            "oe": "utf-8", 
            "word":"name", 
            'rn': 30,
            "pn": 0 
        }

    def set(self, name, num):
        """
        set name and num for crawler
        
        Inputs:
            - name: specify the image name
            - num: specify the image num
        """
        self.name  = name 
        self.num = num
        self.date["queryWord"]=name
        self.date["word"]=name

    def Check(self):
        """
        Check whether the num of image is enough
            - passed: a boolean value to show whether the image is enough
            - t_num: if not enough, the value of t_num will show you how many image there is 
        """
        print('正在检测图片总数，请稍等.....')
        margin=30
        t = 0
        i = 1
        s = 0
        while True:
            self.date["pn"]=t
            # urlencode可以把date数据转化为url
            url="https://image.baidu.com/search/acjson?"+urlencode(self.date)         
            # get数据
            try:
                html=requests.get(url)
            except BaseException:
                t = t + 30
                continue
            else:
                #json中data包含百度图片的30个链接信息
                try:
                    data=html.json()["data"]                         
                except:
                    t+=30
                    continue
                # 一次性获取30个url，并添加到urllist中去
                picture_urllist=[]
                for i in range(len(data)):
                    try:
                        #data也是一个字典，很多键里面可以看到有链接，就是一张图片的链接，进行提取
                        picture_urllist.append(data[i]["middleURL"])    
                    except:
                        continue
                s+=len(picture_urllist)
                if len(data) == 0:
                    if s>=self.num :
                        print('图片总数为'+str(s)+'张，大于需求数量，通过合理性检验')
                        return True,s
                    else:
                        print('图片数量不足，仅有'+str(s)+'张，未通过合理性检验')
                        return False,s
                elif s>=(self.num+margin):
                    print('图片总数超过'+str(self.num)+'张，远大于需求数量,通过合理性检验')
                    return True,s
                else:
                    t = t + 30

    def Download(self):
        """
        download image with self.num and self.name
        
        """
        n=0
        width = len(str(self.num))
        # create folder to save imgs
        if not os.path.exists("./" + self.name):
            os.mkdir("./" + self.name)
        pnMax = (int(self.num/30)+1)*30
        try:
            with tqdm(range(self.num),position=1) as pbar:
                for i in range(0,pnMax*2,30):
                    self.date["pn"]=i
                    # urlencode可以把date数据转化为url
                    url="https://image.baidu.com/search/acjson?"+urlencode(self.date)         
                    # get数据
                    html=requests.get(url)
                    #json中data包含百度图片的30个链接信息
                    try:
                        data=html.json()["data"]                         
                    except:
                        continue
                    # 一次性获取30个url，并添加到urllist中去
                    picture_urllist=[]
                    for i in range(len(data)):
                        try:
                            #data也是一个字典，很多键里面可以看到有链接，就是一张图片的链接，进行提取
                            picture_urllist.append(data[i]["middleURL"])    
                        except:
                            continue
                    # 对list中的图片进行下载和保存
                    for i in tqdm(range(len(picture_urllist)),position=0):
                        path="./"+self.name+"/"+self.name+str(n).rjust(width,'0')+".jpg"
                        picture=requests.get(picture_urllist[i])
                        with open(path,"wb") as file:
                            file.write(picture.content)
                            n+=1
                            pbar.update(1)
                            #print("成功爬去第{}张图片".format(n))
                        if n>=self.num:
                            raise exitLoop()
        except exitLoop:
            print(" 爬取成功")
            exit()

def main():
    name = input("请输入图片搜索关键字: ")
    totalNum = int(input("请输入图片需求数量: "))
    crawler = Crawler()
    crawler.set(name, totalNum)
    passed,num = crawler.Check()
    if not passed:
        while True:
            totalNum = int(input("重新输入图片需求数量: "))
            if totalNum <= num:
                break 
            else:
                continue
    crawler.Download()

main()

