from selenium.webdriver.common.keys import Keys

from selenium import webdriver
from selenium.webdriver.common.by import By

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

        

    def followUser(self,username):
        self.browser.get("https://www.instagram.com/accounts/login/")
        self.browser.maximize_window()
        time.sleep(2)
        web="https://www.instagram.com/"+username+"/"
        self.browser.get(web)
        self.browser.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(self.username)
        k=self.browser.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        k.send_keys(self.password)
        k.send_keys(Keys.ENTER)
        
        time.sleep(1)
        
        #takip et
        self.browser.find_element(By.XPATH, "//*[@id='react-root']/section/main/div/header/section/div[1]/div[1]/div/div/button").click()

instgrm=Instagram(username,password)
instgrm.followUser("coding")