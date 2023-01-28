from selenium import webdriver
import time

def initialize_webdriver(url):
    """Opens a Chrome browser, visits the specified URL, and waits for the page to fully load.

    Args:
        url (str): The URL to visit.

    Returns:
        webdriver.Chrome: The Chrome webdriver instance.
    """
    driver = webdriver.Chrome()
    driver.get(url)
    return driver



