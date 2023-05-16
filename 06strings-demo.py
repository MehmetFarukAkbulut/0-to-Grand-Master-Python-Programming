website= "https://www.linkedin.com/in/mehmet-faruk-akbulut-692340236/"
title= "Mehmet Faruk Akbulut Software Engineer"

# title karakter sayısı
result=len(title)
print(result)
# website içinden www karakterlerini al
w3=website[8:11]
print(w3)
# website içinden com 
wc=website[-38:-35]
wc=website[21:24]
print(wc)
# title içinden ilk 15 ve son 15 karakterlerini alın
print(title[0:15])
print(title[-15:])
# title karakterlerini tersten yazdırın
print(title[::-1])
# s= '12345' *5
# print(s[::5])
name,surname,age,job="Faruk","Akbulut",23,"Bilgisayar Mühendisi"
greeting=f"Benim adım {name} {surname}, Yaşım {age} ve mesleğim {job}."
print(greeting)
hw="Hello world"
hw=hw[0:6]+'W'+ hw[7:]
hw.replace('w','W')
print(hw)

a="abc"
print(a*3)
