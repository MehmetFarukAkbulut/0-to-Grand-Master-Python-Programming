# name = "Faruk Akbulut"
# for letter in name:
#     if letter== 'a':
#         break
#     print(letter)
# name = "Faruk Akbulut"
# for letter in name:
#     if letter== 'a':
#         continue
#     print(letter)
# x=0
# while x<5:
    
#     if x==2:
#         x+=1 
#         continue    
#     print(x)
#     x+=1
#  1den 100 e kadar tek sayıların toplamı
x=1
toplam=0
while x<100:
    if x%2==0: 
        x+=1
        continue 
    toplam+=x
    x+=1
print(f'toplam: {toplam}')