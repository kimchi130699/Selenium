from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys 

browser = webdriver.Chrome(executable_path='chromedriver.exe')
#mo 1 trang web
browser.get('https://www.facebook.com/groups/208293260246603')

while(True):
    #scroll down
    driver.execute_script("window.scrollBy(0,0.7*window.innerHeight")
    time.sleep(3)

# sleep(5)
# link = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div/div/div/div/div[1]/div[2]/div[1]/div/div[3]/div/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div[1]/div/div[1]/div/div[2]/div[1]/div/span')
# link.click()

# browser.close()