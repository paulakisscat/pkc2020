#!爬虫 获取HTML页面源文件内容

import requests


# 获取
res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men4.0.html')

# 解析+提取
html = res.text 


print('响应状态码',res.status_code)

print(html)

htmlcontent = open('websourcescon.txt', 'a+')

# 存储
htmlcontent.write(html)

htmlcontent.close()




