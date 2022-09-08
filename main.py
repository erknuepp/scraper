from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

path = r"C:\WebDrivers\chromedriver.exe"
s=Service(path)

driver = webdriver.Chrome(service=s)
driver.maximize_window()

wait = WebDriverWait(driver, 10)

driver.get('https://odyssey.gwinnettcourts.com/Portal/')       

wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="portlet-29"]/a')))
smart_search_element = driver.find_element(By.XPATH, '//*[@id="portlet-29"]/a')

smart_search_element.click()

driver.quit()