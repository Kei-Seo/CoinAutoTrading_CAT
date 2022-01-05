# 파이썬에서 웹 페이지의 데이터를 가져오기 위해서
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/item/main.nhn?code=000660"
html = requests.get(url).text # html 코드를 다운받아온다.

soup = BeautifulSoup(html, "html5lib")
# html 데이터와 HTML 문서를 파싱하는데 사용할 모듈의 이름인 "html5lib"
tags = soup.select("#_per")
tag = tags[0]
print(tag.text)
