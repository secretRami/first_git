# 1. requests모듈을 import한다
#    BeautifulSoup을 import한다
import requests
from bs4 import BeautifulSoup

# 2. 여긴 crawl4에서 한 부분
url = 'http://comic.naver.com/webtoon/list.nhn'
params = {'titleId' : '637931'}
r = requests.get(url, params=params)
html_doc = r.text

# 4. BeautifulSoup에 'lxml'을 인자로 추가한다
soup = BeautifulSoup(html_doc, 'lxml')

# 5. 결과 확인
print(soup.title)
print(soup.title.name)
print(soup.title.string)


## 결과는 나오는데 이게 뭘 가져온건지 모르겠음






## lxml?
# python 언어로 XML과 HTML을 처리할 수 있는 라이브러리이다

## XML?
#  eXtensible Markup Language의 약어.
#  W3C에서 여러 특수 목적의 마크업 언어를 만드는 용도에서 권장되는 다목적 마크업 언어이다.
#  데이터에 의미를 부여하는 메타데이터를 기술할 수 있다
#  인터넷으로 연결된 시스템끼리 쉽게 식별 가능한 데이터를 주고받을 수 있게 된다