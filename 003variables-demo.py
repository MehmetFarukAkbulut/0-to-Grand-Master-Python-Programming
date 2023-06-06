import datetime
customerName="Faruk"
customerSurname="Akbulut"
customerNameSurname=customerName+' '+customerSurname
customerGender= True #Erkek
customerId= "12345678901"
customerBirthdate= 2000
customerAddress="Basaksehir/Istanbul"
customerAge= datetime.datetime.now().year-customerBirthdate
print(customerName)
print(customerSurname)
print(customerNameSurname)
print(customerGender)
print(customerId)
print(customerBirthdate)
print(customerAddress)
print(customerAge)

order1=110
order2=110.5
order3=356.95
total= order1+ order2+ order3
print("Total: ",total," Dollars")
