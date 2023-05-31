# error handling=> hata yönetimi


# try:
#     x=int(input("x: "))
#     y=int(input("y: "))
#     print(x/y)
    
# except (ZeroDivisionError,ValueError) as e:
#     print("Yanlış bilgi girdiniz.")
#     print(e)
    
# try:
#     x=int(input("x: "))
#     y=int(input("y: "))
#     print(x/y)
    
# except:
#     print("Yanlış bilgi girdiniz.")
while True:
    try:
        x=int(input("x: "))
        y=int(input("y: "))
        print(x/y)

    except Exception as ex:
        print("Yanlış bilgi girdiniz.",ex)
    else:
        # print("her şey yolunda")
        break
    finally:
        print("Try except sonlandı.")