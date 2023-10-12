# -*- coding: utf-8 -*-


import os
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup
import firebase_admin
from firebase_admin import credentials, firestore


URL = "https://www.boseongatopycenter.kr/contentsView.do?pageId=www31"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# 웹 서버의 응답을 받아온 객체.
response = requests.get(URL, headers=headers)


# HTML 테이블에서 데이터를 추출하고 이를 파싱하여 Python 딕셔너리 형식으로 반환하는 함수
def parse_table(html):
    soup = BeautifulSoup(html, 'html.parser')
    food_list = []

    # 첫 번째 tr 태그 안의 모든 td 태그를 찾습니다.
    columns = soup.find('tr').find_all('td')

    for column in columns:
        # 각 td 태그의 텍스트를 콤마로 구분하고, 앞뒤 공백을 제거합니다.
        foods = [food.strip() for food in column.text.split(',')]
        food_list.extend(foods)

    return food_list


# 응답 처리
if response.status_code == 200:

    # 첫 번째 테이블 데이터
    html1 = """<tbody><tr><td>계란, 달걀, 시금치, 옥수수, 샐러리, 감자, 돼지고기, 소고기, 닭고기, 포도주, 고등어, 청어</td>
    <td>오징어, 게, 갑각류, 연체동물, 상어, 농어, 오렌지</td>
    <td>가지, 버섯, 땅콩, 참마, 토란, 메밀, 도토리</td>
    <td>바나나, 파인애플, 키위</td>
    <td>초코렛, 치즈</td>
    <td>연어, 대구,꽁치, 가자미</td>
    <td>토마토, 오이</td></tr></tbody>"""
    food_list = parse_table(html1)

    # 결과 출력 (또는 Firestore에 저장)
    print(food_list)


else:
    print("Error:", response.status_code)


# Firebase Admin SDK 초기화
load_dotenv()
api_key = os.environ.get("MY_API_KEY")
cred = credentials.Certificate(api_key)  # 서비스 계정 키의 경로를 지정해주세요.
firebase_admin.initialize_app(cred)

db = firestore.client()


# Firestore에 데이터 저장
collection_ref = db.collection('menu')  # 적절한 컬렉션 이름으로 변경해주세요.

# 데이터 저장
combined_food_list = {
    "data1": food_list,

}

doc_ref = collection_ref.add(combined_food_list)
