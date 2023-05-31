website="https://github.com/MehmetFarukAkbulut"
job= "Software Engineer"

g=" Hello World "

print(g.strip())
print(g.lstrip())
print(g.rstrip())
print(website.lstrip('/:pths'))
print(website.replace('https://github.com/',''))
print(job.lower())
print(job.upper())
print(job.title())
print(website.count('e'))
print(website.count('http'))
print(website.count('http',0,10))
print(website.startswith('github'))
print(website.startswith('http'))
print(website.endswith('com'))
print(website.endswith('Akbulut'))
print(website.find('github'))
print(website.find('com'))
print(website.index('com'))
print(website.rindex('com'))
# print(website.rindex('comm'))#exception
print(job.find('Soft'))
print(job.rfind('e'))
print(job.isalpha())
print(job.replace(' ','').isalpha())
print(job.isdigit())
print('123'.isdigit())
print('Contents'.center(50))
print('Contents'.center(50,'*'))
print('Contents'.ljust(50,'*'))
print('Contents'.rjust(50,'*'))
print(job.replace(' ','-'))
print(job.replace(' ',''))
print('Hello World'.replace('World','There'))
print(job.split(' '))
print(job.split(' ')[1])


