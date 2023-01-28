import csv
from selenium import webdriver
import logging

logging.basicConfig(filename = 'error.handling.log', format = '‘%(asctime)s %(message)s' , level = logging.DEBUG)

def load_cookies(driver):
    """Loads the cookies from the CSV file

    Args:
        driver (WebDriver): The web driver to which the cookies will be added.

    Returns:
        webdriver.Chrome: with added cookies from the CSV file
    """
    # Open the CSV file with the cookies
    with open('cookies.csv') as csv_file:
        reader = csv.DictReader(csv_file)
        # Iterate through the rows in the CSV file
        for row in reader:
            # Use Selenium's add_cookie method to add each cookie to the driver
            driver.add_cookie({
                'name': row['name'],
                'value': row['value'],
                'path': row['path']
            })
    print(f'cookies loaded: {list(row)}')