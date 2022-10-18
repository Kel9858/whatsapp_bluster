# -*- encoding:utf-8 -*-
from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By

import time





# Replace below path with the absolute path

# to chromedriver in your computer
driver = webdriver.Chrome('C:/Users/KEL/Desktop/chromedriver_win32/chromedriver.exe')
driver.get("https://web.whatsapp.com/")
# wait = WebDriverWait(driver, 600)

# locate search input path in whatsapp
def send_msg(target, msg):
    print(target, msg)
    wait = WebDriverWait(driver, 20)
    x_arg_2 = '//span[contains(@title,' + target + ')]'
    group_title_2 = wait.until(EC.presence_of_element_located((By.XPATH, x_arg_2)))
    group_title_2.click()
    time.sleep(10)
    inp_xpath = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
    input_box = wait.until(EC.presence_of_element_located((By.XPATH, inp_xpath)))
    input_box.send_keys(msg)#"hello" + "\ue008" + "\ue007\ue008" + "hello in new line \n")
    time.sleep(10)
    
#locate input path in whatsapp
def search(target):
    target = target.split('"')[1]
    wait = WebDriverWait(driver, 20)
    search_xpath = '//*[@id="side"]/div[1]/div/label/input'
    search_box = wait.until(EC.presence_of_element_located((By.XPATH, search_xpath)))
    search_box.send_keys(target)

# message that you wanted to send 
newLine ='\ue008\ue007\ue008'
msg = 'xxxxx'+newLine+''+newLine+'xxxxx'+newLine+''+newLine+'xxxxx'+newLine+'xxxxx'+newLine+'\n'

# Group or username that you want to send the message to 
targets = ['"group_name_or_username1"','"group_name_or_username2"','"group_name_or_username3"'

           ]

#looping process and time delay 
while 1:
    for i in range(0, len(targets)):
        print(targets[i])
        search(targets[i])
        time.sleep(10)
        send_msg(targets[i], msg)
        time.sleep(10)
    time.sleep(3900)

