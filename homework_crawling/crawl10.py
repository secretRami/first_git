# crawl9.py에서 만들었던 내용을쪼개서 함수로 만들어준다


# 1. 첫번째 함수만들기

import requests
from bs4 import BeautifulSoup

def get_soup_fron_url(url, params=None):
    '''
    url과 parameter를 사용해서 해당 URL에 GET요청을 보낸 결과(HTML text)로
    뷰티풀숲 객체를 생성해 보관
    :param url: GET 요청을 보낼 URLstring
    :param params: GET요청을 보낼 매개변수 dict
    :return: BeautifulSoup object
    '''
    r = requests.get(url, params=params)
    html_doc = r.text
    soup = BeautifulSoup(html_doc, 'lxml')
    return soup


# 이 함수에선 매개변수로 url, params를 받으므로,
# 원래 바로 변수에 저장해서 사용했던 url과 params는 다른 함수로 만들어진다
# url = 'http://comic.naver.com/webtoon/list.nhn'
# params = {'titleId' : '637931'}

###############

# 2. 두번째 함수만들기

def  get_soup_from_naver_webtoon_by_page(webtoon_id, page=1):
    '''
    네이버 웹툰의 만화 고유 ID (URL paramter중 titleID)와
    페이지 번호(URL GET paramter 중 page)를 받아서
    해당 만화의 페이지(num)의 HTML을 BeautifulSoup객체로 반환시킨다
    :param webtoon_id: 네이버 웹툰의 고유 ID
    :param page: 주어지지 않을 경우 1페이지를 요청함
    :return: BeautifulSoup object
    '''

    # 네이버 웹툰 사이트를 지정한다
    url = 'http://comic.naver.com/webtoon/list.nhn'

    # GET paramter로 전달할 값들의 dict
    params = {'titleId' : webtoon_id, 'page' : page}

    #이것들은 get_soup_from_url 함수의 인자가 된다
    return get_soup_from_url(url,params)

###############

# 4. 네번째 함수만들기

def get_webtoon_recent_episode_number(webtoon_id):
    '''
    웹툰의 페이지, 첫 화 (페이지의 가장 최신화)의 링크에서
    가장 최신화의 번호(= 현재까지 연재한 횟수)를 가져온다
    :param webtoon_id: 웹툰 고유 id
    :return: 최신 에피소드 번호(= 총 연재횟수)
    '''

    # 만화 목록 1페이지 html로부터 이 만화가 총 몇 화 연재중인지 가져온다
    soup = get_soup_from_naver_webtoon_by_page(webtoon_id)

    tr_list = soup.find_all('tr')

    #
    recent_episode_number = None

    for tr in tr_list:
        td = tr.find('td', class_='title')
        if td:
            a = tr.find('a')
            href = a.get('href')

            import re
            p = re.compile(r'.*[?&]no=(\d+)&.*')
            m = re.match(p, href)

            if m:
                recent_episode_number = m.group(1)
                break

    return int(recent_episode_number)

#################

# 3. 세번째 함수만들기 //- 이 함수가 어떻게 작용하는지 한번 더 띁어볼 것

def get_episode_list_from_page(webtoon_id, page=1):

    soup = get_soup_from_naver_webtoon_by_page(webtoon, page)

    #
    episode_list = []
    #
    tr_list = soup.find_all('tr')

    for index, tr in enumerate(tr_list):
        td_list = tr.find_all('td')

        if len(td_list) < 4:
            continue

        td_thumbnail = td_list[0]
        td_title = td_list[1]    #//- 이거랑
        td_rating = td_list[2]
        td_created = td_list[3]  #//- 이거 사용

        title = td_title.get_text(strip=True)
        created = td_created.get_text(strip=True)

        # 여기에 link를 추가해서 href주소 긁어옴
        # 위에서 td_list[1]을 담은 td_title을 가져와서 a태그를 찾아 href를 link변수에 넣는다
        link = td__title.find('a').get('href')

        cur_episode = {
            'title' : title,
            'created' : created,
            'link' : link
        }

        episode_list.append(cur_episode)

    return episode_list

###################

# 5. 다섯번째 함수 만들기

def get_webtoon_episode_list(webtoon_id):
    page_count = 10
    total_episode_list = []

    total_episode_number = get_webtoon_recent_episode_number(webtoon_id)

    import math

    total_page_number = math.ceil(total_episode_number / page_count)

    for i in range(total_page_number):
        cur_page_num = i + 1

        cur_episode_list = get_episode_list_from_page(webtoon_id, cur_page_num)
        total_episode_list.extㅉend(cur_episode_list)

    return total_episode_list




WEBTOON_ID = 637931

result = get_episode_list_from_page(WEBTOON_ID)
for item in result:
    print(item)

