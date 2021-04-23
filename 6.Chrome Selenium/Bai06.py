from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec 
# import bs4
# import io 
# import requests 

# response = requests.get('https://www.google.com/')
# html_doc=response.text
# file = io.open('code.html',mode='w',encoding ='utf8')
# file.write(html_doc)


chrome_options = webdriver.ChromeOptions()
prefs = {
    'profile.managed_default_content_settings.images':2
}
chrome_options.add_experimental_option('prefs',prefs)
driver = webdriver.Chrome('./chromedriver',options = chrome_options)

driver.get('http://nghiahsgs.com')

click
# cach 1 : thuc thi js
js_c = "document.querySelector('.read-more').click()"
driver.execute_script(js_c)
# cach 2 : tim phan tu bang driver
driver.find_element_by_css_selector('.read-more').click()
nhiu truong hop thi dung driver.find_elements_by_css_selector
list_eles = driver.find_elements_by_css_selector('.read-more')
list_eles[0].click()

#c1

driver.get('http://google.com')
js_zzz='document.querySelector(\'input[name="q"]\').value=\'cat\''
driver.execute_script(js_zzz)
#c2
input_search=driver.find_element_by_css_selector('input[name="q"')
input_search.send_keys('ahihi')
input_search.send_keys('haha')

driver.get(url)  # http://taoanhonline.com/wp-admin/post-new.php
title_input = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#title")));
time.sleep(0.5)