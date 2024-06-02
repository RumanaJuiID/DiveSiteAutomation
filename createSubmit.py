from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Set up Chrome webdriver
service = Service('/Users/rumana.jui/PycharmProjects/DiveSiteAutomation/chromedriver')
driver = webdriver.Chrome(service=service)

# Function to ask for input values from the console
def get_user_inputs():
    event_name = input("Enter Event Name: ")
    event_type = input("Enter Event Type: ")
    event_description = input("Enter Event Description: ")
    event_date = input("Enter Event Date (YYYY-MM-DD): ")
    event_time = input("Enter Event Time (HH:MM): ")
    event_duration = input("Enter Event Duration: ")
    event_location = input("Enter Event Location: ")
    event_organizer_name = input("Enter Event Organizer Name: ")
    event_organizer_email = input("Enter Event Organizer Email: ")
    event_organizer_phone = input("Enter Event Organizer Phone: ")
    event_sponsor = input("Enter Event Sponsor: ")
    return (event_name, event_type, event_description, event_date, event_time, event_duration,
            event_location, event_organizer_name, event_organizer_email, event_organizer_phone, event_sponsor)

# Get the input values from the user
(event_name, event_type, event_description, event_date, event_time, event_duration, event_location,
 event_organizer_name, event_organizer_email, event_organizer_phone, event_sponsor) = get_user_inputs()

# Load the web page
driver.get('https://qa3.hrdive.com/selfservice/event-listings/fdb9fcd6-2266-40a5-baa9-01e900dc0e16/details')

# Allow some time for the page to load
time.sleep(2)

# Set the input values
driver.find_element(By.NAME, 'title').send_keys(event_name)
driver.find_element(By.NAME, 'eventType').send_keys(event_type)
driver.find_element(By.NAME, 'teaser').send_keys(event_description)
driver.find_element(By.NAME, 'event_date').send_keys(event_date)
driver.find_element(By.NAME, 'event_time').send_keys(event_time)
driver.find_element(By.NAME, 'event_duration').send_keys(event_duration)
driver.find_element(By.NAME, 'event_location').send_keys(event_location)
driver.find_element(By.NAME, 'event_organizer_name').send_keys(event_organizer_name)
driver.find_element(By.NAME, 'event_organizer_email').send_keys(event_organizer_email)
driver.find_element(By.NAME, 'event_organizer_phone').send_keys(event_organizer_phone)
driver.find_element(By.NAME, 'event_sponsor').send_keys(event_sponsor)

# Click the "Get Started" button
get_started_button = driver.find_element(By.XPATH, '//button[text()="Continue to checkout"]')
get_started_button.click()

# Allow some time to see the result
time.sleep(5)

# Close the browser
driver.quit()
