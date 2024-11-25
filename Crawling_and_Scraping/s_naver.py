from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

base_url = "https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query="
keyword = input("검색을 원하는 키워드를 입력해주세요 : ")
url = base_url + keyword

header_user = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"

options_ = Options()
options_.add_argument(f"User_Agent={header_user}")
options_.add_experimental_option("detach", True)
options_.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(options=options_)
driver.get(url)
time.sleep(2)

for i in range(5):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)") # 0px 부터 스크롤을 움직여 body 의 끝까지 움직이도록 만들어주는 코드
    time.sleep(1)

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

results = soup.select(".view_wrap")

for i in results:
    title = i.select_one(".title_link").text
    author = i.select_one(".name").text
    link = i.select_one(".title_link")["href"]
    if i.select_one(".dsc_link"):
        dsc = i.select_one(".dsc_link").text
    else:
        dsc = "내용없음"

    print(f"제목 : {title}")
    print(f"작성자 : {author}")
    print(f"링크 : {link}")
    print(f"요약 : {dsc}")
    print("-" * 70)

# driver.quit()