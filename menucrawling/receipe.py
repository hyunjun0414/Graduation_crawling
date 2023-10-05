import requests
from bs4 import BeautifulSoup
import firebase_admin
from firebase_admin import credentials, firestore




URL = "https://cjhong.tistory.com/604"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# 웹 서버의 응답을 받아온 객체.
response = requests.get(URL, headers=headers)

# 응답 처리
if response.status_code == 200:

    html ="""<table style="border-collapse: collapse; width: 100%; height: 314px;" border="1" data-ke-align="alignLeft" data-ke-style="style7">
<tbody>
<tr style="height: 20px;">
<td style="text-align: center; height: 20px;"><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';"><b>밥</b></span></td>
<td style="text-align: center; height: 20px;"><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';"><b>죽</b></span></td>
<td style="text-align: center; height: 20px;"><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';"><b>볶음밥 / 덮밥</b></span></td>
</tr>
<tr style="height: 294px;">
<td style="text-align: center; height: 294px;"><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">잡곡밥</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">옥수수밥</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">감자밥</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">무밥</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">명란버터밥</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">비빔밥</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">가지밥</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">전복밥</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">콩나물밥</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">곤드레비빔밥</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">표고버섯영양밥</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">쌈밥</span></td>
<td style="text-align: center; height: 294px;"><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">야채죽</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">전복죽</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">새우죽</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">삼계죽</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">미역죽</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">참치죽</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">소고기버섯죽</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">팥죽</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">단호박죽</span></td>
<td style="text-align: center; height: 294px;"><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">베이컨볶음밥</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">김치볶음밥</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">간장계란밥</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">소고기볶음밥</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">스팸볶음밥</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">해물볶음밥</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">새우볶음밥</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">카레덮밥</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">짜장밥</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">오징어덮밥</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">오므라이스</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">육회비빔밥</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">김치알밥</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';"><br></span></td>
</tr>
</tbody>
</table>"""
    
    soup = BeautifulSoup(html, 'html.parser')

# 테이블의 헤더 추출
    headers = [header.text.strip() for header in soup.find_all('tr')[0].find_all('td')]

# 각 열의 항목들을 저장할 딕셔너리
    data_dict = {header: [] for header in headers}

# 테이블의 각 열에서 항목들 추출
    for header, column in zip(headers, soup.find_all('tr')[1].find_all('td')):
        items = column.find_all('span')
        data_dict[header].extend([item.text.strip() for item in items])

    print(data_dict)
else:
    print("Error:", response.status_code)
