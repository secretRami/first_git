# 1. requests모듈을 import한다
import requests



#r = requests.get('
# http://comic.naver.com/webtoon/list.nhn <-이 부분 뗴어내고
#  ?                             //- 얘랑
# titleId=637931 <-이 부분 떼어냄
# &weekday=thu')                 //- 앤 뭐지?


# 2. 통으로 requests.get 보냈던걸 분리해서 주소는 url에, 웹툰의id값은 params에 저장한다
url = 'http://comic.naver.com/webtoon/list.nhn'
params = {'titleId' : '637931'}

# 3. 분리해서 url과 params변수에 저장한 값을 requests.get으로 가져와 사용한다
r = requests.get(url, params=params)

# 4. 결과 확인
print(r.url)


## http://comic.naver.com/webtoon/list.nhn?titleId=637931으로 출력됨을 볼 수 있다
