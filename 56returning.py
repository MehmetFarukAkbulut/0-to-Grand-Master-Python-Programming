# def usalma(number):
#     # two=usalma(2)
#     # three=usalma(3)
    
#     def inner(power):
#         return number**power 
#     return inner

# two=usalma(2)
# three=usalma(3)
# print(two(3))
# print(three(4))

# def yetki_sorgula(page):
#     def inner(role):
#         if role=="Admin":
#             return "{0} rolü {1} sayfasına ulaşabilir.".format(role,page)
#         else:
#             return "{0} rolü {1} sayfasına ulaşamaz.".format(role,page)
#     return  inner
# user1=yetki_sorgula("Product Edit")
# print(user1("Admin"))
# print(user1("User"))

def islem(islem_adi):
    def toplam(*args):
        toplam=0
        for i in args:
            toplam+=i
        return toplam
    
    def carpma(*args):
        carpim=1
        for i in args:
            carpim*=i
        return carpim    
    def cikarma(x,y):
        return x-y
    def bolme(x,y):
        return x/y
    if islem_adi=="toplama":
        return toplam
    elif islem_adi=="çarpma":
        return carpma
    elif islem_adi=="çıkarma":
        return cikarma
    elif islem_adi=="bölme":
        return bolme
    else:
        print("hatalı giriş yaptınız.")
        
toplama=islem("toplama")
print(toplama(1,3,5,6,7,5,1,2,2))
carpma=islem("çarpma")
print(carpma(1,2,4,5,6,8))
cikarma=islem("çıkarma")
print(cikarma(21,12))
bolme=islem("bölme")
print(bolme(18,2))

