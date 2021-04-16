import re
regax1 = re.compile(r'anh (.*?) dep')
s = 'anh chuot dep trai'
kq = regax1.search(s)
print(kq.group(1))

regax2 = re.compile(r'kim (.*?) xinh')
s1 = 'kim anh xinh hoi khung , kim chi xinh hoi dien'
a = regax2.findall(s1)
print(a)
