from selenium import webdriver
from selenium.webdriver.common.by import By
import time

username = ""
password = ""
while username == "" and password == "":
    username = input("username: ")
    password = input("password: ")


class Github:
    def __init__(self, username, password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password
        self.followers = []

    def signIn(self):
        self.browser.get("https://github.com/login")
        time.sleep(2)
        self.browser.find_element(By.XPATH, '//*[@id="login_field"]').send_keys(self.username)
        self.browser.find_element(By.XPATH, '//*[@id="password"]').send_keys(self.password)
        time.sleep(1)
        self.browser.find_element(By.XPATH, '//*[@id="login"]/div[4]/form/div/input[12]').click()

    def loadFollowers(self):
        items = self.browser.find_elements(By.CSS_SELECTOR, ".d-table.table-fixed.col-12.width-full.py-4.border-bottom.color-border-muted")
        for i in items:
            self.followers.append(i.find_element(By.CSS_SELECTOR, ".f4.Link--primary").text)

    def getFollowers(self):
        self.browser.get(f"https://github.com/{self.username}?tab=followers")
        time.sleep(2)
        self.loadFollowers()
        while True:
            try:
                links = self.browser.find_element(By.CLASS_NAME, "pagination").find_elements(By.TAG_NAME, "a")
                if len(links)==1:
                    if links[0].text=="Next":
                        links[0].click()
                        time.sleep(1)
                        self.loadFollowers()

                    else:
                        break
                else:
                    for link in links:
                        if link.text =="Next":
                            link.click()
                            time.sleep(1)
                            self.loadFollowers()
                        else:
                            continue
            except:
                break


github = Github(username, password)
github.signIn()
github.getFollowers()
print(len(github.followers))
print(github.followers)
