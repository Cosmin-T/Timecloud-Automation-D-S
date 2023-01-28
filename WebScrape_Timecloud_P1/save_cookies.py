import csv
from selenium import webdriver

def save_new_cookies(driver):
    """This saves the cookies in the same CSV file added for loading

    Args:
        driver (WebDriver): The web driver to which the cookies will be added
        
    Returns: 
        webdriver.Chrome: overwriting the current cookies in the CSV file
    """
    
    # Get all cookies
    cookies = driver.get_cookies()

    # Write the cookies to a CSV file
    with open('cookies.csv', mode='w') as csv_file:
        fieldnames = ['name', 'value', 'path', 'expiry']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for cookie in cookies:
            writer.writerow({'name': cookie['name'], 'value': cookie['value'], 'path': cookie['path']})
    print(f' Cookies loaded: {list(cookie)}')
