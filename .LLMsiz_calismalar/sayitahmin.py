import random

gizli_sayi = random.randint(1,100)

while True:
	kullanici_tahmin = int(input("1-100 arasında bir sayi tahmin ederek gizli sayiyi bulmaya çalis : "))
	

	if kullanici_tahmin <gizli_sayi :
		print("yanlis tahmin tahminini yükselt")

	elif kullanici_tahmin > gizli_sayi:
		print("yanlis tahmin tahminini kücült")
		
	else:
		print("Tebrikler gizli sayiyi buldun :",gizli_sayi)
		break


"""
import random

gizli_sayi = random.randint(1,100)

def secenekMenusu():
	print("1-Bir daha denemek ister misin")
	print("2-Gizli sayiyi gör")
	print("3-Cikis")
	


while True:
	kullanici_tahmin = int(input("1-100 arasında bir sayi tahmin ederek gizli sayiyi bulmaya çalis : "))
	

	if kullanici_tahmin <gizli_sayi :
		print("tahminini yükselt")
	elif kullanici_tahmin > gizli_sayi:
		print("tahminini kücült")
	elif kullanici_tahmin == gizli_sayi:
		print("Tebrikler gizli sayiyi buldun :",gizli_sayi)
		break
	else:
		print("yanlis tahmin")
		secenekMenusu()
		cevap =input("Secim : ")
		if cevap == "1":
			continue
		elif cevap == "2":
			print("Gizli sayi :",gizli_sayi)
		elif cevap=="3":
			break
		
"""		

"""
import random

gizli_sayi = random.randint(1,100)

while True:
	kullanici_tahmin = int(input("1-100 arasında bir sayi tahmin ederek gizli sayiyi bulmaya çalis : "))
	if kullanici_tahmin == gizli_sayi:
		print("Tebrikler gizli sayiyi buldun :",gizli_sayi)
		break
	else:
		print("yanlis tahmin")
		cevap =input(" bir daha denemek ister misin (E/H):").lower()
		if cevap == "h":
			break
		
"""
"""
import random

gizli_sayi = random.randint(1,100)

def secenekMenusu():
	print("1-Bir daha denemek ister misin")
	print("2-Gizli sayiyi gör")
	print("3-Cikis")
	

while True:
	kullanici_tahmin = int(input("1-100 arasında bir sayi tahmin ederek gizli sayiyi bulmaya çalis : "))
	
	if kullanici_tahmin == gizli_sayi:
		print("Tebrikler gizli sayiyi buldun :",gizli_sayi)
		break
	else:
		print("yanlis tahmin")
		secenekMenusu()
		cevap =input("Secim : ")
		if cevap == "1":
			continue
		elif cevap == "2":
			print("Gizli sayi :",gizli_sayi)
			break
		elif cevap=="3":
			break
        
"""
