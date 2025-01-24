# Description: Class ile iterator oluşturmak
class MyNumbers:
    def __init__(self,start,stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start <= self.stop:
            x = self.start
            self.start += 1
            return x
        else:
            raise StopIteration
        
        
list= MyNumbers(10,25)

myiter = iter(list) # __iter__ methodu çağrılır" tek tek yazdırır
for x in myiter:
    print(x)
