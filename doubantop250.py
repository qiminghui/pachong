# 导入模块
import csv, openpyxl
import requests 
from bs4 import BeautifulSoup

# 定义一个csv文件
with open('douban.csv', 'w+', newline='', encoding='utf-8-sig') as f:
    writer = csv.writer(f)
    writer.writerow(['序号','电影名','评分','推荐语'])
# 设置循环获取更新页码
    for x in range(10):
        url = 'https://movie.douban.com/top250?start=' + str(x*25) +'&filter='
        res = requests.get(url)
        bs = BeautifulSoup(res.text, 'html.parser') # 将text文件转化为bs
        bs_movie = bs.find('ol', class_='grid_view') 
        for x in bs_movie.find_all('li'):
            num = x.find('em').text
            title = x.find('span', class_='title').text
            score = x.find('span', class_='rating_num').text
            inq = x.find('span', class_='inq')
            try:
                print('-----------------\n'+ num + title + score +'\n'+inq.text)
                writer.writerow([num,title,score,inq.text])
            except AttributeError:
                print('-----------------\n'+ num + title + score +'\n'+'there is no discrition')
                writer.writerow([num,title,score,'there is no discrition'])
                