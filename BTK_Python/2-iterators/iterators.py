liste = [1,2,3,4]
iterator = iter(liste)

#print(dir(liste))

print(iterator) #<list_iterator object at 0x000002915F7CA0A0>

print(next(iterator)) #1
print(next(iterator)) #2
print(next(iterator)) #3
print(next(iterator)) #4
#print(next(iterator)) #StopIteration

print("*************************")
print("for döngüsü")
print("*************************")
for i in liste:
    print(i)


# FOR DÖNGÜSÜNÜN YAPTIĞI İŞİ KENDİMİZ YAPMAK İSTERSEK ŞU ŞEKİLDE YAPARIZ 
print("*************************")
print("while döngüsü")
print("*************************")
iterator = iter(liste)
while True:
    try:
        print(next(iterator))
    except StopIteration:
        break

    