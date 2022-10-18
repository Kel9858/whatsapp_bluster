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

def search(target):
    target = target.split('"')[1]
    wait = WebDriverWait(driver, 20)
    search_xpath = '//*[@id="side"]/div[1]/div/label/input'
    search_box = wait.until(EC.presence_of_element_located((By.XPATH, search_xpath)))
    search_box.send_keys(target)


newLine ='\ue008\ue007\ue008'
msg = 'Job Vacancies'+newLine+''+newLine+'! Go to our Facebook page for more details and like our page: http://bit.ly/2xFstlU !'+newLine+''+newLine+'Customer Service Executive: Salary RM2500++'+newLine+'1.) Telco Industry :'+newLine+'@ Language requirement: English & Bahasa Malaysia (Ability to speak in Mandarin will be an added advantage).'+newLine+'@ Working hours: (24H Rotational Shift and 2 off day)'+newLine+'@ Whatsapp: http://bit.ly/2WcDqp9'+newLine+''+newLine+'Job Details:'+newLine+'Working Location: Ara Damansara (LRT Ara Damansara)'+newLine+'School Leavers are encourage to apply'+newLine+'Age: 18 and above'+newLine+''+newLine+'For more information, Kindly do WhatsAPP Mr.Aaron(011-51101695).'+newLine+''+newLine+'Or go to our Facebook page for more details and like our page: http://bit.ly/2xFstlU\n'\
      '诚意聘请员工!'+newLine+''+newLine+'! 欢迎来到我们的FB page 了解详情和别忘了给我们个like ^^ : http://bit.ly/2xFstlU !'+newLine+''+newLine+'薪水轻松赚，RM 3000不是梦!'+newLine+'1.)中文客服人员'+newLine+'@条件：基本英文和华文对话能力（会流利广东话更好)'+newLine+'@年龄介于18-35岁'+newLine+'@地点：Petaling Jaya (Ara damansara)'+newLine+'@薪水：RM3000++'+newLine+''+newLine+'Whatsapp: http://bit.ly/2xFQQA4'+newLine+''+newLine+'2.)Customer service executive(Airline Project)'+newLine+'@条件: 基本英文,华文和马来文对话能力'+newLine+'@候选人必须至少拥有SPM学历'+newLine+'@工作时间:（24/7）轮班和休息日工作,9 hours per shift + 1 hours lunch break'+newLine+'@地点：PJ Branch,Selangor'+newLine+'薪水：RM3000++'+newLine+''+newLine+'Whatsapp: http://bit.ly/2xFQQA4'+newLine+''+newLine+'3.)女性电话销售管理员（水机）'+newLine+'@条件:基本英文,华文和马来文对话能力'+newLine+'@候选人必须至少拥有SPM学历。'+newLine+'@工作时间:周一至周五（10am-6pm）'+newLine+'@只有华裔女性'+newLine+'@薪水：RM3000++'+newLine+'@地点：Puchong (nearby to IOI mall)'+newLine+''+newLine+'Whatsapp: http://bit.ly/2xFQQA4'+newLine+''+newLine+''+newLine+'4.)Technical Support'+newLine+'@条件: 基本英文,华文对话能力和书写能力'+newLine+'@候选人必须至少拥有6个月技术支持和故障排除相关经验'+newLine+'@工作时间: 9:00am – 6:00pm（weekdays)'+newLine+'@地点：KL Sentral'+newLine+'薪水：RM3000++'+newLine+''+newLine+'Whatsapp: http://bit.ly/2xFQQA4'+newLine+''+newLine+''+newLine+'5.)Customer Service (Loyalty Program)'+newLine+'@条件: 基本英文,华文对话能力和书写能力'+newLine+'@候选人必须至少拥有1年电话服务中心相关经验'+newLine+'@工作时间: 9:00am – 6:00pm（weekdays)'+newLine+'@地点：KL Sentral'+newLine+'薪水：RM3000++'+newLine+''+newLine+'Whatsapp: http://bit.ly/2xFQQA4'+newLine+''+newLine+''+newLine+'6.)Customer Service (智能手机)'+newLine+'@条件: 基本英文,华文对话能力和书写能力'+newLine+'@候选人必须至少拥有6个月技术支持和故障排除相关经验'+newLine+'@工作时间: 9:00am – 6:00pm（weekdays)'+newLine+'@地点：Cyberjaya'+newLine+'薪水：RM3000++'+newLine+''+newLine+'Whatsapp: http://bit.ly/2xFQQA4'+newLine+''+newLine+'公司将提供:'+newLine+'@舒适干净的工作环境'+newLine+'@专业培训'+newLine+'请联系我 或(Whatsapp) -  011-51101695 (Mr. Aaron).'+newLine+''+newLine+'! 欢迎来到我们的FB page 了解详情和别忘了给我们个like ^^ : http://bit.ly/2xFstlU !\n'\
      '(急聘）聘请大量想出国的员工! (急聘）'+newLine+''+newLine+'@条件: 基本英文,华文对话能力和书写能力'+newLine+'@候选人必须至少拥有College graduate学历。'+newLine+'@候选人必须至少拥有Microsoft Office 知识。'+newLine+'@21岁以下'+newLine+'@地点：Philippines (Manila)'+newLine+'薪水：RM7000++\n'

targets = ['"kenneth lee"',

           ]

while 1:
    for i in range(0, len(targets)):
        print(targets[i])
        search(targets[i])
        time.sleep(10)
        send_msg(targets[i], msg)
        time.sleep(10)
    time.sleep(3900)

