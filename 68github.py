import requests

class GitHub:
    def __init__(self):
        self.api_url="https://api.github.com"
        self.token='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'
    def getUser(self,username):
        response=requests.get(self.api_url+"/users/"+username)
        return response.json()
    
    def getRepositories(self,username):
        response=requests.get(self.api_url+"/users/"+username+'/repos')
        return response.json()
    
    # def createRepository(self,name):
    #     data={"name": name,"description": "This is your first repository","homepage": "https://github.com","private": False,"has_issues": True,"has_projects": True,"has_wiki": True}
    #     response=requests.post(f"{self.api_url}/user/repos?access_token={self.token}", json=data)
    #     return response.json()
    def createRepository(self, name):
        header = {
            "Authorization": f"token {self.token}"
        }
        data = {
            "name": name,
            "description": "This is your first repository",
            "homepage": "https://github.com",
            "private": False,
            "has_issues": True,
            "has_projects": True,
            "has_wiki": True
        }
        response = requests.post(f"{self.api_url}/user/repos", headers=header, json=data)
        return response.json()


github= GitHub()




while True:
    secim=input("1- Find User\n2- Get Repositories\n3- Create Repository\n4- Exit\n Seçiminiz: ")
    '''   MehmetFarukAkbulut token: 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                                                                            '''
    if secim=="4":
        break
    else:
        if secim=="1":
            username=input("username: ")
            result=github.getUser(username)
            print(f"name: {result['name']} public repos: {result['public_repos']} followers : {result['followers']}")
        elif secim=="2":
            username=input("username: ")
            result=github.getRepositories(username)
            for repo in result:
                print(repo["name"])
        elif secim=="3":
            name=input("repository name: ")
            result=github.createRepository(name)
            print(result)
        else:
            print("Yanlış giriş yaptınız.")        
    