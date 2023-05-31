from selenium import webdriver
import time

driver=webdriver.Chrome()


url="https://github.com/MehmetFarukAkbulut"

driver.get(url)

time.sleep(2)
driver.maximize_window()
driver.save_screenshot("mygithub-homepage.jpeg")

url="https://www.linkedin.com/in/mehmet-faruk-akbulut-692340236/"

driver.get(url)



print(driver.title)

if "Mehmet Faruk Akbulut" in driver.title:
    driver.save_screenshot("mylinkedIn-homepage.jpeg")


time.sleep(2)

driver.back()
# driver.forward()

time.sleep(2)


driver.close()