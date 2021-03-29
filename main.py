import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
driver.get("http://facebook.com")

driver.find_element_by_id("email").send_keys("0680656829")  # input поле логина
driver.find_element_by_id("pass").send_keys("cxzdsaewq321")  # input поле пароля 
driver.find_element_by_xpath("//*[contains(@id,'u_0_c_')]").click()
driver.find_element_by_xpath("//*[contains(@id,'u_0_d_')]").click()

element = driver.find_element_by_xpath("//*[contains(@id,'mount_0_0_')]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[3]/div/div/div[1]/div/div[2]/div/div[2]/div/ul")
friends = element.find_elements_by_tag_name("li")

links_to_friends = []
for i in range(10):
	friends[i].click()
	time.sleep(2)
	driver.find_element_by_xpath("//*[contains(@id,'mount_0_0_')]/div/div[1]/div/div[5]/div/div[1]/div[1]/div[1]/div/div/div/div/div/div/div[1]/div/div/div[1]/span/div/div[1]").click()
	time.sleep(1)
	button_view_profile = driver.find_element_by_xpath("//*[contains(@id,'mount_0_0_')]/div/div[1]/div/div[5]/div/div[1]/div[1]/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div/div[1]/div/a[2]")
	links_to_friends.append(button_view_profile.get_attribute("href"))
	driver.find_element_by_xpath("//*[contains(@id,'mount_0_0_')]/div/div[1]/div/div[5]/div/div[1]/div[1]/div[1]/div/div/div/div/div/div/div[1]/div/div/div[3]/span[4]/div").click()

print(links_to_friends)