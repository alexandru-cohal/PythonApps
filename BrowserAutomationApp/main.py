from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os

# Define driver, options and service
chrome_options = Options()
chrome_options.add_argument("--disable-search-engine-choice-screen")

downloads_path = os.getcwd()
prefs = {"download.default_directory": downloads_path}
chrome_options.add_experimental_option("prefs", prefs)

service = Service("chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)

# Load the webpage
driver.get("https://demoqa.com/login")

# Locate the username and password textboxes and login button
username_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "userName")))
password_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "password")))
login_button = driver.find_element(By.ID, "login")

# Fill in username and password and click on the login button
username_field.send_keys("alexc")
password_field.send_keys("PythonCourse2025!")
# Use execute_script method instead of click() in order to avoid clicking on an advertisement
driver.execute_script("arguments[0].click();", login_button)

# Locate the Elements dropdown and Text Box  option
elements = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div/div[1]/div/div/div[1]/span/div/div[1]')))
elements.click()
text_box = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'item-0')))
text_box.click()

# Locate the form fields
full_name_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "userName")))
email_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "userEmail")))
current_address_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "currentAddress")))
permanent_address_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "permanentAddress")))
submit_button = driver.find_element(By.ID, "submit")

# Fill in the form fields
full_name_field.send_keys("John Smith")
email_field.send_keys("john@gmail.com")
current_address_field.send_keys("John Street 100, New York, USA")
permanent_address_field.send_keys("John Street 100, New York, USA")
driver.execute_script("arguments[0].click();", submit_button)

# Locate the Upload and Download section and the Download button
upload_download = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'item-7')))
upload_download.click()
download_button = driver.find_element(By.ID, "downloadButton")
driver.execute_script("arguments[0].click();", download_button)

input("Press Enter to close the browser")
driver.quit()