#!爬虫 获取HTML页面源文件内容

import requests

res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men4.0.html')

webcontent = res.text

websources = open('websourcescon.txt', 'a+')

websources.write(webcontent)

websources.close()


