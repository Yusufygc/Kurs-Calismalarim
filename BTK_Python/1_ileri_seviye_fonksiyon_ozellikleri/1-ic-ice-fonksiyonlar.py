# obje olarak fonk kullanımı
""" 
def greeting (name):
    print("Hello", name)

print(greeting("ali"))

print(greeting) # <function greeting at 0x7f8b1c3b7d30> obje döner

greeting2 = greeting

print(greeting2)
print(greeting)

"""
##################################################
# encapsulation --> dışarda dönen mevzu içerdeki fonku etkilemiyorr.
"""
def outer(num1):
    print("outer")# num2 = inner_increment(num1) tanımlamasaydık sadece outer yazdırırdı
    def inner_increment(num1):
        print("inner")
        return num1 + 5
    num2 = inner_increment(num1)# içerdeki fonksiyoınu çağırmamız gerek
    print(num1, num2)

outer(10)
# inner_increment(10) # hata verir çünkü dışarda tanımlı değil sadece outer kapsamında çalışır.
"""
##################################################
# Faktoriyel hesaplama

def factorial(number):
    if not isinstance(number, int):
        raise TypeError("Sayi tam sayi olmalıdır")
    if not number >= 0:
        raise ValueError("Sayi negatif olamaz")

    def inner_factorial(number):
        if number <=1:
            return 1
        return number * inner_factorial(number - 1) # recursive fonksiyon çağrısı
    return inner_factorial(number)

try:
    print(factorial(-5))
except Exception as ex:
    print(ex)
    
number = 5    
print(f"{number} faktöriyel :",factorial(5))
