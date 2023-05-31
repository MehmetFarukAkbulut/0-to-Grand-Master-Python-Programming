from datetime import datetime
from datetime import timedelta
# from datetime import date
# from datetime import time
# import datetime

simdi=datetime.now() 
simdi=datetime.today() 
y=simdi.year
m=simdi.month
d=simdi.day
h=simdi.hour
mi=simdi.minute
s=simdi.second

result=datetime.ctime(simdi)
result=datetime.strftime(simdi,'%Y')
result=datetime.strftime(simdi,'%X')
result=datetime.strftime(simdi,'%d')
result=datetime.strftime(simdi,'%A')
result=datetime.strftime(simdi,'%B')
result=datetime.strftime(simdi,'%Y %B %A')


t="23 October 2023 hour 10:12:30"
dt=datetime.strptime(t,"%d %B %Y hour %H:%M:%S")
result=dt.year

print(dt)

birthday=datetime(2000,10,23,10,0,0)
result=datetime.timestamp(birthday)#saniye
result=datetime.fromtimestamp(result)#saniye to datetime
result=datetime.fromtimestamp(0)

result=simdi-birthday #timedelta
# result=result.days
# result=result.seconds
# result=result.microseconds

print(simdi)
# result=simdi+timedelta(days=10)
# result=simdi+timedelta(days=730,minutes=10)


result=simdi-timedelta(days=10)
print(birthday)
# gun,ay,yil=t.split()
# print(gun)
# print(ay)
# print(yil)



print(f'{d}/{m}/{y}\n{h}:{mi}:{s}')
print(result)











