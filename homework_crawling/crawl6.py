# 1. requests모듈을 import한다
#    BeautifulSoup을 import한다
import requests
from bs4 import BeautifulSoup

# 2. 여긴 crawl5에서 한 부분
url = 'http://comic.naver.com/webtoon/list.nhn'
params = {'titleId' : '637931'}
r = requests.get(url, params=params)
html_doc = r.text
soup = BeautifulSoup(html_doc, 'lxml')

# 3. a_list변수를 만들고, soup에서 a태그를 몽땅 찾아넣음(find_all)
a_list = soup.find_all('a')

# 4. for문을 돌려서 a_list안에 들어간 a태그의 주소를 불러옴(href)
for a in a_list:
    print(a.get('href'))

# 5. 결과 확인


## 이제 슬슬 무언가 보이기 시작한다
#  결과에 모든 href가 들어가있는 걸 볼 수 있다

