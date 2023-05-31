# try:    
#     file= open("50newfile.txt")#varsayılan r
#     file= open("50newfile.txt","r")
#     print(file)
# except FileNotFoundError:
#     print("Dosya okuma hatası")
# finally:
#     print("Dosya kapandı")
#     file.close()

file=open("50newfile.txt","r", encoding="utf-8")

# #for döngüsü

# for i in file:
#     print(i,end="")

# #***************** read() fonksiyonu

# content1=file.read()

# print("İçerik 1:")
# print(content1)

# file=open("50newfile.txt","r", encoding="utf-8")# dosyayı tekrar okumak için tekrar read ile açmamız lazım

# content2=file.read()
# print("İçerik 2:")
# print(content2)


# content=file.read(6)
# print(content)

# content=file.read(7)
# print(content)

# content=file.read(6)
# print(content)

# #***************** readline() fonksiyonu

# print(file.readline(),end="")
# print(file.readline(),end="")
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())

# #***************** readlines() fonksiyonu

# liste=file.readlines()

# print(liste)
# print(liste[0])
# print(liste[1])


file.close()

