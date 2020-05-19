import requests
from bs4 import BeautifulSoup

headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
res = requests.get('http://www.xiachufang.com/explore/', headers = headers)
print(res.status_code)
print(type(res))

#! 菜名、原材料、详细烹饪流程的URL
#! 先把数据存到列表里：每一组菜名、URL、食材是一个小列表，小列表组成一个大列表
#! [[菜A,URL_A,食材A],[菜B,URL_B,食材B],[菜C,URL_C,食材C]]
#! 先去爬取所有的最小父级标签<div class="info pure-u">，然后针对每一个父级标签，想办法提取里面的菜名、URL、食材

bs = BeautifulSoup(res.text, 'html.parser')
print('bs类型：')
print(type(bs))

#! method1
# tags_food = bs.findAll('div', class_='info pure-u')
# print(type(tags_food))

#! thinking1
# tag_a = tags_food[0].find('a')
# food_name = tag_a.text.strip()
# food_link = 'http://www.xiachufang.com'+tag_a['href']
# food_formula = tags_food[0].find('p', class_='ing ellipsis').text.strip()

# list_foods = []
# for tag_food in tags_food:
#     food_name = tag_food.find('a').text.strip()
#     food_formula = tag_food.find('p', class_='ing ellipsis').text.strip()
#     food_link = 'http://www.xiachufang.com'+tag_food.find('a')['href']
#     list_food = [food_name, food_formula, food_link]
#     # print(list_food)
#     list_foods.append(list_food)
# print(list_foods)

#! method2
# 查找所有包含菜名和URL的<p>标签
tags_name = bs.find_all('p',class_='name')
# print(type(tags_name))
# 查找所有包含食材的<p>标签
tags_formular = bs.find_all('p',class_='ing ellipsis')
# print(len(tags_name))
list_foods = []
for count in range(len(tags_name)):
    food_name = tags_name[count].text.strip()
    food_fomular = tags_formular[count].text.strip()
    food_link = 'http://www.xiachufang.com'+tags_name[count].find('a')['href']
    list_food = [food_name, food_fomular, food_link]
    list_foods.append(list_food)
print(list_foods)





















