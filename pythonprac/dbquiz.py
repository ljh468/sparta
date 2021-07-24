import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

# 영화제목 '나 홀로 집에'의 평점을 가져오기 (metrix)
movie = db.movies.find_one({'title':'나 홀로 집에'})
onlyhome_point = movie['star']
print('quiz01 : ', onlyhome_point)

# '나 홀로 집에'의 평점과 같은 평점의 영화 제목들을 가져오기
all_movies = list(db.movies.find({'star':onlyhome_point}))
print('quiz02 : ')
for movie in all_movies:
    title = movie['title']
    print(title)

# 매트릭스 영화의 평점을 0으로 만들기
db.movies.update_one({'title':'매트릭스'},{'$set':{'star':'0'}})