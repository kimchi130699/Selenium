import bs4
import io 
import requests 

response = requests.get('https://fandy.vn/nike-ra-mat-giay-moi-dan-tinh-che-vua-xau-vua-dat/')
html_doc=response.text
file = io.open('code.html',mode='w',encoding ='utf8')
file.write(html_doc)

s = bs4.BeautifulSoup(html_doc , 'html.parser')
eles = s.select('title')

for ele in eles:
    print(ele.get_text())