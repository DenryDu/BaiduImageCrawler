# BaiduImageCrawler
Baidu Image Crawler, which is based on python3 (百度图片爬虫，基于python3)      
For personal use, share with you guys (个人学习开发用，适用于计算机视觉项目准备数据集用)     
Including check of image num, have both dynamic and static way to crawl (包含图片数量验证，以及爬取动态链接和静态链接两种方式)       
More stable, more convenient, download with batch_size 30 (提高了爬虫的容错率、稳定性,每30个一批进行图片下载)       
Naming with fixed size, easy to sort by file manager (爬取图片命名兼顾考虑了文件管理器排序规则，通过定长命名（例如：00001）这种以图片需求总数位数为长度、其余位填充零的方式实现图片的有序排列)    

### How to use (使用方法):
- use path /acjson to crawl dynamic pages (通过/acjson路径爬取动态网页) 
> (Recommended, faster and more stable than the other)
``` python
python3 dynamic_acjson_crawler.py
```
- use path /flip to crawl static pages (通过/flip路径爬取静态网页)
``` python
python3 static_flip_crawler.py
```

### Result Show (效果):
```
请输入图片搜索关键字: 硬盘
请输入图片需求数量: 200
正在检测图片总数，请稍等.....
图片总数超过200张，远大于需求数量,通过合理性检验
100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 30/30 [00:04<00:00,  6.98it/s]
100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 30/30 [00:20<00:00,  1.48it/s]
100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 30/30 [00:04<00:00,  6.92it/s]
100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 30/30 [00:04<00:00,  7.03it/s]
100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 30/30 [00:05<00:00,  5.97it/s]
100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 30/30 [00:04<00:00,  6.78it/s]
 63%|█████████████████████████████████████████████████████████████████████████▍                                          | 19/30 [00:02<00:01,  6.73it/s]
100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 200/200 [00:46<00:00,  4.32it/s]
 爬取成功
```

### Examples (下载完成图片样例):
All the images I've downloaded are in the example_images repo. (图片样例在example_images文件夹里)


***
Support from you is my greatest encouragement! (您的支持是对我的最大鼓励！)       
Thanks a lot! (谢谢充电！)       
![wechatpay](https://github.com/DenryDu/DenryDu.github.io/blob/master/image_upload/wechat_charge.png)
![alipay](https://github.com/DenryDu/DenryDu.github.io/blob/master/image_upload/alipay_charge.jpg)

