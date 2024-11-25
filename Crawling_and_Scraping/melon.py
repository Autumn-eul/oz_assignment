import requests
from bs4 import BeautifulSoup

header_user = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"}

url = "https://www.melon.com/chart/index.htm"
req = requests.get(url, headers=header_user)

html = req.text
soup = BeautifulSoup(html, "html.parser")

# 멜론 차트 top100
lst50 = soup.select(".lst50") # 리스트와 동일한 형태라 인덱스를 가지고 있다.
lst100 = soup.select(".lst100")
lst_all =  lst50 + lst100

# 순위, 제목, 가수, 앨범
for rank, i in enumerate(lst_all, 1):
    title = i.select_one(".ellipsis.rank01 a").text
    singer = i.select_one(".checkEllipsis").text # i.select_one(".ellipsis.rank02 a").text
    album = i.select_one(".ellipsis.rank03 a").text

    print(f"[순위] : {rank}")
    print(f"[제목] : {title}")
    print(f"[가수] : {singer}")
    print(f"[앨범] : {album}")
    print("-" * 70)

# for i in lst_all:
#     rank = i.select_one(".rank").text
#     title = i.select_one(".ellipsis.rank01").text
#     singer = i.select_one(".ellipsis.rank02").text
#     album = i.select_one(".ellipsis.rank03").text

#     print(f"순위 : {rank}")
#     print(f"제목 : {title}")
#     print(f"가수 : {singer}")
#     print(f"앨범명 : {album}")
#     print("-" * 100)

#     i += 1