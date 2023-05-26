from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time 

class Twitter:
    def __init__(self,username,password):
        self.service = webdriver.chrome.service.Service(ChromeDriverManager().install())
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs',{'intl.accept_languages':'en,en_US'})
        self.browser = webdriver.Chrome(service=self.service, options=self.browserProfile)
        self.username = username
        self.password = password
        
        time.sleep(5)
        
        
    def signIn(self):
        self.browser.get('https://twitter.com/i/flow/login')
        self.browser.maximize_window()
        time.sleep(2)
        





username = ""
password = ""

while username == "" and password == "":
    username = input("username: ")
    password = input("password: ")

twt=Twitter(username,password)
twt.signIn()