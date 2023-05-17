# Dosya açmak ve oluşturmak için open() fonksiyonu kullanılır.
# Kullanımı: open(dosya adi,dosya erişme modu)
# dosya erişme modu -> dosyayı hangi amaçla açtığımızı belirtir.

# "w": (Write) yazma modu. 
#       **Dosyayı konumda oluşturur.
#       **Dosya içeriğini siler ve yeniden ekleme yapar


# file=open("50newfile.txt","w")
# file= open("C:\Users\Mr. AKBULUT\Desktop\python_temelleri/50newfile.txt","w")
# file.close()
# file=open("50newfile.txt","w",encoding="utf-8")
# file.write("Adım: Mehmet Faruk Akbulut")
# file.close()
# "a": (Append) ekleme. Dosya konumda yoksa oluşturur.
# file= open("50newfile.txt","a",encoding="utf-8")
# file.write("\nBildiğim Diller: Python,C, HTML,CSS,JavaScript,React.js,React Native")
# print(file)
# file.close()
# "x": (Create) oluşturma. Dosya zaten varsa hata verir.
file= open("50newfile2.txt","x",encoding="utf-8")



# "r": (Read) okuma. varsayılan. dosya konumda yoksa hata verir.