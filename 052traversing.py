# file=open("50newfile.txt","r", encoding="utf-8")

# content=file.read()
# print(content)

# file.close()

with open("50newfile.txt","r", encoding="utf-8") as file:
    content=file.read()
    print(content)
    print(file.tell())
    
    file.seek(7)
    print(file.tell())
    content2=file.read()
    print(content2)
    



