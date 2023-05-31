import os
import datetime

result=dir(os)
result=os.name

# dizin değiştirme
# os.chdir('C:\\Users\\Mr. AKBULUT\\Desktop\\')
# os.chdir('../..')


# klasör oluşturma
# os.mkdir("newdirectory")
# os.makedirs("C:\\Users\\Mr. AKBULUT\\Desktop\\newdirectory/yeniklasör")
# os.rename("newdirectory",  "yeniklasör")
# os.rmdir("newdirectory")
# os.removedirs("yeniklasör/yeniklasör")



# listeleme
# result=os.listdir()
# result=os.listdir("C:\\Users")

# filtreleme
# for dosya in os.listdir():
#     if dosya.endswith(".py"):
#         print(dosya)


# etkin dizin öğrenme
# result=os.getcwd()


# result=os.stat("61date.py")
# result=result.st_size/1024
# result=datetime.datetime.fromtimestamp(result.st_ctime)   #oluşturulma tarihi
# result=datetime.datetime.fromtimestamp(result.st_atime)   #son erişilme tarihi
# result=datetime.datetime.fromtimestamp(result.st_mtime) #değiştirilme tarihi

# os.system("notepad.exe")

# path

result=os.path.abspath("61date.py") # adresini verir
result=os.path.dirname("C:/Users/Mr. AKBULUT/Desktop/python_temelleri/61date.py")#bulunduğu klasörün adresini verir
result=os.path.dirname(os.path.abspath("61date.py"))# dosyanın adresini alarak bulunduğu klasörün adresini verir
result=os.path.exists("61date.py")#bu yolda böyle bir dosya veya klasör var mı kontrol eder
result=os.path.exists("C:/Users/Mr. AKBULUT/Desktop")#bu yolda böyle bir dosya veya klasör var mı kontrol eder
result=os.path.isdir("C:/Users/Mr. AKBULUT/Desktop")#bu yolda böyle bir klasör var mı kontrol eder
result=os.path.isdir("C:/Users/Mr. AKBULUT/Desktop/61date.py")#bu yolda böyle bir klasör var mı kontrol eder
result=os.path.isfile("C:/Users/Mr. AKBULUT/Desktop")#bu yolda böyle bir dosya var mı kontrol eder
result=os.path.isfile("C:/Users/Mr. AKBULUT/Desktop/61date.py")#bu yolda böyle bir dosya var mı kontrol eder
result=os.path.join("C:\\","deneme","deneme1")#verilen pathleri klasörleri birleştirir oluşturmaz
result=os.path.split("C:\\deneme")#adresteki klasörleri ayırır
result=os.path.splitext("61date.py")#ismi ve uzantıyı ayırır
# result=result[0]#splitext ten sonra çalıştırılırsa ismi alır
# result=result[1]#splitext ten sonra çalıştırılırsa uzantıyı alır

print(result)