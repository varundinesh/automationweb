#python selenium code to automate login on a website that allows only 10 users to login with same id.
#this was required because lots of users needs to use the same credentials and they could join only when the logged in users signed out.
#this programme tries to login continuously and logs in as soon as any of the existing logged in user signed out.
import time
from selenium import webdriver
#path to the chrome selinium driver
chrome_path = r"C:\Users\Varun\Downloads\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)
#url to the website that we needs to login.
driver.get("http://10.0.0.26:8090")
def login():
    #time.sleep(5)
    #finding the element with id username 
    user = driver.find_element_by_xpath("//input[@name='username']")
    user.send_keys('')
    #registering the username to the input box
    user.send_keys('drishya1015')
    #finding the element with id password
    user = driver.find_element_by_xpath("//input[@name='password']")
    user.send_keys('')
    #sending the password for the corresponding username.obvioiusly not the right one mentioned here.
    user.send_keys('drishya10150')
    #selecting the element with button id
    login = driver.find_element_by_css_selector('#logincaption')
    #automated click on the submit or login button
    login.click()
#running the above code in loops for fixed range.
for i in range(0,1000):
    login()
    #time.sleep(99)



