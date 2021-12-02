import mod_myPyAutoGui as PAG
import pyautogui as pag
import time as t 

#
PAG.win()
PAG.paste_in('cmd')
PAG.enter()
t.sleep(1.5)

# cmd로 크롬브라우저 디버깅모드 실행
PAG.paste_in('cd C:\Program Files (x86)\Google\Chrome\Application')
PAG.enter()
t.sleep(0.3)
PAG.paste_in('chrome.exe --remote-debugging-port=9222 --user-data-dir="C:/ChromeTEMP"') # 포트 9222로 열었기에 셀레니움에서 접근가능
PAG.enter()
t.sleep(2)

# 네이버
PAG.paste_in('www.naver.com')
PAG.enter()

# 로그인 확인
rur = 0
while rur != 'y' :
    rur = input("Do you logged-in? (y/n) : ")

# 종료
PAG.quit()

    




