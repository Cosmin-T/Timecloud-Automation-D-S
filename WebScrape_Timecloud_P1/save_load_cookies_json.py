from collections import OrderedDict
from selenium import webdriver
import json

import json

""" def save_new_cookies(driver): """
    """This function gets all the new cookies and saves them in the JSON file

    Args:
        driver (WebDriver): The web driver to which the cookies will be added
    """
    """ # Get all cookies
    cookies = driver.get_cookies()

    # Create a new list to hold the cookie information
    cookie_list = []

    # Iterate through each cookie
    for cookie in cookies:
        # Create a dictionary to hold the name, value, domain, and path
        cookie_dict = OrderedDict()
        cookie_dict['name'] = cookie['name']
        cookie_dict['value'] = cookie['value']
        cookie_dict['domain'] = cookie['domain']
        cookie_dict['path'] = cookie['path']
        cookie_list.append(cookie_dict)
    # Open a file to save the cookies
    with open('cookies.json', 'w') as f:
        # Write the cookies to the JSON file
        json.dump(cookie_list, f, indent=4)
        print(cookie_list)

import json

def load_cookies(driver): """
    """This function loads the cookies from the json file and adds them to the specified web driver.

    Args:
        driver (WebDriver): The web driver to which the cookies will be added.
    """
    """ #Open the json file
    try:
        with open('cookies.json', 'r') as f:
            #Load the JSON file
            cookies = json.load(f)
            
            #Select the dict in the JSON file and add in the webdriver
            for cookie in cookies:
                driver.add_cookie(cookie)
                print(f'Added cookie: {cookie["name"]}')
    except Exception:
        pass """