# lazy program which automates internship application process, tailored to the concordia compass platform

import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('./chromedriver')
driver.get("https://fas.concordia.ca/adfs/ls/?wa=wsignin1.0&wtrealm=https%3a%2f%2ftakeme2.concordia.ca%2f&wctx=rm%3d0%26id%3d3f97fd49-94b2-4025-9455-5328b74ff1e9%26ru%3d%252findex.html%253fapp%253dcompass&wct=2023-05-14T19%3a25%3a40Z")
driver.maximize_window()
email = driver.find_element(By.ID, "userNameInput")
email.send_keys("INSERT USER HERE")
password = driver.find_element(By.ID, "passwordInput")
password.send_keys("INSERT PASSWORD HERE")
password.send_keys(Keys.ENTER)
time.sleep(5)
driver.get("https://icope.concordia.ca/myAccount/coopjobs.htm")
driver.switch_to.window(driver.window_handles[1])
driver.close()
driver.switch_to.window(driver.window_handles[0])  
time.sleep(1)
program = driver.find_element(By.LINK_TEXT, 'For My Program')
program.click()
search = driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div/div/div/div/div[4]/div[3]/table/thead/tr/th[4]/a")
search.click()
time.sleep(0.1)
i = 1
while i < 101:
    path = "/html/body/main/div[2]/div/div/div/div/div/div/div[4]/div[3]/table/tbody/tr[" + str(i) + "]/td[1]/a[2]"
    apply = driver.find_element(By.XPATH, path)
    apply.click()
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(0.5)
    apply_1 = driver.find_element(By.XPATH, "/html/body/main/div[1]/div/div[2]/div/div[2]/div/button")
    apply_1.click()
    time.sleep(0.1)
    option = driver.find_element(By.NAME, "applyOption")
    option.click()
    time.sleep(0.1)
    package = driver.find_element(By.NAME, "pac")
    package.click()
    time.sleep(0.1)
    submit = driver.find_element(By.XPATH, "/html/body/main/div[3]/div/form/div/div[2]/input")
    submit.click()
    time.sleep(0.1)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(1)
    i += 1
