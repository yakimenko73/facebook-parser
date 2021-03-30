import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
driver.get("http://facebook.com")

driver.find_element_by_id("email").send_keys("0680656829")  # input поле логина
driver.find_element_by_id("pass").send_keys("cxzdsaewq321")  # input поле пароля 
driver.find_element_by_xpath("//*[contains(@id,'u_0_c_')]").click()
driver.find_element_by_xpath("//*[contains(@id,'u_0_d_')]").click()


for i in range(10):
	print(i)

	# get friends list
	contacts = WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.XPATH, "//*[contains(@id,'mount_0_0_')]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[3]/div/div/div[1]/div/div[2]/div/div[2]/div/ul")))
	time.sleep(3)
	friends = contacts.find_elements_by_tag_name("li")

	friends[i].click()

	# click button friend info
	element = WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.XPATH, "//*[contains(@id,'mount_0_0_')]/div/div[1]/div/div[5]/div/div[1]/div[1]/div[1]/div/div/div/div/div/div/div[1]/div/div/div[1]/span/div/div[1]")))
	element.click()

	button_view_profile = WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.XPATH, "//*[contains(@id,'mount_0_0_')]/div/div[1]/div/div[5]/div/div[1]/div[1]/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div/div[1]/div/a[2]")))
	time.sleep(3)
	driver.get(button_view_profile.get_attribute("href"))

	# remove profile frame
	button_view_profile = WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.XPATH, "//*[contains(@id,'mount_0_0_')]/div/div[1]/div/div[5]/div/div[1]/div[1]/div[1]/div/div/div/div/div/div/div[1]/div/div/div[3]/span[4]/div")))

	driver.back()