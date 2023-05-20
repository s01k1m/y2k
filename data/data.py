import requests
import json
from pprint import pprint

file_path = "./movie_data.json"

# API 지정
apikey = "5056d5947b6f2c6e202377ace3152f12"

# 정보를 알고 싶은 영화 리스트 만들기
movie_list = range(1, 100)

# API 지정
movie_api = "https://api.themoviedb.org/3/movie/popular?language=ko-KR&page={page}&api_key={key}"
genre_api = "https://api.themoviedb.org/3/genre/movie/list?language=ko-KR&api_key={key}"

# string.format_map() 매핑용 클래스 만들기
class Default(dict):
    def __missing__(self, key):
        return key

# 장르정보 추출
# API의 URL 구성하기
url = genre_api.format_map(Default(key=apikey))
# API에 요청을 보내 데이터 추출하기
r = requests.get(url)  # json 형태의 데이터가 나온다.
# 결과를 JSON 형식으로 변환하기
raw_data = json.loads(r.text)['genres']
genre_list = {}
for genre in raw_data:
    genre_list[genre['id']] = genre['name']


data = []
# 각 영화의 정보 추출하기
for page in movie_list:
    # print(f"#############{page}#############")
    # API의 URL 구성하기
    url = movie_api.format_map(Default(movies=page, key=apikey))
    # API에 요청을 보내 데이터 추출하기
    r = requests.get(url)  # json 형태의 데이터가 나온다.
    # 결과를 JSON 형식으로 변환하기
    raw_data = json.loads(r.text)['results']

    for d in raw_data:
        movie = {"model" : "stills.moive", "pk": page, "fields" : {}}
        movie["fields"]['movie_id'] = d['id']
        movie["fields"]['movie_title'] = d['title']
        movie["fields"]['movie_released_date'] = d['release_date']
        movie["fields"]['overview'] = d['overview']
        movie["fields"]['genre'] = []
        for genre in d['genre_ids']:
            movie["fields"]['genre'].append(genre_list[genre])
        data.append(movie)

with open(file_path, 'w', encoding='utf-8') as outfile:
    json.dump(data, outfile, indent=4, ensure_ascii=False)

print('finished')