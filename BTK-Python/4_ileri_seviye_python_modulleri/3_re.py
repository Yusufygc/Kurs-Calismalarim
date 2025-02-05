import re

str ="Python Kursu: Python Programlama Rehberi | 40 saat"
result = re.findall("Python",str) # aranan kelimeyi bulur
# print(len(result))# ['Python', 'Python'] liste döndürdüğü için len ile uzunluğunu bulduk

result=re.split(" ",str) # boşluklara göre ayırır
# ['Python', 'Kursu:', 'Python', 'Programlama', 'Rehberi', '|', '40', 'saat']

result=re.sub(" ","-",str) # boşlukları - ile değiştirir boşluk yerin \s de kullanılabilir
# Python-Kursu:-Python-Programlama-Rehberi-|-40-saat

result=re.search("Python",str) # aranan kelimenin başlangıç ve bitiş indexini döndürür
# <re.Match object; span=(0, 6), match='Python'>
"""
result = result.span() # başlangıç ve bitiş indexini döndürür
# (0, 6)
result = result.start() # başlangıç indexini döndürür
# 0
result = result.end() # bitiş indexini döndürür
# 6

result = result.group() # aranan kelimeyi döndürür
# Python

result = result.string # kelimenin bulunduğu cümleyi döndürür
# Python Kursu: Python Programlama Rehberi | 40 saat
"""
##########################################################
"""
[] - Köşeli parantezler arasına yazılan bütün karakterler
aranır.

        [abc] => a : 1 match
                ac : 2 match
                Python : No matches

        [a-e] => [abcde]
        [1-5] => [12345]
        [0-39] => [01239]

        [^abc] => abc dışındaki karakterler.
        [^0-9] => rakam olmayan karakterler.

"""
result = re.findall("[abc]",str)
result = re.findall("[a-e]",str)
result = re.findall("[a-z]",str)
result = re.findall("[0-5]",str)
##########################################################
"""
        . - Herhangi bir karakteri belirtir.
                .. => aa : 1 match
                    ab : 1 match
                    a : No match              

"""
result = re.findall("..",str) # 2 karakterli kelimeleri bulur
result = re.findall("...",str) # 3 karakterli kelimeleri bulur
##########################################################
"""
        ^ - Belirtilen karakterle başlayan ifadeleri seçer.ilk karakteri seçer
            ^a => aa : 1 match
                ab : No match
                ba : No match

        $ - Belirtilen karakterle biten ifadeleri seçer.
            a$ => aa : 1 match
                ba : 1 match
                ab : No match
"""
result = re.findall("^P",str) # P ile başlayan kelimeleri bulur
result = re.findall("t$",str) # t ile biten kelimeleri bulur
##########################################################
"""
        * - Bir karakterin sıfır ya da daha fazla sayıda geçtiği durumları seçer.

        ma*n => mn : 1 match
                man : 1 match
                maan : 1 match
                main : No match (a karakterinden sonra i karakteri geldiği için)

"""
result = re.findall("sa*t",str) # a harfi 0 ya da daha fazla olabilir
##########################################################
"""
        + - Bir karakterin bir ya da daha fazla sayıda geçtiği durumları seçer
            ma+n => mn : No match
                    man : 1 match
                    maan : 1 match
                    main : No match (a karakterinden sonra i karakteri geldiği için)n gelmiyor
"""
result = re.findall("sa+t",str) # a harfi 1 ya da daha fazla olabilir
##########################################################
"""
        ? - Bir karakterin sıfır ya da bir kez geçtiği durumları seçer
            
"""
result = re.findall("sa?t",str) # a harfi 0 ya da 1 kez geçebilir
##########################################################
"""
    {}-karakter sayısını kontorl eder
        al{2} => al : No match
                all : 1 match
                alll : No match
"""
result = re.findall("Python{1}",str) # n harfi 1 kez geçebilir
result = re.findall("Python{2}",str) # n harfi 2 kez geçebilir
##########################################################
print(result)