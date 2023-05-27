from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 

class LinkedIn:
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
            self.browser.get('https://www.linkedin.com/sales/inbox/')
            self.browser.maximize_window()
            time.sleep(10)
            # username input
            userinput=self.browser.find_element(By.XPATH, "//input[@id='username']")
            userinput.click()
            userinput.send_keys(self.username)

            # password input
            passwordinput=self.browser.find_element(By.XPATH, "//input[@id='password']")
            passwordinput.click()
            passwordinput.send_keys(self.password)
            # enter
            self.browser.find_element(By.XPATH, "//input[@id='password']").send_keys(Keys.ENTER)
            time.sleep(15)
        except Exception as e:
            print(e)
    def searchMessage(self,hashtag,kisi):
        try:
            nowChatList=[]
            chatwithhashtag=[]
            # 1848 kişi
            for a in range(0,(kisi//20)):
                moreUserbutton=self.browser.find_element(By.XPATH,"//button[@id='ember965']")    
                moreUserbutton.click()
                time.sleep(2)
            
            for person in range(0,kisi):
                self.browser.find_elements(By.XPATH,"//li[@class='list-style-none conversation-list-item']")[person].click()
                time.sleep(2)
                personname=self.browser.find_element(By.XPATH,"//div[@class='artdeco-entity-lockup__title ember-view']/span[@data-anonymize='person-name']").text
                print(personname)
                nowChat=self.browser.find_elements(By.XPATH,"//div[@data-x-message-content='message']")

                for chat in nowChat:
                    nowChatList.append(chat.text)
                    for i in chat:
                        if hashtag in nowChatList:
                            chatwithhashtag.append(f"{personname} kullanıcısından mesaj: {i}")
            for x in chatwithhashtag:
                print(x)
        except Exception as e :
            print(e)
    
    
    
    
username = ""
password = ""
hashtag=""

while username == "" and password == "":
    username = input("username: ")
    password = input("password: ")
    hashtag = input("hashtag: ")
    

lkn=LinkedIn(username,password)
lkn.signIn()
lkn.searchMessage(hashtag,kisi)