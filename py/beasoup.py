#！ 爬虫
#！ 解析&提取 BeautifulSoup

import requests
from bs4 import BeautifulSoup




# 获取
# res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html')#获取网页源代码，得到的res是response对象
# print(res.status_code) #检查请求是否正确响应
# print(type(res.text))


#解析
# soup = BeautifulSoup(res.text,'html.parser')
# print(soup)
# print(type(soup))



# 获取https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html中
# 书名
# 链接
# 介绍

# 获取
res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html#type2')
html = res.text

#解析
soup = BeautifulSoup(html,'html.parser')

#提取
# items = soup.find_all('div', class_='books')
items = soup.find_all(class_='books')
# print(items)
# print(type(items))

#循环遍历列表中的数据
for item in items:
    # print('想找的数据都在这里了：\n', item)
    # # print(type(item))

#     < div
#
#
#     class ="books" >
#
#     < h2 > < a
#     name = "type1" > 科幻小说 < / a > < / h2 >
#     < a
#     href = "https://book.douban.com/subject/27077140/"
#
#
#     class ="title" > 《奇点遗民》 < / a >
#
#     < p
#
#
#     class ="info" > 本书精选收录了刘宇昆的科幻佳作共22篇。《奇点遗民》融入了科幻艺术吸引人的几大元素：数字化生命、影像化记忆、人工智能、外星访客……刘宇昆的独特之处在于，他写的不是科幻探险或英雄奇幻，而是数据时代里每个人的生活和情感变化。透过这本书，我们看到的不仅是未来还有当下。
#
#     < / p >
#     < img
#
#
#     class ="img" src="./spider-men5.0_files/s29492583.jpg" >
#
#     < br >
#     < br >
#     < hr
#     size = "1" >
# < / div >
    kind = item.find('h2')  # 在列表中的每个元素里，匹配标签<h2>提取出数据
    title = item.find(class_='title')  # 在列表中的每个元素里，匹配属性class_='title'提取出数据
    brief = item.find(class_='info')  # 在列表中的每个元素里，匹配属性class_='info'提取出数据
    # print(kind, '\n', title, '\n', brief)  # 打印提取出的数据
    # print(type(kind), type(title), type(brief))  # 打印提取出的数据类型
    print(kind.text,'\n',title.text,'\n',title['href'],'\n',brief.text)








