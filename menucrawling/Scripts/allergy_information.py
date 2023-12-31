ALLERGENS_MAPPING = {
    "시금치": ["시금치"],
    "옥수수": ["옥수수", "콘"],
    "샐러리": ["샐러리"],
    "감자": ["감자"],
    "와인": ["포도주", "와인"],
    "가지": ["가지"],
    "버섯": ["버섯"],
    "땅콩": ["땅콩"],
    "참마": ["참마"],
    "토란": ["토란"],
    "메밀": ["메밀"],
    "도토리": ["도토리"],
    "밀가루": ["떡", "국수", "만두", "면", "짬뽕"],
    "고춧가루": ["고춧가루"],
    "돼지고기": ["돼지고기", "돈", "만두", "소세지", "순대", "스팸", "짜장", "짬뽕", "제육", "베이컨"],
    "소고기": ["소고기", "육", "불고기", "사골", "스테이크", "햄버거"],
    "닭고기": ["닭고기", "닭", "오리"],
    "계란": ["계란", "달걀"],
    "초코렛": ["초코렛", "초코"],
    "치즈": ["치즈"],
    "고등어": ["고등어"],
    "청어": ["청어"],
    "오징어": ["오징어"],
    "꽃게": ["꽃게", "게"],
    "갑각류": ["갑각류", "새우", "전복", "랍스터", "랍스타", "굴", "홍합", "해물"],
    "연체동물": ["연체동물", "오징어", "문어", "쭈꾸미"],
    "농어": ["농어"],
    "연어": ["연어"],
    "대구": ["대구"],
    "꽁치": ["꽁치"],
    "가자미": ["가자미"],
    "생선": ["생선"],
    "낙지": ["낙지", "낙"],
    "바나나": ["바나나"],
    "파인애플": ["파인애플"],
    "키위": ["키위"],
    "오렌지": ["오렌지"],
    "토마토": ["토마토"],
    "오이": ["오이"]
}


def get_allergens(food_name):
    detected_allergens = [allergen for allergen, keywords in ALLERGENS_MAPPING.items(
    ) for keyword in keywords if keyword in food_name]
    return ', '.join(detected_allergens) if detected_allergens else None
