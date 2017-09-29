import time
from selenium import webdriver
def login():
    chrome_path = r"C:\Users\Varun\Downloads\chromedriver_win32\chromedriver.exe"
    driver = webdriver.Chrome(chrome_path)
    driver.get("http://10.0.0.26:8090")
    #time.sleep(5)
    user = driver.find_element_by_xpath("//input[@name='username']")
    user.send_keys('drishya1015')
    user = driver.find_element_by_xpath("//input[@name='password']")
    user.send_keys('drishya10150')
    login = driver.find_element_by_css_selector('#logincaption')
    login.click()
for i in range(10):
    login()
    time.sleep(100000)



