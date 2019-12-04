from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

username = "user"
message = ["message0","message1","message2","message3","message4","message5"]
chrome = webdriver.Chrome("chromedriver.exe")
chrome.get("https://tellonym.me/" + username)
time.sleep(1)
textArea = chrome.find_element_by_name("tell")
button = chrome.find_element_by_xpath('//*[@id="root"]/div/div/div[4]/div/div[1]/div/div/div[4]/div[3]/div/div[2]/form/button/div/div')

while True:
    textArea.send_keys(random.choice (message))
    button.click()
    time.sleep(5.5)
    if chrome.current_url == ("https://tellonym.me/" + username):
            print("waiting")
            time.sleep(1500000)
    else:
        chrome.back()
    time.sleep(0.50)
    textArea = chrome.find_element_by_name("tell")
    button = chrome.find_element_by_xpath('//*[@id="root"]/div/div/div[4]/div/div[1]/div/div/div[4]/div[3]/div/div[2]/form/button/div/div')
