from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys 

#khai bao bien browser
browser = webdriver.Chrome(executable_path='chromedriver.exe')
#mo 1 trang web
browser.get('http://facebook.com')
#dien thong tin vao form dang nhap
username = browser.find_element_by_id('email')
username.send_keys('kimchi')
password = browser.find_element_by_id('pass')
password.send_keys('123')

#submit
password.send_keys(Keys.ENTER)
#dung chuong trinh sau 5s
sleep(5)

#dong trinh duyet
browser.close()
