# 1. requests모듈을 import한다
import requests


# 2. requests의 get을 통해 가져올 홈페이지의 주소를 적어넣는다
r = requests.get('http://comic.naver.com/webtoon/list.nhn?titleId=637931&weekday=thu')

# 3. 결과 확인
print(r)