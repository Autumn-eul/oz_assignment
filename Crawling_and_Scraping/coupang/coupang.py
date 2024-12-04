import ftplib

from datetime import datetime # 시간 정보를 가져올 때 사용

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

#클래스, 아이디를 CSS_SELECTOR를 이용하기 위한 패키지
from selenium.webdriver.common.by import By
#키보드의 입력 형태를 코드로 작성하기 위한 패키지
from selenium.webdriver.common.keys import Keys
import time

header_user = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"

# 셀레니움 옵션 설정
options_ = Options()
options_.add_argument(f"User_Agent={header_user}")
options_.add_experimental_option("detach", True)
options_.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(options=options_)

# 검색 키워드 받기
keyword = input("검색할 상품 : ")
url = f"https://www.coupang.com/np/search?component=&q={keyword}"

# 완성된 주소로 크롬 열기
driver.get(url)
time.sleep(2)

# 열린 페이지의 html 소스 가져오기
html = driver.page_source
soup = BeautifulSoup(html, "html.parser") # 분석된 트리구조의 결과를 soup 변수에 담는다

items = soup.select("[class=search-product]") # ".search-product"

main_text = ""

for rank, item in enumerate(items, 1): # enumerate? : 반복가능한 객체를 원하는 갯수만큼 넣어서 증가시킬 수 있음
    name = item.select_one(".name").text
    price = item.select_one(".price-value").text
    link = item.a["href"]
    img_src = item.select_one(".search-product-wrap-img")
    rocket = item.select_one(".badge.rocket") # 로켓 배송이 있는 경우 : <span> ... </span> / 로켓 배송이 없는 경우 : None -> if 문을 만나면 false

    print(f"[{rank}]")
    print(f"제품명 : {name}")
    print(f"가격 : {price}원")

    if rocket:
        print("🚀 로켓 배송 가능")
    else:
        print("🚀 로켓 배송 불가")

    print(f"링크 : https://www.coupang.com{link}")

    if img_src.get('data-img-src'):
        img_url = f"http:{img_src.get('data-img-src')}"
    else:
        img_url = f"http:{img_src.get('src')}"

    img_url = img_url.replace("230x230ex", "600x600ex")
    print(f"이미지 URL : {img_url}")
    print("-" * 90)
    main_text += f"<p><h2>{rank}위 : {name}</h2><b>가격 : {price}</b></p><div><a href='https://www.coupang.com{link}' target='_blank'><div class='img main'><img src='{img_url}' alt='제품 이미지' /></div></div>"
    if rank == 10:
        break

now = datetime.now()
today = f"{now.year}년 {now.month}월 {now.day}일"
summary = f"{today} 기준 추천 {keyword} Top10"

file_name = 'oz.html'
title = f"오늘의 추천 {keyword}"

main = f"""<!DOCTYPE HTML>
<html>
	<head>
		<title>{title}</title>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
		<link rel="stylesheet" href="assets/css/main.css" />
		<noscript><link rel="stylesheet" href="assets/css/noscript.css" /></noscript>
	</head>
	<body class="is-preload">

		<!-- Wrapper -->
			<div id="wrapper">

				<!-- Header -->
					<header id="header">
						<a href="index.html" class="logo">Massively</a>
					</header>

				<!-- Main -->
					<div id="main">

						<!-- Post -->
							<section class="post">
								<header class="major">
									<span class="date">{today}</span>
									<h1>{title}</h1>
									<p>{summary}</p>
								</header>
								{main_text}
							</section>

					</div>


				<!-- Copyright -->
					<div id="copyright">
						<ul><li>&copy; Untitled</li><li>Design: <a href="https://html5up.net">HTML5 UP</a></li></ul>
					</div>

			</div>

		<!-- Scripts -->
			<script src="assets/js/jquery.min.js"></script>
			<script src="assets/js/jquery.scrollex.min.js"></script>
			<script src="assets/js/jquery.scrolly.min.js"></script>
			<script src="assets/js/browser.min.js"></script>
			<script src="assets/js/breakpoints.min.js"></script>
			<script src="assets/js/util.js"></script>
			<script src="assets/js/main.js"></script>

	</body>
</html>"""

with open(f"coupang/{file_name}", "w", encoding="utf-8") as f: # coupang/oz.html
    f.write(f"{main}")
    
ftp_url = "lolll.dothome.co.kr/"
ftp_id = "lolll"
ftp_pw = "lll1503120!"

ftp = ftplib.FTP()
ftp.connect(ftp_url, 21)
ftp.login(ftp_id, ftp_pw)

ftp.cwd("./html")

my_file = open(f"coupang/{file_name}", "rb")

ftp.storlines(f"STOR {file_name}", my_file)
my_file.close
ftp.close()