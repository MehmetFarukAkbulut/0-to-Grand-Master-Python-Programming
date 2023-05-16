# "Bmw,Mercedes,Opel,Mazda" elemanlarına sahip bir liste oluştur
# print("Bmw,Mercedes,Opel,Mazda".split(','))
cars=['Bmw', 'Mercedes', 'Opel', 'Mazda']
# Liste kaç elemanlı?ilk ve son elemanı?
print(len(cars))
print(cars[0])
print(cars[-1])
print(cars[len(cars)-1])
# Mazda değerini Toyota ile değiştirin
cars[-1]= 'Toyota'
print(cars)
# Mercedes listenin bir elemanı mıdır?
print('Mercedes'in cars)
print('Meireles'in cars)
# Listenin -2 indeksindeki değer
print(cars[-2])
# ilk 3 elemanını alın
print(cars[0:3])
print(cars[:3])
print(cars[-2:])
cars[-1]= 'Mazda'
print(cars)
# son iki elemanı yerine "Toyota" ve "Renault" ekleyin
cars[-2:]=['Toyota','Renault']
print(cars)
# üzerine "Audi" ve "Nissan" ekleyin
print(cars + ['Audi','Nissan'])
# son elemanını silin
del cars[-1]
print(cars)

# Liste elemanlarını tersten yazdır
print(cars[::-1])
# liste oluştur: 
    # studentA: Faruk Akbulut 2000,(100,99,90)
    # studentB: Rümeysa Akbulut 19998,(90,89,80)
    # studentC: Fatih Akbulut 1991,(80,79,70)
    
studentA=['Faruk', 'Akbulut', 2000,[100,99,90]]     
studentB=['Rümeysa','Akbulut', 1998,[90,89,80]]     
studentC=['Fatih','Akbulut', 1991,[80,79,70]]    
students= [studentA,studentB,studentC] 
print(studentA)
print(studentB)
print(studentC)
print(students)
print(f"{studentA[0]} {studentA[1]}, {2023-studentA[2]} yaşında ve not ortalaması {(studentA[3][0]+studentA[3][1]+studentA[3][2])//3}")
print(f"{studentB[0]} {studentB[1]}, {2023-studentB[2]} yaşında ve not ortalaması {(studentB[3][0]+studentB[3][1]+studentB[3][2])//3}")
print(f"{studentC[0]} {studentC[1]}, {2023-studentC[2]} yaşında ve not ortalaması {(studentC[3][0]+studentC[3][1]+studentC[3][2])//3}")

