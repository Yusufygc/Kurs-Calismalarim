import os
import datetime
result = dir(os)
result = os.name # nt=windows posix=linux
result = os.getcwd() # içinde bulunduğumuz dizin
result = os.listdir() # dizin içindeki dosya ve klasörleri listeler.
print(result)

########################################################################
# KLASÖR İŞLEMLERİ
########################################################################
# os.mkdir("newdirectory") # içinde bulunduğumuz dizinde yeni bir klasör oluşturur.
# os.chdir("C:\\") # dizin değiştirme
# os.chdir("../") # bir üst dizine çıkar.
# os.makedirs("newdirectory/yeniklasor") # iç içe klasör oluşturur.
# os.rmdir("newdirectory") # klasör silme
# os.removedirs("newdirectory/yeniklasor") # iç içe klasör silme
# os.rename("newdirectory","yeniklasor") # klasör adı değiştirme
########################################################################
for dosya in os.listdir(): # dizin içindeki dosyaları listeler.biz py ile bitenleri listeledik.
    if dosya.endswith(".py"):
        print(dosya)
########################################################################
# DOSYA HAKKINDA BİLGİLER EDİNME
########################################################################
#result = os.stat("1_datetime.py") # dosya hakkında bilgi verir.
#print(result)

#result = result.st_size/1024 # dosyanın boyutunu verir.
#print(result)

#result= datetime.datetime.fromtimestamp(result.st_ctime) # dosyanın oluşturulma tarihini verir.
#print(result)

#result= datetime.datetime.fromtimestamp(result.st_atime) # dosyanın son erişilme tarihini verir.
#print(result)

#result= datetime.datetime.fromtimestamp(result.st_mtime) # dosyanın son değiştirilme tarihini verir.
#print(result)
########################################################################
# PATH İŞLEMLERİ
########################################################################
"""
result = os.path.abspath("2_os.py") # dosyanın tam yolunu verir.
print("Dosya yolu       : ",result)

result = os.path.dirname(os.path.abspath("2_os.py")) # dosyanın bulunduğu dizini verir.
print("Dosya dizini     : ",result)

result = os.path.exists("2_os.py") # dosyanın var olup olmadığını kontrol eder.
print("Dosyanın varlığı : ",result)

result = os.path.dirname(os.path.abspath("2_os.py")) # dosyanın bulunduğu dizini verir.
print("Dosya dizini     : ",result)

result = os.path.isdir("C:\\") # dizin mi değil mi kontrol eder.
print("C:\\ Dizini mi   : ",result)

result = os.path.isfile("C:\\") # dosya mı değil mi kontrol eder.
print("C:\\ Dosya mı    : ",result)

result = os.path.join("C:\\","deneme","deneme1") # dosya yolu birleştirme
"""
result = os.path.split("C:\\deneme") # dosya yolu ayırma
print(result)

result = os.path.splitext("2_os.py") # dosya uzantısı yolu ayırma
result1 = result[0]
result2 = result[1]
print("dosya adı  : ",result1)
print("uzantı adı : ",result2)
print(result)