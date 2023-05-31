
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys



email = ""
password = ""

while email == "" and password == "":
    email = input("username: ")
    password = input("password: ")

inpt=input("İçinde geçen bütün mailleri sileceğim kelime:  ")
class Gmail:
    def __init__(self, email, password):
        self.browser = webdriver.Chrome()
        self.email = email
        self.password = password
        self.followers = []
    def signIn(self):
        self.browser.get("https://mail.google.com/mail/u/0/#inbox")
        self.browser.maximize_window()
        time.sleep(2)
        e=self.browser.find_element(By.XPATH, '//*[@id="identifierId"]')
        e.send_keys(self.email)
        e.send_keys(Keys.ENTER)
        p=self.browser.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        p.send_keys(self.password)
        p.send_keys(Keys.ENTER)
        time.sleep(1)
        self.browser.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button/div').click()
        time.sleep(3)
        
    def delete(self):
        self.browser.get("https://mail.google.com/mail/u/0/#inbox")
        self.browser.maximize_window()
        while True:
            time.sleep(2)
            search=self.browser.find_element(By.XPATH, '//*[@id="gs_lc50"]/input[1]')
            search.send_keys(inpt)
            self.browser.find_element(By.XPATH, '//*[@id=":qy"]/div[1]/span').click()
            time.sleep(3)

            self.browser.find_element(By.XPATH, '//*[@id=":4"]/div[3]/div[2]/div[1]/div/div/div[2]/div[3]/div').click()
            time.sleep(3)
            try:self.browser.find_element(By.XPATH, '//*[@id=":3ll"]').click()
            except: break     
            
gml=Gmail(email,password)
gml.signIn()
gml.delete()