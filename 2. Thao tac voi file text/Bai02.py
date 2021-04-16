import io
import os
from shutil import copyfile
#get duong dan hien tai
print(os.getcwd())

# chuyen thu muc
os.chdir(r'D:\ThucTap\BaiTap\Selenium\2. Thao tac voi file text')

# mo file
f = open('kimchi1.txt','w')
f.close()

# doi ten file
os.rename('kimchi1.txt','kimchi.txt')

# xoa file
os.remove('kimchi.txt') 

# copy file
copyfile('kimchi.txt','kimchicopy.txt')

# viet file ko co utf8 (tieng anh)
filename ='chi.txt'
f = open(filename,'a')
content = 'ahihi ahihi tui la chi ne'
f.write(content +'\n')
f.close()

# viet file co utf8 (tiếng việt)
def tiengviet(filename1, content1):
    n = io.open(filename1,mode ='a',encoding='utf-8')
    n.write(content1 +'\n')
    n.close()
filename1 = 'filetiengviet.txt'
content1 = 'Tớ tên là bùi thị kim chi nè !'
tiengviet(filename1,content1)

# doc file co tieng viet
def tiengviet(filename):
    f = io.open(filename,mode='r',encoding='utf-8')
    line = f.readlines()
    for i in line:
        print(i)
filename='filetiengviet.txt'
tiengviet(filename)
