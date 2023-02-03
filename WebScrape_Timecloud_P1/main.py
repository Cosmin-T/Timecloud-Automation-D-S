# __main__ if statement for launchctl automation using plist
if __name__ == "__main__":

    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions as EC
    import time
    from initialize_driver import initialize_webdriver
    from load_cookies import load_cookies
    from login_page import login
    from send_email import send_email
    from selenium.common.exceptions import NoSuchElementException
    from verify_clock_btn import check_xpath
    from add_code import add_code
    from save_cookies import save_new_cookies
    import logging
    import schedule


    # Variables for ease of access
    url = 'https://secure3.entertimeonline.com/ta/DSGlobal.login?rnd=SIA&%40rtm=1#time/timeoff/editRequest'
    driver = initialize_webdriver(url)
    username = 'CosminTurculeanu'
    password = 'Holocaust00@@'
    clock_btn = '//*[@id="clock_punch"]/div/div/ul/li[1]/div/button'
    user_g = 'cosmin.turculeanu@dandsltd.com'
    password_g = 'Holocaust0@@@'
    imap_url = 'imap.gmail.com'
    clocked_in = False
    logging.basicConfig(filename = 'error.handling.log', format = '‘%(asctime)s %(message)s' , level = logging.DEBUG)

    # Loading cookies from csv file
    load_cookies(driver)

    # Loging in the page & pass clock button if cookies are not available
    try:
        login(driver, username, password)
        logging.info('Login successful!')
    except Exception as e:
        logging.warning(f'An error occurred while logging in: {e}', exec_info = True)

    # If statmenet where it checks the clockin button if the cookies are good
    if check_xpath(clock_btn, driver):
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="clock_punch"]/div/div/ul/li[1]/div/button'))).click()
        try:
            logging.info('Clocked in successfully')
        except Exception as e:
            logging.warning(f'An error occured while verifying if clockin button exists: {e}', exec_info = True)
        clocked_in = True
        time.sleep(15) # Wait 15 seconds for page to load
    else:
        # Prints error message if not found, sends email, gets code, copies code, logs in, clocks in/out and saves new cookies.
        try:
            logging.info('Clockin button not found, passing')
            send_email(driver)
            logging.info('Sent email successfully')
            time.sleep(5) # Wait 5 seconds for emails to be sent
            add_code(driver)
            logging.info('Copying code into driver')
            time.sleep(10) # Wait 10 seconds for page to load
            driver.refresh()
            time.sleep(5) # Wait 5 seconds for page to load
            logging.info('Cookies saved succesfully')
            save_new_cookies(driver)
            time.sleep(30) # Wait 30 seconds for page to load
        except Exception as e:
            logging.warning(f'An error occured and the passing couldn\'t move forward: {e}', exec_info = True)
            logging.warning(f'An error occured while trying to send email: {e}', exec_info = True)
            logging.warning(f'An error occured while trying to copy code: {e}', exec_info = True)
            logging.warning(f'An error occuerd whil trying ot save cookies: {e}', exc_info = True)