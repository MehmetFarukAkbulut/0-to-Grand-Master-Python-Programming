from selenium import webdriver
from selenium.webdriver.common.by import By
import time

email = ""
password = ""
while email == "" and password == "":
    email = input("email: ")
    password = input("password: ")

class Instagram:
    def __init__(self, email, password):
        self.browser = webdriver.Chrome()
        self.email = email
        self.password = password
        self.followers = []

    def signIn(self):
        self.browser.get("https://www.secure.instagram.com/accounts/login/")
        time.sleep(2)
        self.browser.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(self.email)
        self.browser.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(self.password)
        time.sleep(1)
        self.browser.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button/div').click()
        
instgrm=Instagram(email,password)
instgrm.signIn()