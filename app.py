from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import pyautogui
import time
option = webdriver.ChromeOptions()
option.add_argument('start-maximized')
service = Service()
driver = webdriver.Chrome(service=service,options=option)
url='https://www.google.com.br/'
driver.get(url)
time.sleep(2)

#click into the box
driver.find_element("xpath",'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea').click()
time.sleep(1)


driver.find_element("xpath",'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea').send_keys('free course python programming')
time.sleep(2)
#press enter
pyautogui.press('enter')
time.sleep(5)