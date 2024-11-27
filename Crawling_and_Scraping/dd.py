from flask import Flask
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

#클래스, 아이디를 CSS_SELECTOR를 이용하기 위한 패키지
from selenium.webdriver.common.by import By
#키보드의 입력 형태를 코드로 작성하기 위한 패키지
from selenium.webdriver.common.keys import Keys
import time
import pymysql

app = Flask(__name__)

connection = pymysql.connect(
     host = '127.0.0.1',
     user = 'root',
     password= '1234',
     db = 'kream',
     charset = 'utf8mb4'
)

@app.route('/')
def index():
    kream_scraping()
    return "스크래핑 성공"

if __name__ == '__main__': #파일 실행하면 __name__ = __main__ 인터프리터가 자동으로 할당해주는 이름입니다.
    app.debug = True
    app.run

#---------------------------------------------------------------------------------------
def kream_scraping():    
    header_user = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"

    options_ = Options()
    options_.add_argument(f"User_Agent={header_user}")
    options_.add_experimental_option("detach", True)
    options_.add_experimental_option("excludeSwitches", ["enable-logging"])

    driver = webdriver.Chrome(options=options_)

    url = "https://kream.co.kr"
    driver.get(url)
    time.sleep(2)

    driver.find_element(By.CSS_SELECTOR, ".btn_search.header-search-button.search-button-margin").click() #driver => chrome browser
    time.sleep(1.5)

    # keyword = input("검색을 원하는 키워드를 입력해주세요")
    driver.find_element(By.CSS_SELECTOR, ".input_search.show_placeholder_on_focus").send_keys("슈프림")
    driver.find_element(By.CSS_SELECTOR, ".input_search.show_placeholder_on_focus").send_keys(Keys.ENTER)

    for i in range(20):
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
        time.sleep(0.5)

    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    items = soup.select(".product_card") #리스트 가능하는 데이터타입


    product_list = []

    for item in items:
        #제품명에 "후드"가 들어간것만 추출 / 1.제품명만 추출합니다. 2.제품명을 if문을 이용해서 분류하는데 3.문자열 안에 "후드"가 있는지를 찾는 조건을 만들어야한다.
        product_name = item.select_one(".translated_name").text
        if "후드" in product_name:
            category = "상의"
            product_brand = item.select_one(".product_info_brand.brand").text
            product_price = item.select_one(".amount").text
            
            product = [category, product_brand, product_name, product_price]
            product_list.append(product) #[[상의, 슈프림, 멜란지 후드, 50000], [상의, 슈프림, 검은색 오버 후드, 100000], ]

    driver.quit()
    for i in product_list:#[[상의, 슈프림, 멜란지 후드, 50000], [상의, 슈프림, 검은색 오버 후드, 100000], ]
     #i = [상의, 슈프림, 멜란지 후드, 50000] -> i[0]
        execute_query(connection, "INSERT INTO kream (category, brand, product_name, price) VALUES (%s, %s, %s, %s)",(i[0], i[1], i[2], i[3]))


def execute_query(connection, query, args=None): #들어갈 데이터 ("홍길동", 25, "제주도")
     with connection.cursor() as cursor:
          cursor.execute(query, args or ()) #쿼리문을 담아서 데이터베이스 보냄 / select 검색 결과가 나올것이고 / insert 데이터베이스 데이터가 저장되어있음
          if query.strip().upper().startswith('SELECT'): #SELECT * from kream or insert
               return cursor.fetchall()
          else:
               connection.commit()#데이터베이스에 insert문을 사용했다면 데이터베이스에 데이터를 영구적으로 저장해줘