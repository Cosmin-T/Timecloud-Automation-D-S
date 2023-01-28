import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from search_get_code import get_code

def add_code(driver):
    """This takes the get_code function and checks if it returns the code,
    if the code is present it loads it on the website, clicks the checkbox,
    logs in and clicks in/out

    Args:
        driver (WebDriver): The web driver to which the cookies will be added

    Returns:
        webdriver.Chrome: Adding the code into the input field
    """
    code = get_code()
    if code:
        search_box = driver.find_element(By.NAME, 'TokenValueEmail')
        search_box.send_keys(int(code))
        print(f'Copied code: {code}')
    else:
        print("Code not found")

    # Presses the checkbox button
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='FldMFARememberDevice']/label/b"))).click()

    # Presses the login button
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='AuthenticateMFAButton']"))).click()

    # Waits 15 seconds for the page to load
    time.sleep(15)

    # Press clock in/out button
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="clock_punch"]/div/div/ul/li[1]/div/button'))).click()
    print('Clocked in Successfully')


