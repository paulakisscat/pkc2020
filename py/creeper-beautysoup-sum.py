#！获取 Travel这类书中，所有书的书名、评分、价格三种信息，并且打印提取到的信息
import requests
from bs4 import BeautifulSoup
res = requests.get('http://books.toscrape.com/catalogue/category/books/travel_2/index.html')
bs = BeautifulSoup(res.text, 'html.parser')

items = bs.findAll(class_='product_pod')
# print(items)

for tags_books in items:
    tag_name = tags_books.find('h3').find('a')
    # print(tag_name)
    tag_price = tags_books.find('p', class_='price_color')
    # print(tag_price)
    tags_star = tags_books.find('p', class_='star-rating')
    # print(tags_star)

    # 输出书名
    # print(tag_name['title'])
    print(tag_name.text)

    # 输出价格
    print(tag_price.text)

    # 输出星级
    print(tags_star['class'][1])

# 爬取博客【人人都是蜘蛛侠】首页四篇文章
# 标题、发布时间、文章链接
res = requests.get('https://wordpress-edu-3autumn.localprod.oc.forchange.cn/')
# print(res.status_code)
bs = BeautifulSoup(res.text, 'html.parser')

tags_article = bs.findAll('header', class_='entry-header')
# print(tags_article)
for tag_article in tags_article:
    article_time = tag_article.find(class_='entry-date published').text
    article_link = tag_article.find(class_='entry-title').find(rel='bookmark')['href']
    article_name = tag_article.find(class_='entry-title').text
    
    print(article_name+'发布于'+article_time+'\t'+article_link)