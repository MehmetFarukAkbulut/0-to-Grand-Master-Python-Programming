import re

result= dir(re)


# re module

str="Python Kursu: Python Programlama Rehberiniz | 40 saat"


# re.findall()#bulma
# result=re.findall("Python",str) 
# result=len(result)

# re.split() #ayırma
# result=re.split(" ",str)
# result=re.split("r",str)

# re.sub() # değiştirme
# result=re.sub(" ", "-",str)
# result=re.sub("\s", "-",str)

# re.search()#arama

# result=re.search("Python",str) #<re.Match object; span=(0, 6), match='Python'> --bunu döndürdü

# result=result.span()#(0, 6) --Match objesi üzerinden span aldık
# result=result.start()# 0 --Match objesi üzerinden başlangıcını aldık
# result=result.end()# 6 --Match objesi üzerinden bitişi aldık
# result=result.group()#Python --Match objesi üzerinden aradığımız ifadeyi aldık
# result=result.string#Python Kursu: Python Programlama Rehberiniz | 40 saat --Match objesi üzerinden içinde aradığımız stringi aldık



#regular expression

'''
[] - Köşeli parantezler arasına yazılan bütün karakterler aranır.

    [abc] =>     a      :.1 match
                ac      : 2 match
                Python  : No matches
    
    [a-e] => [abcde]
    [1-5] => [12345]
    [0-39] => [01239]
    
    [^abc]=> abc dışındaki karakterler.
    [^0-9]=> rakam olmayan karakterler.

'''
result=re.findall("[abc]",str)
result=re.findall("[sat]",str)
result=re.findall("[a-e]",str)
result=re.findall("[a-z]",str)
result=re.findall("[0-5]",str)
result=re.findall("[^abc]",str)
result=re.findall("[^0-9]",str)

'''
    . - Her hangi bir tek karakteri belirtir.
    
        .. => a      : No match
              ab     : 1 match    
              abc    : 1 match    
              abcd   : 2 match    
'''
result=re.findall("...",str)
result=re.findall("Py..on",str)

'''
    ^ - Belirtilen string karakterle başlıyor mu?
    
    ^a =>   a  :   1 match
            abc:   1 match
            bac:  No match

'''
result=re.findall("^P",str )

'''
    $ - Belirtilen string karakterle bitiyor mu?
    a$ =>   a           : 1 match
            lambda      : 1 match
            Python      : No match

'''

result=re.findall("t$",str )
result=re.findall("saat$",str )
result=re.findall("saatt$",str )


'''
    * - Bir karakterin sıfır ya da daha fazla sayıda olmasını kontrol eder.
    
    ma*n =>     mn          : 1 match
                man         : 1 match
                maaan       : 1 match
                main        : No match( a' nın arkasına n gelmiyor.)

'''

result=re.findall("sa*t",str )


'''
    + - Bir karakterin bir ya da daha fazla sayıda olmasını kontrol eder.
    
    ma*n =>     mn          : No match
                man         : 1 match
                maaan       : 1 match
                main        : No match( a' nın arkasına n gelmiyor.)

'''

result=re.findall("sa+t",str )

'''
    ? - Bir karakterin sıfır ya da bir kez olmasını kontrol eder.
    
    ma?n =>     mn          : 1 match
                man         : 1 match
                maaan       : No match
                main        : No match

'''

result=re.findall("sa?t",str )
result=re.findall("saa?t",str )

'''
    {} - Karakter sayısını kontrol eder.
    
    al{2} =>  a karkaterinin arkasına l karakteri 2 kez tekrarlamalı.
    al{2,3} =>  a karkaterinin arkasına l karakteri en az 2 en fazla 3 kez tekrarlamalı.
    [0-9]{2,4} =>  en az 2 en çok 4 basamaklı sayılar.
                
'''

result=re.findall("a{2}",str )
result=re.findall("a{2,3}",str )
result=re.findall("[0-9]{2}",str )

'''
    |  - alternatif seçeneklerden birinin gerçekleşmesi gerekir.
    
    a|b =>   a ya da b
            cde             : No match
            ade             : 1 match
            acdbea          : 3 match
            
'''

result=re.findall("Py|Pr",str)

'''
    ()  - gruplamak için kullanılır.
    
        (a|b|c)xz => a,b,c  karakterlerinin arkasına xz gelmelidir.
            
'''

'''
    \ - Özel karakterleri aramamızı sağlar.
        \$a=> $ karakterinin arkasına a karkterini arar. Yani $ regular exp. engine tarafından yorumlanmaz

    \A - ÖBelirtilen karakter stringin başında mı?
        \Athe=> the stringin başında mı?
        
        result=re.findall("\APython",str)
        result=re.findall("saat\Z",str)
    
    \Z - Belirtilen karakter stringin sonunda mı?
        the\Z=> the stringin sonunda mı?
        
    \b - Belirtilen karakter kelimenin başında ya da sonunda mı?
        \bthe=> the kelimeni başında mı?
        the\b=> the kelimeni sonunda mı?
        
    \B - Belirtilen karakter kelimenin başında ya da sonunda değil mı?
        \Bthe=> the kelimeni başında mı?
        the\B=> the kelimeni sonunda mı?

    \d - [0-9] ile aynı anlam 
        \d=> 12abc34
        
    \D - [^0-9] ile aynı anlam
        \D=> 1ab44_50

    \s-  Boşluk karakterlerini arar.
    \S-  Boşluk karakterleri dışındakiler.
    \w-  Alfabetik karakterler, rakamlar ve alt çizgi karakteri.
    \W-  \w nin tam tersi



'''

print(result)
