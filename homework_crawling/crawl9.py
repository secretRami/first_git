# 1. requests모듈을 import한다
#    BeautifulSoup을 import한다
import requests
from bs4 import BeautifulSoup

# 2. 여긴 crawl8에서 한 부분
url = 'http://comic.naver.com/webtoon/list.nhn'
params = {'titleId' : '637931'}
r = requests.get(url, params=params)
html_doc = r.text
soup = BeautifulSoup(html_doc, 'lxml')


# 3. tr_list변수를 만들고, soup에서 tr태그를 몽땅 찾아넣음
tr_list = soup.find_all('tr')


# 4. for문을 돌려준다
for index, tr in enumerate(tr_list):
    td_list = tr.find_all('td')


    if len(td_list) < 4:
        continue

    # td_list의 index마다 변수를 만들어준다
    td_thumbnail = td_list[0]
    td_title = td_list[1]    #//- 이거랑
    td_rating = td_list[2]
    td_created = td_list[3]  #//- 이거 사용

    # 위에 index를 넣어둔 변수를 가져와서 값을 받아올 수 있게 만들고, 변수에 넣어준다
    title = td_title.get_text(strip=True)
    created = td_created.get_text(strip=True)

    # 5. 결과 확인
    print(title, created)




#  결과를 토대로 웹 페이지를 뜯어보면, title은 'STAGE 102 - 저것들 못 말립니다'로 제목이고,
#  created는 '2016.12.21'로 작성일자임을 알 수 있다

## enumerate는 "열거하다"라는 뜻이다.
#   이 함수는 순서가 있는 자료형(리스트, 튜플, 문자열)을 입력으로 받아
#   인덱스 값을 포함하는 enumerate 객체를 리턴한다.