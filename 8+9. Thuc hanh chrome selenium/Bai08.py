from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec 


import time

def initDriver(filePath):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("user-data-dir="+filePath)
    #config ko load anh
    # prefs ={
    # "profile.managed_default_content_setting.images":2
    # }
    # chrome_options.add_experimental_option("prefs",prefs)
    driver = webdriver.Chrome(executable_path=(
        r"D:\ThucTap\BaiTap\Selenium\8+9. Thuc hanh chrome selenium\chromedriver.exe"), options=chrome_options)
    return driver 

def ham_surf_face(filePath):
    driver = initDriver(filePath)
    driver.get('https://www.facebook.com/')
    print("CHIDEBU: driver")
    WebDriverWait(driver,10).until(ec.visibility_of_element_located((By.CSS_SELECTOR,"stories_tray")))
    print("CHIDEBU: WebDriverWait")
    time.sleep(2)
    count_eles_btn_like =0

    while(True):
        #scroll down
        driver.execute_script("window.scrollBy(0,0.7*window.innerHeight")
        time.sleep(2)

        eles_btn_like =driver.find_elements_by_css_selector('div[data-testid="UFI2ReactionLink/actionLink"]a') #selector cua nut like
        count_eles_btn_like = len(eles_btn_like)
        print(count_eles_btn_like)
filePath ='chrome'
ham_surf_face(filePath)

def pool_hander():
    p = pool(2)
    kq = map_async(ham_surf_face,('chrome','chrome2'))
    print('main')
    print(kq.get())
    p.close()
    p.join()
    print('Task end')
if __name__ == '__main__':
    pool_hander()