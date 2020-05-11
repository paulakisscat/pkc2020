#!爬虫 获取HTML页面源文件内容

import requests

res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men4.0.html')

html = res.text

print('响应状态码',res.status_code)

print(html)

htmlcontent = open('websourcescon.txt', 'a+')

htmlcontent.write(html)

htmlcontent.close()




