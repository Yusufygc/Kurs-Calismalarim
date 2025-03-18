# BELLEKTE YER İŞGAL ETMEYEN İTERATORLER ÜRETİR
"""
def cube (): # bellkete gereksiz yer işgal ediyor
    result = []

    for i in range(5):
        result.append(i**3)
    return result

print(cube())
"""
def cube ():
    for i in range(5):
        yield i**3 # bu üretilen değerlere ikinci kez ulaşmak istersem ulaşamam . üretilir ve ekrana yazdırılır
# OLUŞTURDUĞUMUZ DEĞERİ LİSTE İÇİNDE TUTMAMIZA GEREK YOKSA ÜRETİP O AN KULLANMAK İSTİYORSAK YİELD ANAHRTAR KELİMESİNİ KULLANIRIZ

kupler = cube()
print(kupler) # <generator object cube at 0x0000020CCD489430>

generator = cube() # generator objesi oluşturduk

iterator = iter(generator)

print(next(iterator)) # 0
print(next(iterator)) # 1
print(next(iterator)) # 8
print(next(iterator)) # 27

print("*************************")
print("direkt iterator kullandık")
iterator = cube() # direkt iterator ile oluşturduk

print(next(iterator)) # 0
print(next(iterator)) # 1
print(next(iterator)) # 8
print(next(iterator)) # 27

print("*************************")
#   EN KISA ŞEKİLDE YAZMAK İSTERSEK

for i in cube():
    print(i)
print("*************************")

# LİST COMPREHENSİON U GENERATOR A ÇEVİRMEK
    
liste0 = [i*3 for i in range(5)] # liste comprehension
liste1 = (i*3 for i in range(5)) # generator

print(liste0) # [0, 3, 6, 9, 12]
print(liste1) # <generator object <genexpr> at 0x0000020CCD489430>
print(next(liste1)) # 0
print("*************************")