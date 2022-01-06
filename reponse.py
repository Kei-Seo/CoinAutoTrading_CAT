# 파이썬에서 웹 페이지의 데이터를 가져오기 위해서
import datetime

import requests
from bs4 import BeautifulSoup


def get_per(code):

    url = "https://finance.naver.com/item/main.nhn?code=" + code
    html = requests.get(url).text # html 코드를 다운받아온다.

    soup = BeautifulSoup(html, "html5lib")
    # html 데이터와 HTML 문서를 파싱하는데 사용할 모듈의 이름인 "html5lib"
    tags = soup.select("#_per")
    tag = tags[0]
    return float(tag.text)


def get_dividend(code):
    url = "https://finance.naver.com/item/main.nhn?code=" + code
    html = requests.get(url).text  # html 코드를 다운받아온다.

    soup = BeautifulSoup(html, "html5lib")
    # html 데이터와 HTML 문서를 파싱하는데 사용할 모듈의 이름인 "html5lib"
    tags = soup.select("#_dvr")
    tag = tags[0]
    return float(tag.text)

def get_foreigner(code):
    url = "https://finance.naver.com/item/main.nhn?code=" + code
    html = requests.get(url).text  # html 코드를 다운받아온다.

    soup = BeautifulSoup(html, "html5lib")
    # html 데이터와 HTML 문서를 파싱하는데 사용할 모듈의 이름인 "html5lib"
    tags = soup.select("#tab_con1 > div:nth-child(3) > table > tbody > tr.strong > td > em")
    for tag in tags:
        print(tag.text)

r = requests.get("https://api.korbit.co.kr/v1/ticker/detailed?currency_pair=btc_krw")
print(r.text) # r은 str
bitcoin = r.json() # str -> dic
timestamp = bitcoin["timestamp"]
print(timestamp)
date = datetime.datetime.fromtimestamp(timestamp/1000)
print(date)
#print(get_per("000660"))
#get_foreigner("000660")
#print(get_dividend("000660"))
