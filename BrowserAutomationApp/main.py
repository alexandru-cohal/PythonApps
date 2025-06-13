from dotenv import load_dotenv
load_dotenv("../.env")

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
import time


class WebAutomation:
    def __init__(self):
        """ Define the driver, options and service """

        chrome_options = Options()
        chrome_options.add_argument("--disable-search-engine-choice-screen")

        downloads_path = os.getcwd()
        prefs = {"download.default_directory": downloads_path}
        chrome_options.add_experimental_option("prefs", prefs)

        service = Service("chromedriver-win64/chromedriver.exe")
        self.driver = webdriver.Chrome(service=service, options=chrome_options)

        # Load the webpage
        self.driver.get("https://demoqa.com/login")

    def login(self, username, password):
        """ Execute the login """

        # Locate the UserName and Password textboxes and Login button
        username_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "userName")))
        password_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "password")))
        login_button = self.driver.find_element(By.ID, "login")

        # Fill in UserName and Password textboxes and click on the Login button
        username_field.send_keys(username)
        password_field.send_keys(password)
        # Use execute_script method instead of click() in order to avoid clicking on an advertisement
        self.driver.execute_script("arguments[0].click();", login_button)

    def fill_form(self, full_name, email, current_address, permanent_address):
        """ Fill in the form and submit it """

        # Locate and click on the Elements dropdown and Text Box option
        elements = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="app"]/div/div/div/div[1]/div/div/div[1]/span/div/div[1]')))
        elements.click()
        text_box = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'item-0')))
        text_box.click()

        # Locate the form fields
        full_name_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "userName")))
        email_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "userEmail")))
        current_address_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "currentAddress")))
        permanent_address_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "permanentAddress")))
        submit_button = self.driver.find_element(By.ID, "submit")

        # Fill in the form fields
        full_name_field.send_keys(full_name)
        email_field.send_keys(email)
        current_address_field.send_keys(current_address)
        permanent_address_field.send_keys(permanent_address)
        self.driver.execute_script("arguments[0].click();", submit_button)

    def download(self):
        """ Download a file """

        # Locate and click on the Upload and Download option and the Download button
        upload_download = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'item-7')))
        upload_download.click()
        download_button = self.driver.find_element(By.ID, "downloadButton")
        self.driver.execute_script("arguments[0].click();", download_button)

    def close(self):
        """ Quit the driver """

        self.driver.quit()


if __name__ == "__main__":
    web_automation = WebAutomation()
    web_automation.login(username=os.getenv("DEMOQA_USER"),
                         password=os.getenv("DEMOQA_PASS"))
    web_automation.fill_form(full_name="John Smith",
                             email="john@gmail.com",
                             current_address="John Street 100, New York, USA",
                             permanent_address="John Street 100, New York, USA")
    web_automation.download()
    time.sleep(5)
    web_automation.close()