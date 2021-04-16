import openpyxl

#truy van cot
def function(filename, column):
    a = openpyxl.load_workbook(filename)
    sheet1 = a['Sheet1']
    a.close()
    return sheet1[column].value
filename = 'danhsach.xlsx'
column = 'B4'
x = function(filename,column)
print(x)

# thay doi gia tri value
def update(filename,column,value):
    b = openpyxl.load_workbook(filename)
    S1 = b['Sheet1']
    S1[column].value = value
    b.close()
    b.save(filename)
file_name = 'danhsach.xlsx'
column_ = 'C4'
value = 'not live'
c = update(file_name,column_,value)
print(c)

#lay gia tri cua 2 cot A va B
col_name = 'A'
col_word = 'B'
filename = 'danhsach.xlsx'

for i in range(3,12):
    username = '%s%s'%(col_name,i)
    password = '%s%s'%(col_word,i)

    name = function(filename,username)
    key = function(filename,password)

    print('user name : ', name)
    print('pass word:',key)

    input('pause')