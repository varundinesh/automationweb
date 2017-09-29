import time
from selenium import webdriver

chrome_path = r"C:\Users\Varun\Downloads\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)
def login():
    driver.get("https://portal.vjcet.ac.in/")
    user = driver.find_element_by_css_selector('#txtUserName_txt')
    user.send_keys('pv13rr173')
    password = driver.find_element_by_css_selector('#txtPassword_txt')
    password.send_keys('9979173')
    plogin = driver.find_element_by_css_selector('#btnLogin')
    plogin.click()

login()
if driver.find_element_by_xpath('//*[@id="menu"]/div[2]/div/ul[2]/li/a'):
    x=driver.find_element_by_xpath('//*[@id="menu"]/div[2]/div/ul[2]/li/a')
    x.click()
    driver.save_screenshot("screenshot.png")

time.sleep(100)



