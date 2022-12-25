"""
Snapchat web spam bot.

:author: Max Milazzo
"""


import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from time import time, sleep
from random import random
# manages imports


MY_USERNAME = "EXAMPLE@gmail.com"
MY_PASSWORD = "PASSWORD123"

USERNAME = '//*[@id="username"]'
PASSWORD = '//*[@id="password"]'
LOGIN = '//*[@id="loginTrigger"]'

TEXT = '//*[@id="root"]/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div/div'
SEND = '//*[@id="root"]/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div/button'


def init():
    """
    Creates driver and opens site.
    
    :return: driver
    :rtype: webdriver
    """

    driver = uc.Chrome(use_subprocess=True)
    driver.get("http://web.snapchat.com/")
    
    input("Wait for site to load (login button MUST be yellow), then press enter to continue...")
    
    return driver


def login(driver):
    """
    Logs into site.
    
    :param driver: current webdriver in use
    :type driver: webdriver
    """
    
    username_elem = driver.find_element(By.XPATH, USERNAME)
    username_elem.send_keys(MY_USERNAME)
    # enters username
    
    sleep(1)
    
    password_elem = driver.find_element(By.XPATH, PASSWORD)
    password_elem.send_keys(MY_PASSWORD)
    # enters password
    
    sleep(1)
    
    login_elem = driver.find_element(By.XPATH, LOGIN)
    login_elem.click()
    # clicks login button


def send_msg(driver, message, delay, wait):
    """
    Sends a single message.
    
    :param driver: current webdriver in use
    :param message: message to send
    :param delay: delay time between typing and sending
    :param wait: waits time between sending messages
    """
    
    text_elem = driver.find_element(By.XPATH, TEXT)
    text_elem.send_keys(message)
    
    sleep(delay)
    # sleeps by "delay" time between typing and sending
    
    click_elem = driver.find_element(By.XPATH, SEND)
    click_elem.click()
    
    sleep(wait)
    # waits after sending to type another message


def main():
    """
    Main run module.
    """
    
    driver = init()
    login(driver)
    
    message = input("Enter spam message\n> ")
    input("Navigate to chat page then click enter...")
    
    print("3")
    sleep(1)
    print("2")
    sleep(1)
    print("1")
    sleep(1)
    print("RUNNING...")
    # run countdown
    
    while True:
        try:
            send_msg(driver, message, 0.5, 0.5)
        except Exception as e:
            print("UNEXPECTED ERROR OCCURED:")
            print("=" * 20)
            print(e)


if __name__ == "__main__":
    main()