# İnstagramda verilen profile giriş yapıp istenilen kullanıcının sayfasını takip ederek tüm gönderilerini beğenen selenium kodu

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

class Instagram:
    def __init__(self, username, password):
        
        # webdriver.chrome.service_log_path = "/path/to/chromedriver.log"
        self.service = webdriver.chrome.service.Service(ChromeDriverManager().install())
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs',{'intl.accept_languages':'en,en_US'})
        self.browser = webdriver.Chrome(service=self.service, options=self.browserProfile)
        self.username = username
        self.password = password
        self.followers = []

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
            
        
username = ""
password = ""
follow=""

while username == "" and password == "" and follow:
    username = input("username: ")
    password = input("password: ")
    follow = input("follow: ")

instgrm = Instagram(username, password)
instgrm.followAndLikeUser(follow)
