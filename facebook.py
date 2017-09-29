import time
from selenium import webdriver
def fblogin():
    chrome_path = r"C:\Users\Varun\Downloads\chromedriver_win32\chromedriver.exe"
    driver = webdriver.Chrome(chrome_path)
    driver.get("https://www.facebook.com/")
    #time.sleep(5)
    user = driver.find_element_by_css_selector('#email')
    user.send_keys('abc@gmail.com')
    password = driver.find_element_by_css_selector('#pass')
    password.send_keys('9979173')
    login = driver.find_element_by_css_selector('#u_0_q')
    login.click()
    # login_attempt = browser.find_element_by_xpath("//*[@type='submit']")
    # login_attempt.submit()

fblogin()



