# def cube():
#     result=[]
    
#     for i in range(5):
#         result.append(i**3)
#     return result

# def cube():
#     for i in range(5):
#         yield i**3

# for i in cube():
#     print(i)

generator=(i**3 for i in range(5))
print(generator)
for i in generator:
    print(i)

