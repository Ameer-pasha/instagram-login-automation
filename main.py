import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os


EMAIL_OR_USERNAME = os.getenv('INSTA_USERNAME')
PASS = os.getenv('INSTA_PASSWORD')


def login(username,password):
    chrome_open=webdriver.ChromeOptions()
    chrome_open.add_experimental_option("detach",True)

    drive=webdriver.Chrome(options=chrome_open)
    drive.get("https://www.instagram.com/")

    time.sleep(5)
    drive.find_element(By.XPATH,'//*[@id="loginForm"]/div[1]/div[1'
                                ']/div/label/input').send_keys(username)

    drive.find_element(By.XPATH,'//*[@id="loginForm"]/div[1]/div[2]'
                                '/div/label/input').send_keys(password)

    time.sleep(3)
    drive.find_element(By.XPATH,'//*[@id="loginForm"]/div[1]/div[3]').click()

    time.sleep(5)
    drive.find_element(By.XPATH,'//*[@id="mount_0_0_z/"]/div/div/div[2]/'
                                'div/div/div[1]/div[1]/div[1]/section/main/div/div'
                                '/section/div/button').click()


login(EMAIL_OR_USERNAME,password=PASS)