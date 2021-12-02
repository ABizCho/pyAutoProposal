import time as t

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import mod_myPyAutoGui as PAG




#사전 warning제거 설정#
def set_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver
######################



########## Selenium 으로 chrome 브라우저 가동 ###########
### 브라우저 열기 옵션 설정
options = webdriver.ChromeOptions()

options.add_argument('window-size=1920,1080')#윈도우사이즈
options.add_argument('headless')#헤들리스
options.add_argument('start-maximized')#창 최대화

### 브라우저 드라이버 최종 할당 및 시작
driver = webdriver.Chrome('C:/Users/JSW/Desktop/GIT/MyDevSources/selenium_chromeDriver_9604/chromedriver.exe')

# 웹페이지 이동
naverUrl = "https://www.naver.com"
driver.get(naverUrl)
driver.current_url
#########################################################




