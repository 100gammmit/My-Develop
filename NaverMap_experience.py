from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re
import csv


driver = webdriver.Chrome("D:\chromedriver\chromedriver.exe")

driver.get("https://map.naver.com/v5/search/체험?c=14111267.1064309,4532969.7466661,14,0,0,0,dh") #네이버 신 지도 
'''
try:
   element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "input_search"))
   ) 
finally:
   pass
search = driver.find_element(By.CLASS_NAME, "input_search")
search.send_keys('홍대 맛집')
search.send_keys(Keys.ENTER)
'''


time.sleep(2)

'''


'''
zoom_in = driver.find_element(By.CSS_SELECTOR, "button.btn_zoom_in.ng-tns-c167-7")
for _ in range(1):
    zoom_in.click()
zoom_out = driver.find_element(By.CSS_SELECTOR, "button.btn_zoom_out.ng-tns-c167-7")
for _ in range(2):
    zoom_out.click()
time.sleep(1)
research_button = driver.find_element(By.CSS_SELECTOR, "button.btn_research.auto.ng-star-inserted")
research_button.click()
time.sleep(2)




 
frame = driver.find_element(By.CSS_SELECTOR, "iframe#searchIframe")

driver.switch_to.frame(frame)

scroll_div = driver.find_element(By.CSS_SELECTOR, "div#_pcmap_list_scroll_container._1Az1K")
#검색 결과로 나타나는 scroll-bar 포함한 div 잡고

file = open('stores.csv', mode='w', newline='')
writer = csv.writer(file)
writer.writerow(["가게명", "업종", "주소", "영업시간", "전화번호", "주차"])

driver.execute_script("arguments[0].scrollBy(0,3000)", scroll_div)
time.sleep(1)
driver.execute_script("arguments[0].scrollBy(0,3000);", scroll_div)
time.sleep(1)
driver.execute_script("arguments[0].scrollBy(0,3000);", scroll_div)
time.sleep(1)
driver.execute_script("arguments[0].scrollBy(0,3000);", scroll_div)
time.sleep(1)
driver.execute_script("arguments[0].scrollBy(0,3000);", scroll_div)
time.sleep(1)
#맨 아래까지 내려서 해당 페이지의 내용이 다 표시되게 함

# csv 파일 생성

final_result = []
# # 반복 시작
i = 2
while i<=7:
    stores = scroll_div.find_elements(By.CSS_SELECTOR, "li._22p-O._2NEjP")
    #모든 가게명 리스트로 저장
    
    #각 가게명별로 클릭하여 상세정보 추출을 위한 반복문
    for store in stores:
        name = store.find_element(By.CSS_SELECTOR, "span.place_bluelink._3Apve").text
        #가게명 저장
        click_name = store.find_element(By.CSS_SELECTOR, "span.place_bluelink._3Apve")
        click_name.click()
        #가게명 클릭하여 상세정보 표시
        
        driver.switch_to.default_content()
        time.sleep(2)
        frame_in = driver.find_element(By.XPATH, '/html/body/app/layout/div[3]/div[2]/shrinkable-layout/div/app-base/search-layout/div[2]/entry-layout/entry-place-bridge/div/nm-external-frame-bridge/nm-iframe/iframe')
        driver.switch_to.frame(frame_in)
        #상세정보가 표시되는 iframe으로 이동
        
        TypeOfBusiness = driver.find_element(By.CSS_SELECTOR, "span._3ocDE").text
            
        address = driver.find_element(By.CSS_SELECTOR, "span._2yqUQ").text
        #가게 주소 저장
        
        try:
            number = driver.find_element(By.CSS_SELECTOR, "span._3ZA0S").text
        except:
            number = ''
        #가게 번호 저장(없는 경우 예외처리)
        
        try:
            opcl_click = driver.find_element(By.CLASS_NAME, "_20Y9l")
            opcl_click.click()
            try:
               opcl = driver.find_element(By.CLASS_NAME, "_3uEtO").text
            except:
                opcl=''
        except:
            opcl=''
        #가게 영업시간 저장(없는 경우 예외처리)
        #영업시간의 경우 클릭시 가장 위에 표기되는 시간을 추출하였으므로 휴무인 요일에 실행 시 휴무라고 뜰 수 있음
        
        park='X'
        #주차가능 여부(기본값'X')
        parking = driver.find_elements(By.CLASS_NAME, "_1M_Iz")
        #'_1M_Iz'를 포함하는class가 다수이며, 그중 내부에 'place_blind'class의 text가 '편의'인 경우에 주차가능 여부를 확인할 수 있음
        #이 조건을 만족하는 class를 찾아서 그 클래스의 text가 주차를 포함한 경우 park값 변경 
        for p in parking:
            try:
                pk = p.find_element(By.CLASS_NAME, "place_blind").text
                if pk == '편의':
                    if '주차' in p.find_element(By.CLASS_NAME, "_1h3B_").text:
                        park='O'
                        break
                    else:
                        break
            except:
                continue
        
        
        store_info = {
            'placetitle':name,
            'typeOfbusiness':TypeOfBusiness,
            'address':address,
            'business_hour':opcl,
            'phone_num':number,
            'park':park
        }
        print(store_info)
        final_result.append(store_info)
        driver.switch_to.default_content()
        driver.switch_to.frame(frame)
        
    try:
        next_button = driver.find_element(By.LINK_TEXT, str(i))
        next_button.click()
        i = i+1
        time.sleep(3)
    except:
        break
    
for result in final_result: #크롤링한 가게 정보에 순차적으로 접근 & csv 파일 작성
    row = []
    row.append(result['placetitle'])
    row.append(result['typeOfbusiness'])
    row.append(result['address'])
    row.append(result['business_hour'])
    row.append(result['phone_num'])
    row.append(result['park'])
    writer.writerow(row)
