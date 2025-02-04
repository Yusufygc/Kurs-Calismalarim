# datetime modülü ile tarih ve saat işlemleri yapabiliriz.
"""import datetime
result = datetime.datetime.now()
print(result)
print("yıl    :",  result.year)
print("Ay     :",result.month)
print("Gün    :",result.day)
print("Saat   :",result.hour)
print("Dakika :",result.minute)
print("Saniye :",result.second)
print("--------------------------------")
datetime_icerigi = dir(datetime)
print(datetime_icerigi)
"""
###############################################################################
# tüm kütüphaneyi import etmeden işimize yarayan kısmı import edebiliriz.
"""
from datetime import datetime
result = datetime.now()
datetime_icerigi = dir(datetime)
#print(datetime_icerigi)
print(result)
print("yıl    :",  result.year)
print("-------------------------------")
simdi=datetime.today()
print("Bugün :",simdi)# today ve now aynı işlemi yapar.
"""
###############################################################################
# Bazı fonksiyonlar
from datetime import datetime
"""
simdi=datetime.now()
result=datetime.ctime(simdi) # ay adı ve gün adı ile tarih ve saat bilgisini verir.
print(result)

result=datetime.strftime(simdi,'%Y') # yıl bilgisini verir.
print("yıl           :",result)
result=datetime.strftime(simdi,'%X') # saat bilgisini verir.
print("saat          :",result)
result=datetime.strftime(simdi,'%d') # gün bilgisini verir.sayısal olarak.
print("gün           :",result)
result=datetime.strftime(simdi,'%A') # gün adını verir.
print("gün           :",result)
result=datetime.strftime(simdi,'%B') # ay adını verir.
print("ay            :",result)
result=datetime.strftime(simdi,'%Y %B %A') # yıl ay gün bilgisini verir.
print("tarih         :",result)
result=datetime.strftime(simdi,'%Y %B %A %X') # yıl ay gün saat bilgisini verir.
print("tarih ve saat :",result)
print("-------------------------------")

t= "15 April 2019 hour 10:12:30"
result=datetime.strptime(t,'%d %B %Y hour %H:%M:%S') # string ifadeyi tarih ve saat bilgisine çevirir.
print("string ifadeden : ",result)
print(result.year)
print(result.month)
print(result.day)
"""
###############################################################################

birthday=datetime(1999,12,10,12,30,10)
result=datetime.timestamp(birthday) # tarihi saniye cinsinden verir.
print(result)

result=datetime.fromtimestamp(result)
print(result) # saniye cinsinden verilen tarihi tarih ve saat bilgisine çevirir.

result=datetime.fromtimestamp(0)
print(result) # 0 saniyeden itibaren geçen tarih ve saat bilgisini verir. 1970-01-01 03:00:00 çünkü bilgisayarların miladı 1970-01-01 03:00:00 dir.

simdi=datetime.now()
result=simdi-birthday # timedelta
print(result) # iki tarih arasındaki farkı verir.

result=result.days
print(result) # iki tarih arasındaki farkı gün cinsinden verir.

#result=result.seconds
#print(result) # iki tarih arasındaki farkı saniye cinsinden verir.

result=result//3600
print(result) # iki tarih arasındaki farkı saat cinsinden verir.

from datetime import timedelta

result=timedelta(days=10)
print(result)

simdi=datetime.now()
print(simdi)
result=simdi+result
print(result) # bugünden 10 gün sonrasını verir.