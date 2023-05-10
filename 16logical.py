
x=5
hak=5
devam='e'
result=5<x<10

# and
result= x>5 and x<10
result= hak>0 and devam=='e'

# or
result= x>0 or x%2==0
result= x>0 and x%2==0

# not

result= not(x>0)

# x 5-10 arasında olan bir çift sayı mı
# x+=1
result= 10>x>5 and x%2==0
print(result)