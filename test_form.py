from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("file:C:\\Users\\parth\\Downloads\\SEM 6\\DevOps\\Symbi Form\\index.html")

time.sleep(2)

driver.find_element(By.ID, "name").send_keys("Parthiv Abhani")
driver.find_element(By.ID, "email").send_keys("parthiv@email.com")
driver.find_element(By.ID, "phone").send_keys("9876543210")

course = driver.find_element(By.ID, "course")
course.send_keys("BTech CSE")

driver.find_element(By.ID, "address").send_keys("Nagpur Maharashtra")

driver.find_element(By.ID, "submitBtn").click()

time.sleep(3)

print("Form test completed successfully")

driver.quit()