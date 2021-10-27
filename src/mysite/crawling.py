'''
Created on 2021. 8. 13.

@author: pc368
'''
import csv
from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
#크롤링한 데이터를 csv 파일로 만들기

def search():
    print('크롤링 작업 중입니다.')
    # url = f'https://section.blog.naver.com/Search/Post.naver?pageNo=1&rangeType=ALL&orderBy=sim&keyword={quote_plus(search)}'
    url = f'https://m.search.naver.com/search.naver?where=m_view&sm=mtb_jum&query={quote_plus(search)}'
    html = urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    total = soup.select('.api_txt_lines.total_tit')
    #저장 작업
    data = []
    for i in total:
        # print(i.text)
        # print(i.attrs['href'])
        data.append([i.text,i.attrs['href']])
    return data
            
if __name__ == '__main__':
    data = search('인공지능')
    for x in data:
        print(x)