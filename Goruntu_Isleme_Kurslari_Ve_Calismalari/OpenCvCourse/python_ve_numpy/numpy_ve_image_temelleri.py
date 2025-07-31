import numpy as np 

#--------------------------------------------------------------#
#--------------------------------------------------------------#
mylist = [1,2,3]
print(type(mylist))
#--------------------------------------------------------------#
#--------------------------------------------------------------#
myarray = np.array(mylist) # numpy array oluşturduk
print(myarray)
print(type(myarray))
#--------------------------------------------------------------#
#--------------------------------------------------------------#
sayi_olustur= np.arange(0,10) # 0'dan 10'a kadar sayılar oluşturur
print(sayi_olustur)
#--------------------------------------------------------------#
#--------------------------------------------------------------#
ikiser_ikiser_sayi_olustur= np.arange(0,10,2) 
print(ikiser_ikiser_sayi_olustur)
#--------------------------------------------------------------#
#--------------------------------------------------------------#
cok_boyutlu_array = np.zeros(shape=(5,5)) # 5'e 5'lik 0'lardan oluşan bir matris oluşturduk
print(cok_boyutlu_array)
 
cok_boyutlu_array2= np.zeros(shape=(10,5)) # 10'a 5'luk 0'lardan oluşan bir matris oluşturduk
print(cok_boyutlu_array2)
#--------------------------------------------------------------#
#--------------------------------------------------------------#
cok_boyutlu_array3=np.ones(shape=(2,4)) # 2'ye 4'lük 1'lerden oluşan bir matris oluşturduk
print(cok_boyutlu_array3) 

cok_boyutlu_array4=np.ones((3,3))
print(cok_boyutlu_array4)

#--------------------------------------------------------------#
#--------------------------------------------------------------#

random_array = np.random.randint(0,10,5) # 0'dan 10'a kadar 5 tane rastgele sayı oluşturduk
print(random_array)

random_array2 = np.random.randint(0,100,10) # 0'dan 10'a kadar 10 tane rastgele sayı oluşturduk
print(random_array2)

print(random_array2.max()) # random_array2 içindeki en büyük sayıyı verir
print(random_array2.min()) # random_array2 içindeki en küçük sayıyı verir
print(random_array2.mean()) # random_array2 içindeki sayıların ortalamasını verir
print(random_array2.argmax()) # random_array2 içindeki en büyük sayının indexini verir
print(random_array2.argmin()) # random_array2 içindeki en küçük sayının indexini verir
print(random_array2.reshape(2,5)) # random_array2 içindeki sayıları 2'ye 5'lik matris haline getirir
print(random_array2.reshape(5,2)) # random_array2 içindeki sayıları 5'e 2'lik matris haline getirir
print(random_array2.reshape(10,1)) # random_array2 içindeki sayıları 10'a 1'lik matris haline getirir
print(random_array2.reshape(1,10)) # random_array2 içindeki sayıları 1'e 10'luk matris haline getirir
print(random_array2.reshape(10,)) # random_array2 içindeki sayıları 10'a 1'lik matris haline getirir

#--------------------------------------------------------------#
#--------------------------------------------------------------#

mat = np.arange(0,100).reshape(10,10) # 0'dan 100'e kadar sayıları 10'a 10'luk matris haline getirir
print(mat)
print(mat.shape) # matrisin boyutunu verir
print(mat[0,0]) # matrisin 0. satır 0. sütunundaki sayıyı verir
print(mat[0,:]) # matrisin 0. satırındaki tüm sayıları verir
print(mat[:,0]) # matrisin 0. sütunundaki tüm sayıları verir
print(mat[0:3,0:3]) # matrisin 0. satır ve 0. sütunundan 3. satır ve 3. sütuna kadar olan sayıları verir
print(mat[0:3,0:3].sum()) # matrisin 0. satır ve 0. sütunundan 3. satır ve 3. sütuna kadar olan sayıların toplamını verir
print(mat[:,0].reshape(10,1)) # matrisin 0. sütunundaki tüm sayıları 10'a 1'lik matris haline getirir
print(mat[5,:].reshape(1,10)) # matrisin 6. satırındaki tüm sayıları 1'e 10'luk matris haline getirir
print(mat[3:8,3:8]) # matrisin 3. satır ve 3. sütunundan 8. satır ve 8. sütuna kadar olan sayıları verir


copy= mat.copy() # matrisin kopyasını oluşturur

print(copy)




















