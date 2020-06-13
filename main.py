from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import urllib.request as urllib
import time
import cv2
import processcpt

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches",["enable-automation"])
#you probably need the next two options since the website doesnt have an ssl cert.
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
options.add_experimental_option('useAutomationExtension', False)

web = webdriver.Chrome(r"C:\Users\samar\Downloads\chromedriver.exe",options=options)
wait = WebDriverWait(web,10)


web.get("")
processcpt.catch_captcha(web,"captcha")
