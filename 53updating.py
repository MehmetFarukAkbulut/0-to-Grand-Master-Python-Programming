# with open("50newfile.txt","r+", encoding="utf-8") as file:# "r+" : hem okuma hem yazma
#     print(file.read())
    
# with open("50newfile.txt","r+", encoding="utf-8") as file:
#     file.seek(20)
#     file.write("deneme")
        
# with open("50newfile.txt","r+", encoding="utf-8") as file:
#     print(file.read())

##*******Sayfa sonunda güncelleme*****
    
# with open("50newfile.txt","a",encoding="utf-8")as file:
    # file.write("\nAdresim: Türkiye/İstanbul")
    
    
    
##********Sayfa başında güncelleme**********
 
# with open("50newfile.txt","r+", encoding="utf-8") as file:
#     content=file.read()
#     content="LinkedIn adresim: https://www.linkedin.com/in/mehmet-faruk-akbulut-692340236/\n"+content
#     file.seek(0)
#     file.write(content)

# with open("50newfile.txt","r", encoding="utf-8") as file:
#     print(file.read())
    
    
##********Sayfa ortasında güncelleme**********
    
with open("50newfile.txt","r+", encoding="utf-8") as file:
    liste=file.readlines()
    liste.insert(1,"GitHub Adresim: https://github.com/MehmetFarukAkbulut\n")
    file.seek(0)
    # for i in liste:
    #     file.write(i)
    file.writelines(liste)
    
    
with open("50newfile.txt","r", encoding="utf-8") as file:
    print(file.read())