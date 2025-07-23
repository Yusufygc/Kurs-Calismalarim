import requests

class GitHub:
    def __init__(self):
        self.api_url = "https://api.github.com"
        self.token = "bireysel erişim tokeninizi buraya girin" 

        self.headers = {
            "Accept": "application/vnd.github.v3+json",
            "Authorization": f"token {self.token}"
        }

    def get_user_info(self, username):
        response = requests.get(f"{self.api_url}/users/{username}")
        if response.status_code == 200:
            return response.json()
        else:
            return None
    
    def get_user_repos(self, username):
        response = requests.get(f"{self.api_url}/users/{username}/repos")
        if response.status_code == 200:
            return response.json()
        else:
            return None
        
    def create_repo(self, repo_name, description="", private=False):

        data = {
            "name": repo_name,
            "description": description,
            "private": private
        }
        response = requests.post(f"{self.api_url}/user/repos", headers=self.headers, json=data)
        if response.status_code == 201:
            return response.json()
        else:
            print("Hata oluştu:", response.status_code, response.text)
            return None
        
    def delete_repo(self, owner, repo_name):
        full_repo_name = f"{owner}/{repo_name}"
        response = requests.delete(f"{self.api_url}/repos/{full_repo_name}", headers=self.headers)
        if response.status_code == 204:
            return True
        else:
            print("Hata oluştu:", response.status_code, response.text)
            return False

        
github = GitHub()


while True:
    secim = input("1. Kullanıcı bilgisi al\n2. Kullanıcı reposu al\n3. Repo oluştur\n4. Repo Sil\n5. Çıkış\nSeçiminiz: ")

    if secim =="5":
        print("Çıkılıyor...")
        break
    else:
        if secim == "1":
            username = input("Kullanıcı adını giriniz: ")
            result =github.get_user_info(username)
            if result:
                print(f"Kullanıcı Adı: {result['login']}")
                print(f"Ad: {result['name']}")
                print(f"Bio: {result['bio']}")
                print(f"Takipçi Sayısı: {result['followers']}")
                print(f"Takip Edilen Sayısı: {result['following']}")
                print(f"Repo Sayısı: {result['public_repos']}")
            else:
                print("Kullanıcı bulunamadı.")

        elif secim == "2":
            username = input("Kullanıcı adını giriniz: ")
            result = github.get_user_repos(username)
            if result:
                for repo in result:
                    print(f"Repo Adı: {repo['name']}")
                    print(f"Açıklama: {repo['description']}")
                    print(f"Yıldız Sayısı: {repo['stargazers_count']}")
                    print("-" * 30)
            else:
                print("Kullanıcıya ait repo bulunamadı.")

        elif secim == "3":
            repo_name = input("Oluşturmak istediğiniz repo adını giriniz: ")
            description = input("Repo açıklamasını giriniz (isteğe bağlı): ")
            private = input("Repo özel mi olsun? (evet/hayır): ").lower() == "evet"
            result = github.create_repo(repo_name, description, private)
            if result:
                print(f"Repo başarıyla oluşturuldu: {result['html_url']}")
            else:
                print("Repo oluşturulamadı.")

        elif secim == "4":
            owner = input("GitHub kullanıcı adınızı girin: ")  
            repo_name = input("Silmek istediğiniz repo adını giriniz: ")
            if github.delete_repo(owner, repo_name):
                print(f"Repo başarıyla silindi: {repo_name}")
            else:
                print("Repo silinemedi.")


        else:
            print("Geçersiz seçim, lütfen tekrar deneyin.")
            continue