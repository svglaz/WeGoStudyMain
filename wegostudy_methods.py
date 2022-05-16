import datetime
import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import wegostudy_locators as locators
from selenium.webdriver.support.ui import Select
from selenium.webdriver import Keys

s = Service(executable_path='C:/Automation/Python/wegostudy_main/chromedriver.exe')
driver = webdriver.Chrome(service=s)


def setUp():
    print(f'Launch {locators.app} App')
    print(f'--------------------~*~------------------------')
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get(locators.wegostudy_url)
    if driver.current_url == locators.wegostudy_url and driver.title == locators.wegostudy_home_page_title:
        print(f'{locators.app} App website launched successfully.')
        print(f'{locators.app} Homepage URL: {driver.current_url}, Homepage title: {locators.wegostudy_home_page_title}')
        sleep(0.25)
    else:
        print(f'f{locators.app} did not launch. Check your code or application!')
        print(f'Current URL: {driver.current_url}, Page title: {driver.title}')


def tearDown():
    if driver is not None:
        print(f'-----------------------~*~-------------------------')
        print(f'The test is completed at: {datetime.datetime.now()}')
        sleep(0.25)
        driver.close()
        driver.quit()


def log_in():
    if driver.current_url == locators.wegostudy_url:
        driver.find_element(By.LINK_TEXT, 'LOGIN').click()
        sleep(0.25)

        if driver.find_element(By.XPATH, '//div[contains(@class, "authentication_form")]').is_displayed():
            print(f'Pop up window is displayed.')
            sleep(0.25)
            driver.find_element(By.ID, 'user_email').send_keys(locators.user_email)
            sleep(0.25)
            driver.find_element(By.ID, 'user_password').send_keys(locators.user_password)
            sleep(0.25)
            driver.find_element(By.XPATH, '//input[contains(@value, "SIGN IN")]').click()
            sleep(1.25)

            if driver.current_url == locators.partner_home_page:
               assert driver.find_element(By.XPATH, '//div[contains(text(), "Signed in successfully.")]').is_displayed()
               print(f'Login is successful.')
            else:
                print(f'Login is not successful. Check your code or website and try again.')


def create_new_student():
    assert driver.current_url == locators.partner_home_page
    driver.find_element(By.LINK_TEXT, 'My WeGoStudy').click()
    sleep(0.25)
    driver.find_element(By.LINK_TEXT, 'Students').click()
    sleep(1)
    assert driver.current_url == locators.partner_student_details_page
    assert driver.find_element(By.XPATH, '//h4[contains(text(), "My Students")]').is_displayed()
    driver.find_element(By.LINK_TEXT, 'Create New Student').click()
    sleep(1)

#____________________________User Picture___________________________________

    driver.find_element(By.ID, 'imageUpload').send_keys('C:/Automation/Python/wegostudy_main/upload/StudentImage.png')
    sleep(0.5)

#____________________________Personal Information___________________________

    if driver.current_url == locators.partner_new_student_page:
        assert driver.current_url == locators.partner_new_student_page
        print(f'We are on new student page.')
        driver.find_element(By.ID, 'user_student_detail_attributes_first_name').send_keys(locators.first_name)
        sleep(0.5)
        driver.find_element(By.ID, 'user_student_detail_attributes_middle_name').send_keys(locators.middle_name)
        sleep(0.5)
        driver.find_element(By.ID, 'user_student_detail_attributes_last_name').send_keys(locators.last_name)
        sleep(0.5)
        driver.find_element(By.ID, 'user_student_detail_attributes_preferred_name').send_keys(locators.preferred_name)
        sleep(0.5)
        driver.find_element(By.ID, 'user_student_detail_attributes_birth_date').send_keys(Keys.ENTER)
        sleep(0.5)
        driver.find_element(By.ID, 'user_student_detail_attributes_birth_date').clear()
        sleep(0.5)
        driver.find_element(By.ID, 'user_student_detail_attributes_birth_date').send_keys(locators.date_of_birth)
        sleep(0.5)
        driver.find_element(By.ID, 'user_student_detail_attributes_passport_number').send_keys(locators.passport_number)
        sleep(0.5)
        driver.find_element(By.ID, 'select2-user_student_detail_attributes_country_of_citizenship-container').click()
        sleep(0.5)
        c = random.randint(254, 500)
        driver.find_element(By.XPATH, f"//option[@data-select2-id='{c}']").click()
        sleep(0.5)
        driver.find_element(By.ID, 'phone_number').send_keys(locators.passport_number)
        sleep(0.5)

#_______________________Contact Information_________________________________




setUp()
log_in()
create_new_student()
tearDown()

