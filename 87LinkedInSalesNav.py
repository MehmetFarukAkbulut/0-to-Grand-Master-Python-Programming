from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time 

class LinkedIn:
    def __init__(self,username,password):
        self.service = webdriver.chrome.service.Service(ChromeDriverManager().install())
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs',{'intl.accept_languages':'tr,tr_TR'})
        self.browser = webdriver.Chrome(service=self.service, options=self.browserProfile)
        self.username = username
        self.password = password
        
        time.sleep(5)
        
        
    def signIn(self):
        try:
            self.browser.get('https://www.linkedin.com/uas/login?session_redirect=/sales&fromSignIn=true&trk=navigator')
            self.browser.maximize_window()
            time.sleep(10)
            # username input 
            userinput=self.browser.find_element(By.XPATH, "//*[@id='username']")
            userinput.click()
            userinput.send_keys(self.username)

            # password input
            passwordinput=self.browser.find_element(By.XPATH, "//*[@id='password']")
            passwordinput.click()
            passwordinput.send_keys(self.password)
            # enter
            self.browser.find_element(By.XPATH, "//*[@id='password']").send_keys(Keys.ENTER)
            time.sleep(35)
        except Exception as e:
            print(e)
    def searchMessage(self, hashtag, kisi):
        try:
            self.browser.find_element(By.XPATH, "//*[@id='ember14']").click()
            time.sleep(15)

            nowChatList = []
            chatwithhashtag = []

            # Scroll to the bottom of the chat list
            for _ in range(kisi // 20):
                chat_list = self.browser.find_element(By.XPATH, "//*[@id='content-main']/article/section[1]/div[2]")
                self.browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", chat_list)
                time.sleep(5)
                load_older_button = self.browser.find_elements(By.XPATH, "//*[@class='artdeco-button artdeco-button--1 artdeco-button--secondary ember-view mv1 mhA artdeco-button--0 block']")
                if load_older_button:
                    load_older_button[0].click()
                time.sleep(5)


            for person in range(0, kisi):
                try:
                    person_element = WebDriverWait(self.browser, 10).until(
                        EC.element_to_be_clickable((By.XPATH, f"//*[@id='content-main']/article/section[1]/div[2]/ul/li[{person+1}]"))
                    )
                    person_element.click()
                    time.sleep(2)
                    personname_element = WebDriverWait(self.browser, 10).until(
                        EC.presence_of_element_located((By.XPATH, "//address[@class='mt2 ml8 inline-block t-14 t-bold t-roman ']/span[@data-anonymize='person-name']"))
                    )
                    personname = personname_element.text

                except Exception as e:
                    continue

                nowChat = self.browser.find_elements(By.XPATH, "//*[@class='t-14 white-space-pre-wrap break-words']")
                time.sleep(5)

                if len(nowChat) > 0:
                    for chat_element in nowChat:
                        chat_text = chat_element.text
                        nowChatList.append(chat_text)
                        if hashtag in chat_text:
                            print(f"{personname} kullanıcısından mesaj: {chat_text}")
                            chatwithhashtag.append(f"{personname} kullanıcısından mesaj: {chat_text}")
                            time.sleep(2)
                        nowChatList = []

            for x in chatwithhashtag:
                print(x)
        except Exception as e:
            print(f"An error occurred: {str(e)}")
        
        
    
username = ""
password = ""
hashtag=""
kisi=""
  


while username == "" and password == "" and hashtag==""and kisi=="":
    username = input("username: ")
    password = input("password: ")
    hashtag = input("hashtag: ")
    kisi=int(input("Arayacağınız chat sayısı: "))

lkn=LinkedIn(username,password)
lkn.signIn()
lkn.searchMessage(hashtag,int(kisi))