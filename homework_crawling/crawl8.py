# 1. requests모듈을 import한다
#    BeautifulSoup을 import한다
import requests
from bs4 import BeautifulSoup

# 2. 여긴 crawl7에서 한 부분
url = 'http://comic.naver.com/webtoon/list.nhn'
params = {'titleId' : '637931'}
r = requests.get(url, params=params)
html_doc = r.text
soup = BeautifulSoup(html_doc, 'lxml')


## crawl7과 같지만 이번엔 tr를 찾음

# 3. tr_list변수를 만들고, soup에서 tr태그를 몽땅 찾아넣음(find_all)
tr_list = soup.find_all('tr')


# 4. for문을 돌려준다
for index, tr in enumerate(tr_list):

    # tr_list에 들어가있는 tr에서 td를 모두 찾아 td_list에 저장함
    td_list = tr.find_all('td')

    # index 는 tr의 갯수를 세어서 번호매긴 거
    # td_list가 4인 건 tr 하나에 들어있는 td가 이미지, 제목, 별점, 등록일 이렇게 4개라서
#    print(index, len(td_list))
    print('{} : {}'.format(index, len(td_list))) # 예쁘게 보기위해 fomat으로 형식 만들어줌


# 5. 결과 확인




## enumerate는 "열거하다"라는 뜻이다.
#   이 함수는 순서가 있는 자료형(리스트, 튜플, 문자열)을 입력으로 받아
#   인덱스 값을 포함하는 enumerate 객체를 리턴한다.