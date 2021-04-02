import os
import re
import csv
import datetime as dt

import logging
import configparser

import selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from constants import *
from settings import secret


def setup():
	parameters_set = config_setup()
	logging_setup(
		parameters_set["Path"]["path_to_log"], 
		*parameters_set["LoggingSettings"].values(),
	)

	return parameters_set


def config_setup():
	path_to_config = 'settings/config.ini'
	config = configparser.ConfigParser()
	config.read(path_to_config)

	parameters_set = {}

	try:
		for section in config:
			if section != "DEFAULT":
				parameters_set[section] = {}
			for field in config[section]:
				if section == "LoggingSettings":
					parameters_set[section][field] = config[section][field].lower()
				elif section == "Path":
					parameters_set[section][field] = config[section][field]
				else:
					parameters_set[section][field] = int(config[section][field])
		if not parameters_set:
			raise FileNotFoundError("Config file not found")
	except (ValueError, FileNotFoundError, ) as ex:
		print("Incorrect parameters in the config file or the file is missing at all. " +
			f"Path: {path_to_config}. Ex: {ex}")

		os._exit(0)

	return parameters_set


def logging_setup(path_to_log, log_level, log_filemode):
	if not log_level in TRUE_LOG_LEVELS:
		log_level = 'DEBUG'

	if not log_filemode in TRUE_FILE_MODES:
		log_filemode = 'a'

	path = create_file_path(path_to_log)

	logging.basicConfig(filename=path, 
		level=log_level,
		filemode=log_filemode, 
		format=MESSAGE_FORMAT_FOR_LOGGER,
		datefmt=DATE_FORMAT_FOR_LOGGER)


def workflow(parameters):
	driver = webdriver.Chrome(parameters["Path"]["path_to_driver"])
	driver.maximize_window()
	
	list_friends = parse_friends(driver)

	try:
		path_to_csv = parameters["Path"]["path_to_csv"]
	except KeyError as ex:
		logging.warning("The path to the csv file is missing in the config. Creating a file in the executing directory.")
		path_to_csv = "orders.csv"

	path = create_file_path(path_to_csv)

	logging.debug(f"An attempt to write a list of friends to a csv file. Path: {path}.")
	write_csv(path, list_friends)

	logging.debug(f"An attempt to read a list of friends from a csv file. Path: {path}.")
	read_csv(path)


def log_in_facebook(driver):
	driver.get("http://facebook.com")

	driver.find_element_by_id("email").send_keys(secret.login)
	driver.find_element_by_id("pass").send_keys(secret.password)

	driver.find_element_by_xpath(SHOW_PASSWORD_BUTTON_XPATH).click()
	driver.find_element_by_xpath(LOG_IN_BUTTON_XPATH).click()


def parse_friends(driver):
	list_friends = []
	log_in_facebook(driver)
	go_to_my_profile(driver)
	number_friends = get_number_friends(driver)
	
	driver.get(f'{driver.current_url}&sk=friends')

	list_DOM = get_friend_list_DOM(driver)
	for i in range(number_friends):
		friends = list_DOM.find_elements_by_xpath(FRIEND_CLASSNAME)

		friend_data = {
			"name": friends[i].find_element_by_xpath("div[2]/div[1]").text,
			"url": friends[i].find_element_by_xpath("div/a").get_attribute("href")
		}
		
		list_friends.append(friend_data)

	return list_friends


def go_to_my_profile(driver):
	button_my_profile = WebDriverWait(driver, 10).until(
	EC.presence_of_element_located((By.XPATH, MY_PROFILE_XPATH)))
	button_my_profile.click()


def get_number_friends(driver):
	number_friends_dom = WebDriverWait(driver, 10).until(
	EC.presence_of_element_located((By.XPATH, COUNTER_FRIENDS_XPATH)))

	actions = ActionChains(driver)
	actions.move_to_element(number_friends_dom).perform()

	number_friends = int(number_friends_dom.text.split(": ")[1])

	return number_friends


def get_friend_list_DOM(driver):
	list_DOM = WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.XPATH, FRIEND_LIST_DOM_XPATH)))
	flag = True
	while flag:
		try:
			upload_tag = list_DOM.find_element_by_class_name(FRIEND_UPLOAD_TAG_CLASSNAME)
			actions = ActionChains(driver)
			actions.move_to_element(upload_tag).perform()
		except selenium.common.exceptions.NoSuchElementException:
			flag = False

	return list_DOM


def create_file_path(path):
	pathdir = ''.join(re.findall(r"\w+/", path))
	if pathdir:
		if not os.path.exists(pathdir):
			try:
				os.makedirs(pathdir)
			except OSError as ex:
				logging.warning("Failed to create file in the selected path. " +
					f"Created a file in the executing directory. Path: {path}. Ex: {ex}")
				path = os.path.basename(path)
	return path


def write_csv(filename, list_friends):
	try:
		with open(filename, "w") as f:
			csv_f = csv.writer(f)
			csv_f.writerow(FRIEND_DATA_ATTRIBUTES)

			for friend in list_friends:
				csv_f.writerow(friend.values())
	except OSError as ex:
		logging.error(f"Failed to write data to file. Path: {filename}. Ex: {ex}")
		return 0


def read_csv(filename):
	try:
		with open(filename, "r", newline="") as f:
			csv_f = csv.reader(f)

			for row in csv_f:
				if row:
					print(FORMAT_DISPLAYING_FRIENDS.format(*row))
	except OSError as ex:
		logging.error(f"Failed to read data from file. Path: {filename}. Ex: {ex}")
		return 0


if __name__ == "__main__":
	parameters_set = setup()
	logging.debug("Config and logger setup was successful. " + 
		f"Number of sections from config: {len(parameters_set.keys())}")
	workflow(parameters_set)