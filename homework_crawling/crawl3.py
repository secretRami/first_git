# 1. requests모듈을 import한다
import requests


# 2. 여긴 crawl2에서 한 부분
url = 'http://comic.naver.com/webtoon/list.nhn'
params = {'titleId' : '637931'}
r = requests.get(url, params=params)

# 3. html text를 가져와서 t 에 저장한다
t = r.text

# 4. 결과 확인
print(t)


## html에 쓰여진 text를 그대로 긁어와서 출력하는 걸 볼 수 있다 ...길다