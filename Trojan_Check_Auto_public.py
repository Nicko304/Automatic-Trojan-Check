import os
import selectors
import time
from selenium import webdriver
from getpass import getpass
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

start = time.time()

SSO_TrojanCheck = 'https://trojancheck.usc.edu/login'

#/////////// REQUIRED SETUP ///////////
driver = webdriver.Chrome("__________________________") # Fill in with appropriate path to your chromedriver file
# driver = webdriver.Chrome("C:\\Users\\Nicholas Schumacher\\Desktop\\WebDrivers\\chromedriver.exe") # Example with my computer (Windows)
#//////////////////////////////////////

driver.maximize_window()
driver.get(SSO_TrojanCheck)

wait = WebDriverWait(driver, 50)
wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Log in with your USC NetID"]'))).click()


# Clicks "Continue" > "Begin" > "Start screening"
wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@class="mat-focus-indicator submit-button btn-next mat-button mat-button-base mat-accent"]'))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@class="mat-focus-indicator mat-flat-button mat-button-base btn-begin-assessment"]'))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Start screening']"))).click()

# Question regarding isolation due to COVID-19
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@name,'wasDiagnosed')]//div[text()='No']"))).click() # Clicks "no" on Are you currently required to isolate* due to a COVID-19 infection?
# wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@id="mat-button-toggle-2-button"]'))).click() Also worked but risky to use since the number can change
wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Next']"))).click() # "Next" button

# Rest of questions and "Next" button for this page
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@name,'hasFever')]//div[text()='No']"))).click() # Clicks "no" on Chills or Fever of 100 degrees or higher
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@name,'hasLostSenses')]//div[text()='No']"))).click() # Clicks "no" on Loss of Taste or Smell
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@name,'hasSoreness')]//div[text()='No']"))).click() # Clicks "no" on Muscle Soreness or Headaches or Fatigue
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@name,'hasFluSymptoms')]//div[text()='No']"))).click() # Clicks "no" on Cough or Runny Nose or Sore Throat or Congestion
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@name,'hasBreathingSymptoms')]//div[text()='No']"))).click() # Clicks "no" on Difficulty Breathing or Shortness of Breath
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@name,'hasConjunctivitis')]//div[text()='No']"))).click() # Clicks "no" on Conjunctivitis (inflammation of eye including redness, itching and tearing) ALONG WITH feeling feverish
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@name,'hasOtherSymptoms')]//div[text()='No']"))).click() # Clicks "no" on GI symptoms such as Abdominal Pain or Diarrhea or Nausea or Vomiting
wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Next']"))).click() # "Next" button

# Attest response and submit page
wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@class="mat-checkbox-inner-container"]'))).click() # Clicks checkbox attesting that answers are correct
wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Submit']"))).click() # Clicks the "Submit" button and finishes Trojan Check


# time.sleep(20)
# driver.quit()