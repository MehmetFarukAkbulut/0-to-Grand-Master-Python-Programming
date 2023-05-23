from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
        time.sleep(1)
        self.browser.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button/div').click()
        time.sleep(3)
        
    def getFollowers(self):
        self.browser.get(f"https://www.instagram.com/{self.username}/")
        time.sleep(3)

        self.browser.find_element(By.XPATH, '//a[contains(@href, "/followers/")]').click()
        time.sleep(2)
        followers=self.browser.find_element(By.CSS_SELECTOR, 'div[role=dialog ul]').find_elements(By.CSS_SELECTOR,'li')
        for user in followers:
            link=user.find_element(By.CSS_SELECTOR,"a").get_attribute("href")
            print(link)
instgrm=Instagram(username,password)
instgrm.signIn()
instgrm.getFollowers()
