from time import sleep
import getpass
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#Define Driver
def create_driver():
    driverOptions = webdriver.ChromeOptions()
    driverOptions.add_experimental_option("excludeSwitches", ["enable-logging"])
    return webdriver.Chrome(executable_path=r"B:\SeleniumDrivers\chromedriver.exe", options=driverOptions)

#Open Discord
driver = create_driver()
driver.get("https://discord.com/login")


driver.implicitly_wait(5)

#Email or Phone number input
emailOrPhone = driver.find_element_by_css_selector(
    'input[aria-label="Email or Phone Number"]'
)
userInputOfEmailOrPhone = input("What is your email or phone number: ") 
emailOrPhone.send_keys(userInputOfEmailOrPhone)

#Password input
passwordField = driver.find_element_by_css_selector(
    'input[aria-label="Password"]'
)
userInputOfPassword = getpass.getpass("Password: ")
passwordField.send_keys(userInputOfPassword)

#Press login button
loginButton = driver.find_element_by_css_selector(
    'button[type="submit"]'
)
loginButton.click()

#Wait to login
sleep(2)

#Go to the person who is going to be spammed
whoToSpam = input("Who would you like to spam? : ") 
whoToSpamButton = driver.find_element_by_css_selector(
    f'a[aria-label*="{whoToSpam} (direct message)"]'
)
whoToSpamButton.click()

#Take in messages & spam (with 5 seconds between each one)
#The user can also enter nothing in for one or both fields to select a new person
inputTextBox = driver.find_element_by_css_selector(
    f'div[aria-label="Message @{whoToSpam}"]'
)

while True:

    whatToSpam = input("What would you like to spam? : ")
    howManyTimes = input("How many times would you like to send that? : ")
    if len(whatToSpam) == 0 or len(howManyTimes) == 0 or int(howManyTimes) <= 0:
        whoToSpam = input("Who would you like to spam? : ") 
        try:
            whoToSpamButton = driver.find_element_by_css_selector(
                f'a[aria-label*="{whoToSpam} (direct message)"]'
            )
            whoToSpamButton.click()
        except:
            break

        #Take in messages & spam
        inputTextBox = driver.find_element_by_css_selector(
            f'div[aria-label="Message @{whoToSpam}"]'
        )
        continue
        
    howManyTimes = int(howManyTimes)
    howManyHaveBeenSent = 0
    for _ in range(howManyTimes):
        sleep(5)
        # if howManyHaveBeenSent % 5 == 0:
        #     sleep(1.5)
        inputTextBox.send_keys(whatToSpam)
        inputTextBox.send_keys(Keys.ENTER)
        howManyHaveBeenSent += 1

driver.quit()