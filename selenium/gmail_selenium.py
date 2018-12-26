"""
This Selenium script sent an email to the list of users who are 
all in the particular group. 

We hope you have already have a group and list of users are already in the 
group

"""

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# Getting chrome browes for the webdriver
driver = webdriver.Chrome()

# Maximize the browser window
driver.maximize_window() 

# Get the GMAIL 
driver.get("https://gmail.com")

# Xpath for email id text box
email_textbox = driver.find_element_by_xpath("//input[@type='email']")
# Sending the user ID to the textbox
email_textbox.send_keys("annapoorani@qxf2.com")
# Sleeping time till the page loads(approx)
time.sleep(2)

# Xpath for the next button
next_button = driver.find_element_by_xpath('//span[@class="RveJvd snByac" and text()="Next"]')
# Click the next button
next_button.click()
# Sleeping time till the page loads
time.sleep(4)

# Xpath for password textbox
password_textbox = driver.find_element_by_xpath("//input[@name='password']")
# Sending the password to the password textbox
password_textbox.send_keys("hoodi2782")

# Xpath for the next button
password_next_button = driver.find_element_by_xpath('//span[@class="RveJvd snByac" and text()="Next"]')
# Click the next button
password_next_button.click()
# Sleeping time till the page loads
time.sleep(5)

"""google_apps = driver.find_element_by_xpath('//a[@aria-label="Google apps"]')
google_apps.click()
contacts = driver.find_element_by_xpath('//span[text()="Contacts"]')
contacts.click()
print ' i found contacts'
action = ActionChains(driver)
action.move_to_element(contacts)
print ' i performed click on contacts'
action.perform()"""

# Xpath for compose button
compose_button = driver.find_element_by_xpath('//div[@class="T-I J-J5-Ji T-I-KE L3"]')
# Click the compose button
compose_button.click()
# Sleep time is little more still it takes time to load
time.sleep(7)

# Xpath for 'to' field  in the compose 
to_field = driver.find_element_by_xpath('//textarea[@name="to"]')
# Send the group name which we want to send an email
to_field.send_keys("test")
# Select the group which is in the autoselect
to_field.send_keys(Keys.ENTER)
time.sleep(5)

# Xpath for 'subject' filed in the compose
subject_field = driver.find_element_by_xpath("//input[@name='subjectbox']")
# Send the subject in the subject field
subject_field.send_keys("Sprint Meeting")

# Xpath for the description of the email filed
mail_field = driver.find_element_by_xpath("//div[@role='textbox']")
# Description of the email
mail_field.send_keys("Meeting at 10 pm.Do not reply for this mail")
time.sleep(5)

# Xpath for the send button
send_button = driver.find_element_by_xpath("//div[@role='button' and text()='Send']")
send_button.click()


