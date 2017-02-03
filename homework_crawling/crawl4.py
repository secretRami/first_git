# 1. requests모듈을 import한다
#    BeautifulSoup을 import한다
import requests
from bs4 import BeautifulSoup

# 2. 여긴 crawl3에서 한 부분
url = 'http://comic.naver.com/webtoon/list.nhn'
params = {'titleId' : '637931'}
r = requests.get(url, params=params)

# 3. 긁어온 text를 html_doc 변수에 저장한다
html_doc = r.text

# 4. BeautifulSoup 객체를 생성하고 html_doc을 인자로 사용한다
soup = BeautifulSoup(html_doc)

# 5. 결과 확인. BeautifulSoup을 예쁘게 보여주기 위해 prettify를 사용한다
#    그냥 print(soup)만 하면 indent가 하나도 안되어있는 걸 볼 수 있다
print(soup.prettify())


## 역시나 html에 쓰여진 text를 그대로 긁어와서 출력하는 걸 볼 수 있다
#  그냥 텍스트를 가져오는 것과 soup를 사용하는것이 무슨 차이가 있는지 한번 더 알아보자


## 뷰티플수프는 HTML과 XML 파일로부터 데이터를 뽑아내기 위한 파이썬 라이브러리이다.