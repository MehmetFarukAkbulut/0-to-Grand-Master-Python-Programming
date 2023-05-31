numbers= [1,10,5,16,4,9,10]
letters =['a','g','s','b','y','a','s']


print(min(numbers))
print(max(numbers))
print(min(letters))
print(max(letters))
print(numbers[3:6])
print(numbers[:3])
print(numbers[4:])

numbers[4]= 40
numbers.append(49)
numbers.append(59)
numbers.insert(3,78)
numbers.insert(-1,52)
# numbers.pop()
# numbers.pop(0)
# numbers.pop(-1)
# numbers.remove(59)

numbers.sort()
numbers.reverse()
letters.sort()
letters.reverse()
print(numbers)
print(len(numbers))
print(len(letters))
print(numbers.count(10))
print(letters.count('a'))
numbers.clear()
print(numbers)
