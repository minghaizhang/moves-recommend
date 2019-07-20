# -*- coding: utf-8 -*-
#create by "小郑同学"

import pandas as pd
movies_data=pd.read_csv('movies.csv')
ratings_data=pd.read_csv('ratings.csv')

print (movies_data)

#合并
data=pd.merge(movies_data,ratings_data)
data.drop('timestamp',1,inplace=True)    #删除列，可写可不写，不会产生影响

#print(data)

#评价最多的 20 部电影
data.title.value_counts()[:20]

#评价最高的电影
import numpy as np

movie_ratings=data.groupby('title').agg({'rating':[np.size,np.mean]})
movie_ratings.head()

movie_ratings.sort_values([('rating','mean')],ascending=False).head(5)    #评分最高前5名
movie_ratings[movie_ratings['rating']['size']>=150].sort_values([('rating','mean')],ascending=False).head()


fans=data[data['rating']>=3.5]
fans.title.value_counts()[:10]

#推荐电影
import re
name=input('Please input the movie name(or keywords): ')
name=name.title()            #首字母大写
mov=movies_data[movies_data['title'].str.contains(name)]

#提取电影名字
y=str(mov['genres']).strip('Name: genres, dtype: object').strip()
p = re.compile(r'\D+')
result=p.findall(y)
res=result[0].strip()

movie_lists=movies_data[movies_data['genres']==res]
print (movie_lists)