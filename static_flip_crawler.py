# -*- coding:utf-8 -*-
import re
import requests
import os
from tqdm import tqdm
from PIL import Image

def Find(url):
    List = []
    print('正在检测图片总数，请稍等.....')
    margin=60
    t = 0
    i = 1
    s = 0
    while True:
        Url = url + str(t)
        try:
            Result = requests.get(Url, timeout=7)
        except BaseException:
            t = t + 60
            continue
        else:
            result = Result.text
            pic_url = re.findall('"objURL":"(.*?)",', result, re.S)  # 先利用正则表达式找到图片url
            s += len(pic_url)
            if len(pic_url) == 0:
                if s>=totalNum :
                    print('图片总数为'+str(s)+'张，大于需求数量，通过合理性检验')
                    return True,s
                else:
                    print('图片数量不足，仅有'+str(s)+'张，未通过合理性检验')
                    return False,s
            elif s>=(totalNum+margin):
                print('图片总数超过'+str(totalNum)+'张，远大于需求数量,通过合理性检验')
                return True,s
            else:
                List.append(pic_url)
                t = t + 60

def dowmloadPic(i, pic_url, keyword, num):
    print('现在开始下载第'+str(int(i/60)+1)+'批图片...')
    pbar_ = tqdm(pic_url)
    for each in pbar_:
        try:
            pic = requests.get(each, timeout=10)
        except:
            continue
        width = len(str(totalNum))
        path = './'+keyword+'/' + keyword + '_' + str(num).rjust(width,'0') + '.jpg'
        fp = open(path, 'wb')
        fp.write(pic.content)
        fp.close()
        if num==totalNum:
            print('下载完成！')
            print('-------------------------------------')
            print('一共保存了'+str(num)+'张图片到了'+word+'文件夹')
            exit()
        num += 1
    return num


if __name__ == '__main__':
    word = input("请输入图片搜索关键字: ")
    totalNum = int(input("请输入图片需求数量: "))
    url = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=' + word + '&ct=201326592&v=flip&rn=60&pn='
    passed,num = Find(url)
    if not passed:
        while True:
            totalNum = int(input("重新输入图片需求数量: "))
            if totalNum <= num:
                break 
            else:
                continue
    if not os.path.exists("./" + word):
        os.mkdir("./" + word)
    pnMax = (int(totalNum/60)+1)*60
    pic_url = []
    num = 1
    for i in range(1,pnMax,60):
        pn = i
        result = requests.get(url+str(pn))
        pic_url = re.findall('"objURL":"(.*?)",', result.text, re.S)
        num = dowmloadPic(i, pic_url, word, num)
    
