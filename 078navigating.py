from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver=webdriver.Chrome()
url="http://github.com"
driver.get(url)
# time.sleep(1)
driver.maximize_window()
# time.sleep(1)
searchInput = driver.find_element(By.NAME, "q")
# time.sleep(1)
searchInput.send_keys("python")
# time.sleep(2)
searchInput.send_keys(Keys.ENTER)
# time.sleep(2)
# result=driver.page_source
wait = WebDriverWait(driver, 10)

results = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//ul/li/div[2]/div[1]/div[1]/a")))
for element in results:
    print(element.text)
time.sleep(2)
    
# for i in range(1,3):
    # results = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//ul/li/div[2]/div[1]/div[1]/a")))
    # for element in results:
    #     print(element.text)
    # time.sleep(2)
    
    # nextButton = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "next_page")))
    # nextButton=driver.find_element(By.CLASS_NAME, "next_page")
    # nextButton.click()
    
# driver.close()
driver.quit()

# /html/body/div[2]/div[4]/main/div/div[1]/div/form/input[1]
