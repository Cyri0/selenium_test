from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome("chromedriver.exe")
driver.get("https://nemestamas.hu/13EKC/")
#driver.quit()

time.sleep(2)
reg_button = driver.find_element(By.XPATH, '//*[@id="frame"]/button')
reg_button.click()

time.sleep(2)
username_input = driver.find_element(By.ID, 'username')
username_input.send_keys("Nemes Tamás")
reg_button.click()

li = ["alma", "körte@", "szilva@körte", "szilva.korte.hu"]

for mail in li:
    time.sleep(2)
    email_input = driver.find_element(By.ID, 'email')
    email_input.send_keys(mail)
    reg_button.click()