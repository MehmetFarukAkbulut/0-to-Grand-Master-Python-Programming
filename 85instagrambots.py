from selenium.webdriver.common.keys import Keys

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
import time

username = ""
password = ""

while username == "" and password == "":
    username = input("username: ")
    password = input("password: ")

class Instagram:
    def __init__(self, username, password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password
        self.followers = []

    def signIn(self):
        self.browser.get("https://www.instagram.com/accounts/login/")
        self.browser.maximize_window()
        time.sleep(2)
        self.browser.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(self.username)
        self.browser.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(self.password)
        time.sleep(2)
        self.browser.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button/div').click()
        time.sleep(8)
        
    def getFollowers(self):
        self.browser.get(f"https://www.instagram.com/{self.username}/")
        time.sleep(4)
        self.follower = self.browser.find_elements(By.TAG_NAME, "a")[12]
        time.sleep(2)
        self.browser.execute_script("arguments[0].click();", self.follower)
        time.sleep(2)
        self.followers=self.browser.find_elements(By.CSS_SELECTOR, "span._ac2a")[2].text
        followers=int(self.followers)
        print(followers)
        try:
            followerCount=0 
            
            list=[]
            while True:
                for a in range(0, followers):
                    list.append(self.browser.find_elements(By.CSS_SELECTOR, 'div.x9f619.xjbqb8w.x1rg5ohu.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1n2onr6.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x6s0dn4.x1oa3qoh.x1nhvcw1')[a].text)
                    followerCount += 1
                    if a%4==0:    

                        dialog=self.browser.find_element(By.CSS_SELECTOR, 'div._ac76') 
                        dialog.send_keys(Keys.SHIFT + Keys.TAB)
                        time.sleep(3)
                        self.browser.execute_script("arguments[0].click();", dialog)
                        time.sleep(2)
                    if followers != followerCount:
                        print(f"Takipçi sayınız yazılıyor... {followerCount}")
                    else:
                        print(f"Toplam takipçi sayınız: {followerCount}")
                        break
                time.sleep(1)
        except Exception as e:
            print(e)
        for user in list:
            print(user)
        with open(f"85followers{self.username}.txt","w",encoding="UTF-8")as file:
            for item in list:
                file.write(item+"\n")
    
    def followUser(self, username):
        self.browser.get("https://www.instagram.com/accounts/login/")
        self.browser.maximize_window()
        time.sleep(2)
        
        login_input = self.browser.find_element(By.NAME, 'username')
        login_input.send_keys(self.username)
        
        password_input = self.browser.find_element(By.NAME, 'password')
        password_input.send_keys(self.password)
        password_input.send_keys(Keys.ENTER)
        
        time.sleep(5)
        
        user_url = f"https://www.instagram.com/{username}/"
        self.browser.get(user_url)
        
        try:
            time.sleep(10)
            followButton=self.browser.find_element(By.TAG_NAME, "button")
            if followButton.text!= "Following":
                followButton.click()
                time.sleep(2)
            else:
                print("Zaten takiptesin")
            time.sleep(10)
            
        except Exception as e:
            print(e)
            time.sleep(10)
    
    
    def followAndLikeUser(self, username):
        self.browser.get("https://www.instagram.com/accounts/login/")
        self.browser.maximize_window()
        time.sleep(2)
        
        login_input = self.browser.find_element(By.NAME, 'username')
        login_input.send_keys(self.username)
        
        password_input = self.browser.find_element(By.NAME, 'password')
        password_input.send_keys(self.password)
        password_input.send_keys(Keys.ENTER)
        
        time.sleep(5)
        
        user_url = f"https://www.instagram.com/{username}/"
        self.browser.get(user_url)
        
        try:
            time.sleep(10)
            followButton = self.browser.find_element(By.TAG_NAME, "button")
            if followButton.text != "Following":
                followButton.click()
                time.sleep(2)
                print(f"{username} adlı kullanıcıyı takip ettin.")
            else:
                print(f"{username} adlı kullanıcıyı zaten takiptesin.")
                time.sleep(2)
            self.post=self.browser.find_elements(By.CSS_SELECTOR, "span._ac2a")[0].text
            counter=int(self.post)
            self.browser.find_element(By.CLASS_NAME, "_aagw").click()
            a=0
            time.sleep(5)

            while True:
                if counter!=0: 
                    like_button = self.browser.find_elements(By.CSS_SELECTOR, "div._abm0._abl_")[1]
                    time.sleep(2)
                    self.browser.execute_script("arguments[0].click();", like_button)
                    counter-=1 
                while counter>0:
                    if a==0:
                        forward_button = self.browser.find_elements(By.CSS_SELECTOR, "button._abl-")[1]
                        self.browser.execute_script("arguments[0].click();", forward_button)
                        a=1
                    else:
                        forward_button = self.browser.find_elements(By.CSS_SELECTOR, "button._abl-")[2]
                        self.browser.execute_script("arguments[0].click();", forward_button)
                    time.sleep(5)  
                    like_button = self.browser.find_elements(By.CSS_SELECTOR, "div._abm0._abl_")[1]
                    time.sleep(2)
                    self.browser.execute_script("arguments[0].click();", like_button)
                    time.sleep(2)
                    counter-=1 
                print(f"{username} adlı kullanıcının bütün gönderilerini beğendin. ")  
                break   
        except Exception as e:
            print("Gönderileri beğenirken hata aldın.İşte hata:\n ",e)
            time.sleep(5)
    
    
    def unfollowUser(self, username):
        self.browser.get("https://www.instagram.com/accounts/login/")
        self.browser.maximize_window()
        time.sleep(2)
        
        login_input = self.browser.find_element(By.NAME, 'username')
        login_input.send_keys(self.username)
        
        password_input = self.browser.find_element(By.NAME, 'password')
        password_input.send_keys(self.password)
        password_input.send_keys(Keys.ENTER)
        
        time.sleep(5)
        
        user_url = f"https://www.instagram.com/{username}/"
        self.browser.get(user_url)
        
        try:
            time.sleep(10)
            followButton=self.browser.find_element(By.TAG_NAME, "button")
            if followButton.text== "Following":
                followButton.click()
                time.sleep(2)
                self.browser.find_element(By.XPATH,'//button[text()="Unfollow"]').click()
            else:
                print("Zaten takip etmiyorsun.")
            time.sleep(10)
            
        except Exception as e:
            print(e)
            time.sleep(10)
            




instgrm=Instagram(username,password)
instgrm.signIn()
instgrm.getFollowers()
instgrm.followUser()
instgrm.followAndLikeUser()
instgrm.unfollowUser()
