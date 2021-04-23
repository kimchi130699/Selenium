from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec 

import time
import urllib
import requests
import shutil

def initDriver(filePath):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("user-data-dir="+filePath)
    #config ko load anh
    prefs ={
    "profile.managed_default_content_setting.images":2
    }
    chrome_options.add_experimental_option("prefs",prefs)
    driver = webdriver.Chrome(executable_path=(
        r"D:\ThucTap\BaiTap\Selenium\8+9. Thuc hanh chrome selenium\chromedriver.exe"), options=chrome_options)
    return driver 
def ham_download_image_gg(filePath,folder_save,keyword,number_scroll):
    nameFile = "-".join(keyword.split(" "))
    driver =initDriver(filePath)
    driver.get('https://www.google.com/')
    driver.get('https://www.google.com/search?tbm=isch&q='+keyword.replace(" ","+"))
    time.sleep(10)

    for i in range(number_scroll):
        driver.execute_script("window.scrollBy(0,0.7*window.innerHeight);")
        time.sleep(10)

    #lay link truc tiep cua anh
    list_elements =driver.find_elements_by_css_selector('a[jsname="hSRGPd"]')
    list_href = []
    for image in list_elements[3:]:
        href = image.get_attribute('href')
        list_href.append(href)
    print('len(list_href)', len(list_href))
    list_src=[]

    #tach url chuoi va download
    pos = 0 
    for href in list_href:
        print(pos,href)
        try:
            href = urllib.parse_qs(href)
            href  = href['https://www.google.com/imgres?imgurl'][0]
            print('href',href)
            #input(conan)
            downloadImg(href,nameFile+'-'+str(pos),folder_save)
        except:
            print('error at %s'%pos)
        pos +=1

def downloadImg(url,nameFile,result_dir):
    try:
        response = requests.get(url,stream = True,timeout =10)
        with open(r'%s\%s.jpg'%(result_dir,nameFile),'wb') as out_file:
            shutil.copyfileobj(response.raw,out_file)
        del response
    except:
        print("error downloadImg")
filePath = 'chrome2'
folder_save = 'image'
keyword = 'conan'
number_scroll = 2
ham_download_image_gg(filePath,folder_save,keyword,number_scroll)
