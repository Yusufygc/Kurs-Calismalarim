
import json
import os

class User:
    def __init__(self, username, password,email):
        self.username = username
        self.password = password
        self.email = email

class UserRepository:

    def __init__(self):
        self.users = []
        self.isLoggedIn = False # varsiyalan olarak login olmamış kullanıcılar
        self.currentUser = {} # giriş yapmış kullanıcı

        # json dosyasından kullanıcı verilerini yükleme
        self.loadUser()

    def loadUser(self):
        if os.path.exists("users.json"):
            with open("users.json", "r", encoding="utf-8") as file:
               users = json.load(file)
               print("Kullanıcı verileri başarıyla yüklendi.")
               for user in users:
                   user = json.loads(user)  # JSON string i Python dictionary ye çevirmek için python tarafinda kullanabilecegimiz bir objeye donusturmus olduk
                   newUser = User(user['username'], user['password'], user['email']) # User sınıfından bir nesne oluşturuyoruz
                   self.users.append(newUser)
            print(self.users) # kullanıcı verilerini obje şeklinde liste olarak yazdırma
        else:
            print("Kullanıcı verileri bulunamadı.")

    def register(self, user: User):# kullanıcı kaydı user: User sınıfından bir nesne
        self.users.append(user) #kullaniciyı listeye ekler
        self.savetoFile() # kullanıcı verilerini dosyaya kaydetme
        print(f"{user.username} kullanıcısı başarıyla kaydedildi.")
        

    def login(self,username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                self.isLoggedIn = True
                self.currentUser = user
                print(f"{username} kullanıcısı başarıyla giriş yaptı.")
                return
        print("Kullanıcı adı veya şifre hatalı.")

    def logout(self):
        if self.isLoggedIn:
            print(f"{self.currentUser.username} kullanıcısı başarıyla çıkış yaptı.")
            self.isLoggedIn = False
            self.currentUser = {}
        else:
            print("Önce giriş yapmalısınız.")

    def identity(self):
        if self.isLoggedIn:
            print(f"Giriş yapan kullanıcı: {self.currentUser.username}, Email: {self.currentUser.email}")
        else:
            print("Önce giriş yapmalısınız.")


    def savetoFile(self):
        list = []
        for user in self.users:
            list.append(json.dumps(user.__dict__)) # user nesnesini sözlük olarak listeye ekler cunku json.dump() ile yazdırmak için string formatında olması gerekiyor

        with open("users.json", "w") as file:
            json.dump(list, file, indent=4)  # kullanıcı verilerini JSON formatında dosyaya kaydeder


userRepository = UserRepository()# her seferinde tekar set etmemek icin dongu disinda olusturuyoruz.
# dongu icinde olsaydi her seferinde icindeki kullanici sifirlanip yeni kullanici eklenirdi.

while True:
    print('Menu'.center(50, '*'))
    secim = input('1- Register\n2- Login\n3- LogOut\n4- Identity\n5- Exit\nChoice: ')

    if secim == '5':
        break
    else:
        if secim == '1': # kullanıcı kaydı
            username = input('Username: ')
            password = input('Password: ')
            email = input('Email: ')
            user = User(username, password, email)
            userRepository.register(user)

        elif secim == '2': # giriş yapma login
            
            if userRepository.isLoggedIn:
                print("Zaten giriş yapmış bir kullanıcı var.")
                continue
            else:
                username = input('Username: ')
                password = input('Password: ')
                userRepository.login(username, password)
            
        elif secim == '3':# çıkış yapma logout
            userRepository.logout()

        elif secim == '4':
            userRepository.identity()
        else:
            print('Geçersiz seçim. Lütfen tekrar deneyin.')