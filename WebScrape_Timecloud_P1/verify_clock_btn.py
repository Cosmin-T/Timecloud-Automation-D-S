from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

clock_btn = '//*[@id="clock_punch"]/div/div/ul/li[1]/div/button'
def check_xpath(xpath, driver):
    """
    Checks if element specified by xpath exists in the page

    Args:
        xpath (str): The xpath of the element to check for
        driver (WebDriver): The Selenium WebDriver instance to use

    Returns:
        bool: True if element exists, False if it does not
    """
    try:
        driver.find_element('xpath', xpath)
    except NoSuchElementException:
        return False
    return True