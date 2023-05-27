from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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
        try:
            self.browser.get('https://twitter.com/i/flow/login')
            self.browser.maximize_window()
            time.sleep(5)
            # username input
            self.browser.find_element(By.CSS_SELECTOR, "input.r-30o5oe.r-1niwhzg.r-17gur6a.r-1yadl64.r-deolkf.r-homxoj.r-poiln3.r-7cikom.r-1ny4l3l.r-t60dpp.r-1dz5y72.r-fdjqy7.r-13qz1uu").send_keys(self.username)
            # enter
            self.browser.find_element(By.CSS_SELECTOR, "input.r-30o5oe.r-1niwhzg.r-17gur6a.r-1yadl64.r-deolkf.r-homxoj.r-poiln3.r-7cikom.r-1ny4l3l.r-t60dpp.r-1dz5y72.r-fdjqy7.r-13qz1uu").send_keys(Keys.ENTER)
            time.sleep(2)
            # password input.r-30o5oer-1niwhzg.r-17gur6a.r-1yadl64.r-deolkf.r-homxoj.r-poiln3.r-7cikom.r-1ny4l3l.r-t60dpp.r-1dz5y72.r-fdjqy7.r-13qz1uu
            self.browser.find_element(By.XPATH, "//input[@type='password']").send_keys(self.password)
            # enter
            self.browser.find_element(By.XPATH, "//input[@type='password']").send_keys(Keys.ENTER)
            time.sleep(15)
        except Exception as e:
            print(e)

    def search(self,hashtag):
        try:
            searchInput=self.browser.find_element(By.CSS_SELECTOR,"input.r-30o5oe.r-1niwhzg.r-17gur6a.r-1yadl64.r-deolkf.r-homxoj.r-poiln3.r-7cikom.r-1ny4l3l.r-xyw6el.r-13rk5gd.r-1dz5y72.r-fdjqy7.r-13qz1uu")
            searchInput.send_keys(hashtag)
            time.sleep(2)
            searchInput.send_keys(Keys.ENTER)
            time.sleep(5)
            
            list=self.browser.find_elements(By.CSS_SELECTOR,"div.css-901oao.r-1nao33i.r-37j5jr.r-a023e6.r-16dba41.r-rjixqe.r-bcqeeo.r-bnwqim.r-qvutc0")
            for item in list:
                print("***********************************")
                print(item.text)
            time.sleep(3)
        except Exception as e:
            print(e)



username = ""
password = ""
hashtag=""

while username == "" and password == "" and hashtag=="":
    username = input("username: ")
    password = input("password: ")
    hashtag = input("search hashtag: ")

twt=Twitter(username,password)
twt.signIn()
twt.search(hashtag)