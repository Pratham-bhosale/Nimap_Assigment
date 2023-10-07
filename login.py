import time

from selenium import webdriver
# from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# options = webdriver.ChromeOptions()
option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
option.add_argument('ignore-certificate-error')
service_obj = Service()
driver = webdriver.Chrome(options= option, service= service_obj)
driver.implicitly_wait(25)
driver.get("https://testffc.nimapinfotech.com/")
driver.find_element(By.XPATH, "//input[@id='mat-input-0']").send_keys("mandarc600@gmail.com")
driver.find_element(By.XPATH, "//input[@id='mat-input-1']").send_keys("12345678")
inp = input("Enter capche = ")
driver.find_element(By.XPATH, "//input[@class='ng-untouched ng-pristine ng-valid']").send_keys(inp)
driver.find_element(By.XPATH, "//button[@id='kt_login_signin_submit']").click()
driver.execute_script("alert('Login Successfully');")
alert = driver.switch_to.alert
alert_text = alert.text
assert "Login Successfully" == alert_text
alert.accept()
driver.find_element(By.XPATH, "//span[normalize-space()='My Customers']").click()
driver.find_element(By.XPATH, "//button[@class='mat-button-mt-4 mat-raised-button mat-button-base mat-primary ng-star-inserted']").click()
# xpath = driver.find_element(By.XPATH, "//div[@id='cdk-overlay-10']")
# driver.switch_to.frame(xpath)
# driver.find_element(By.XPATH, "//div[@id='cdk-overlay-10']//input[@id='mat-input-36']").send_keys("Prathames Bhosle")
# driver.find_element(By.XPATH, "//div[@id='cdk-overlay-10']//button[@mattooltip='Save changes']").click()
element = WebDriverWait(driver, 10).until(EC.p)
element.send_keys("prathamesh")