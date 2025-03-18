"""
1. Fonksiyon Tanımları
usAlma(number) fonksiyonu: Bu, bir closure (kapanış) fonksiyonu oluşturur. usAlma fonksiyonu bir sayı (number) alır ve bir iç fonksiyon olan inner_usAlmayı döndürür.
inner_usAlma(power) fonksiyonu, verilen number değerini power üssüne yükseltir (number ** power).

2. two = usAlma(2)
Bu satırda, usAlma(2) çağrılır.
usAlma fonksiyonu number parametresine 2 değerini alır ve inner_usAlma fonksiyonunu döndürür.
Bu fonksiyonun içinde number değeri artık 2 olarak "saklanır". Bu mekanizmaya closure denir.
Artık two değişkeni, inner_usAlma(power) fonksiyonunu temsil eder ve içinde number = 2 sabitlenmiştir.

3. three = usAlma(3)
Bu satırda, usAlma(3) çağrılır.
usAlma fonksiyonu number parametresine 3 değerini alır ve yine inner_usAlma fonksiyonunu döndürür.
Bu kez, number = 3 olarak "saklanır".
Artık three değişkeni, inner_usAlma(power) fonksiyonunu temsil eder ve içinde number = 3 sabitlenmiştir.

4. print(two(3))
two(3) ifadesi, inner_usAlma(power) fonksiyonunu çağırır. Bu fonksiyonda:
number değeri, usAlma(2) çağrısından dolayı 2 olarak sabitlenmiştir.
power parametresine ise 3 atanır.
Bu yüzden işlem şu şekilde yapılır: 2 ** 3 = 8.
Çıktı: 8

5. print(three(4))
three(4) ifadesi, inner_usAlma(power) fonksiyonunu çağırır. Bu fonksiyonda:
number değeri, usAlma(3) çağrısından dolayı 3 olarak sabitlenmiştir.
power parametresine ise 4 atanır.
Bu yüzden işlem şu şekilde yapılır: 3 ** 4 = 81.
Çıktı: 81

Özet:
Bu kod, closure kullanarak dinamik olarak üstel fonksiyonlar oluşturan bir yapı kurar. usAlma fonksiyonu bir sayı alır ve bu sayı için bir üstel işlem yapan fonksiyonu döndürür. Daha sonra döndürülen fonksiyon farklı üs değerleriyle çağrılarak işlem yapılabilir.

two = usAlma(2) bu işlemde two da fonksiyon oldu demi?
Evet, two bir fonksiyon haline geliyor. Şimdi bunu biraz daha detaylı açıklayayım:

usAlma(2) Ne Yapar?
usAlma fonksiyonu çağrılır:

number parametresine 2 değeri atanır.
usAlma içinde tanımlı inner_usAlma adlı bir iç fonksiyon vardır.
inner_usAlma döndürülür:

usAlma fonksiyonu, inner_usAlma adlı fonksiyonu bir obje olarak döndürür.
Döndürülen fonksiyonun içinde, number = 2 değeri kapanış (closure) ile saklanır.
two artık inner_usAlma fonksiyonuna referans eder:

Yani, two şu an aslında bir fonksiyondur.
Bu fonksiyonun power adında bir parametresi vardır ve sabit bir number = 2 değerine sahiptir.
###################
# two(3) çağrısı, şu şekilde çalışır:
def inner_usAlma(power):
    return 2 ** power  # Buradaki "2", closure'dan gelir.

# Sonuç:
print(two(3))  # 2 ** 3 = 8
###################

two tam olarak inner_usAlma fonksiyonuna eşittir ama içinde number = 2 değeri saklanmıştır. Her usAlma çağrısında bu değer farklı olabilir. Bu sayede, farklı sayılar için farklı üslerle işlem yapabiliriz.

Özet:
Evet, two bir fonksiyon objesidir, çünkü usAlma(2) çağrısı sonucunda inner_usAlma adlı fonksiyon döndürülür ve two bu fonksiyonu temsil eder. Bu mekanizma sayesinde farklı tabanlar (örneğin 2, 3, vb.) için üstel hesaplama yapacak farklı fonksiyonlar oluşturabilirsiniz.

## KODU ÇALIŞTIR ##
def usAlma(number):
    def inner_usAlma(power):
        return number ** power
    return inner_usAlma

two = usAlma(2)
three = usAlma(3)

print(two(3))
print(three(4))
"""
##################################################
"""
def yetki_sorgula(page):
    def inner(role):
        if role == "Admin":
            return "{0} rolü {1} sayfasına ulaşabilir.".format(role, page)
        else:
            return "{0} rolü {1} sayfasına ulaşamaz.".format(role, page)
    return inner

user1 = yetki_sorgula("Product Edit") # page = "Product Edit"
print(user1("Admin"))
print(user1("User"))
"""
##################################################

def islem(islem_adi):
    def toplam(*args):
        toplam =0
        for i in args:
            toplam += i
        return toplam
        
    def carpma(*args):
        carpim = 1
        for i in args:
            carpim *= i
        return carpim
    
    if islem_adi == "toplama":
        return toplam
    elif islem_adi == "carpma":
        return carpma
    
toplama = islem("toplama")
carpma = islem("carpma")
print("SAYILARIN TOPLAMI :" ,toplama(1,2,3,4,5))
print("SAYILARIN CARPİMİ :" ,carpma(1,2,3,4,5))
