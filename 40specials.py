# mylist=[1,2,3]
# myString="my string"


# print(len(mylist))
# print(len(myString))
# print(type(mylist))
# print(type(myString))

class Movie():
    def __init__(self,title,director,duration):
        self.title=title
        self.director=director
        self.duration=duration
        print("movie objesi oluşturuldu.")
m=Movie("film adı","yönetmen adı", "filmin süresi")

print(type(m))
print(len(m))


