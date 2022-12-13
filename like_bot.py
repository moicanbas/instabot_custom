import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random

users_list=('snoopdogg')
print(users_list)

driver = webdriver.Chrome(executable_path=r"./chromedriver")  
time.sleep(random.randint(2, 4))
driver.get('https://www.instagram.com')

user_element = driver.find_element_by_xpath("//input[@name='username']")
user_element.clear()
time.sleep(random.randint(1, 3))
user_element.send_keys('username')
password_element = driver.find_element_by_xpath("//input[@name='password']")
password_element.clear()
password_element.send_keys('password')
time.sleep(random.randint(1, 3))
password_element.send_keys(Keys.RETURN)

driver.get('https://www.instagram.com/'+users_list)
driver.find_element_by_xpath('//ul[@class=" x78zum5 x1q0g3np      xieb3on"]/li[2]/a').click()
time.sleep(2)
followers_username=[]
followers=driver.find_elements_by_xpath('//div[@class="_aacl _aaco _aacu _aacx _aada"]/div/span/a/span/div')
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

for i in followers:
  followers_username.append(i.text)

for i in followers_username:
  driver.get('https://www.instagram.com/'+i)
  time.sleep(random.randint(2, 4))
  post=driver.find_elements_by_xpath('//div[@class="_ac7v _aang"]/div[1]/a')
  if post:
      post[0].click()
      time.sleep(2)
      like= driver.find_elements_by_xpath('//div[@class="_ae2s _ae3v _ae3w"]/section[1]/span[1]/button')
      like[0].click()
  if not post:
      continue
  print('complete for :'+i)
  time.sleep(random.randint(2, 4))



  