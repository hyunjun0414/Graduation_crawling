import os
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup
import firebase_admin
from firebase_admin import credentials, firestore
from allergy_information import get_allergens

# 1. 음식 이름 크롤링
url = "https://cjhong.tistory.com/604"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# 해당 <tr> 태그 내의 모든 <span> 태그를 선택합니다.
food_spans = soup.select(
    'tr td span[style="font-family: \'Noto Sans Demilight\', \'Noto Sans KR\';"]')


# <span> 태그 내의 텍스트를 리스트로 저장합니다.
foods = [span.text for span in food_spans if span.text.strip() != ""]


# 2. Firestore에 저장
# Firebase Admin SDK 초기화
load_dotenv()
api_key = os.environ.get("MY_API_KEY")
cred = credentials.Certificate(api_key)  # 서비스 계정 키의 경로를 지정해주세요.
firebase_admin.initialize_app(cred)

db = firestore.client()

# 크롤링한 음식 리스트를 Firestore에 저장
for food in foods:
    # 문서 ID로 사용하기 위해 음식 이름에서 특수 문자와 공백을 제거
    food_id = ''.join(e for e in food if e.isalnum())
    allergens_value = get_allergens(food)
    food_doc_ref = db.collection('foods').document(food_id)
    food_doc_ref.set({
        'name': food,
        'allergens': allergens_value,
        'description': None
    })

print("All foods have been added to Firestore!")
