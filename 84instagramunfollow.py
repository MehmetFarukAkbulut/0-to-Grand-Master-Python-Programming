from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Instagram:
    def __init__(self, username, password):
        
        # webdriver.chrome.service_log_path = "/path/to/chromedriver.log"
        self.service = webdriver.chrome.service.Service(ChromeDriverManager().install())
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs',{'intl.accept_languages':'en,en_US'})
        self.browser = webdriver.Chrome('chromedriver.exe',chrome_options=self.browserProfile,service=self.service)
        self.username = username
        self.password = password
        self.followers = []

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
            

username = ""
password = ""

while username == "" and password == "":
    username = input("username: ")
    password = input("password: ")

instgrm = Instagram(username, password)
instgrm.followUser("mfaruk_akbulut")