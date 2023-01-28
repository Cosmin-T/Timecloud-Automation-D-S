import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def send_email(driver):
    """This is a function that sends out an email with a code if the cookies are no longer available

    Args:
        driver (WebDriver): The web driver to which the cookies will be added.
        
    Returns: 
        webdriver.Chrome: pressing on send button
    """
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@name = 'SendEmailButton']"))).click()
    print('Email sent successfully')

         
         

         
