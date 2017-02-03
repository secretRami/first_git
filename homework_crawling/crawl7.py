# 1. requests모듈을 import한다
#    BeautifulSoup을 import한다
import requests
from bs4 import BeautifulSoup

# 2. 여긴 crawl6에서 한 부분
url = 'http://comic.naver.com/webtoon/list.nhn'
params = {'titleId' : '637931'}
r = requests.get(url, params=params)
html_doc = r.text
soup = BeautifulSoup(html_doc, 'lxml')


## crawl6과 같지만 이번엔 td를 찾음

# 3. td_list변수를 만들고, soup에서 td태그, 클래스가 title로 지정된 것을 몽땅 찾아넣음
td_list = soup.find_all('td', class_='title')

# 4. for문을 돌려서 td_list안에 들어간 td태그의 text를 불러옴
for td in td_list:
#    print(td.get_text())  //- 그냥 이렇게 출력하면 공백이 너무 많음
    print('{}'.format(td.get_text().strip()))  # //- 그래서 strip을 사용함(아마도)

# 5. 결과 확인


## 이제 슬슬 무언가 보이기 시작한다
#  결과에 모든 td의 text가 보인다

