
def toplama(a,b):
    return a+b

def carpma(a,b):
    return a*b

def cikarma(a,b):
    return a-b

def bolme(a,b):
    return a/b

def islem(f1,f2,f3,f4,islem_adi):
    if islem_adi == "toplama":
        print(f1(3,4))
    elif islem_adi == "carpma":
        print(f2(3,4))
    elif islem_adi == "cikarma":
        print(f3(3,4))
    elif islem_adi == "bolme":
        print(f4(3,4))
    else:
        print("Geçersiz işlem")

islem(toplama,carpma,cikarma,bolme,"toplama")
islem(toplama,carpma,cikarma,bolme,"carpma")
islem(toplama,carpma,cikarma,bolme,"cikarma")
islem(toplama,carpma,cikarma,bolme,"bolme")
islem(toplama,carpma,cikarma,bolme,"bolmee")
