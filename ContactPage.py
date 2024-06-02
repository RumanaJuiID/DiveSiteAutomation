from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


# Setting up Chrome webdriver
service = Service('/Users/rumana.jui/PycharmProjects/DiveSiteAutomation/chromedriver')
driver = webdriver.Chrome(service=service)


# Asking for input values from the console
def get_user_inputs():
    fullName = input("Enter Full Name: ")
    email = input("Enter Email: ")
    phone = input("Enter Phone: ")
    company = input("Enter Company: ")
    job = input("Enter your Job title: ")
    return fullName, email, phone, company, job

time.sleep(5)

# Getting the input values from the user
fullName, email, phone, company, job = get_user_inputs()

# Loading the web page
driver.get('https://qa3.hrdive.com/selfservice/event-listings/contact')

time.sleep(2)

# Setting up the input values
driver.find_element(By.ID, 'submitterName').send_keys(fullName)
driver.find_element(By.NAME, 'email').send_keys(email)
driver.find_element(By.NAME, 'phone').send_keys(phone)
driver.find_element(By.NAME, 'company').send_keys(company)
driver.find_element(By.NAME, 'submitterTitle').send_keys(job)

# Clicking the "Get Started" button
get_started_button = driver.find_element(By.NAME, 'submitCreate')
get_started_button.click()

# Allow some time to see the result
time.sleep(5)

# Close the browser
driver.quit()
