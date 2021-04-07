# list of correct log levels
TRUE_LOG_LEVELS = [
	'critical', 
	'error', 
	'warning', 
	'info', 
	'debug', 
]

# list of correct file modes
TRUE_FILE_MODES = [
	'r',
	'w',
	'x',
	'a',
	'b',
	't',
	'+',
]

FRIEND_DATA_ATTRIBUTES = [
	'NAME',
	'URL',
]

DATE_FORMAT_FOR_LOGGER = '%Y-%m-%d %H:%M:%S'

MESSAGE_FORMAT_FOR_LOGGER = '%(asctime)s.%(msecs)03d %(name)s %(levelname)s: %(message)s'

# format for displaying the list of friends in the console
FORMAT_DISPLAYING_FRIENDS = '{:<25}{:<25}'

MY_PROFILE_XPATH = "//*[contains(@id,'mount_0_0_')]/div/div[1]/div/div[2]/div[4]/div[1]/div[4]"

COUNTER_FRIENDS_XPATH = "//*[contains(@id,'mount_0_0_')]/div/div[1]/div/div[3]/div/div/div[2]/div[1]/div/div/div[4]/div[2]/div/div[1]/div[2]/div/div[3]/div/div/div/div/div[1]/div/div/div/div[2]/span/span"

FRIENDS_BUTTON_DOM_XPATH = "//*[contains(@id,'mount_0_0_')]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[3]"
FRIEND_LIST_DOM_XPATH = "//*[contains(@id,'mount_0_0_')]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div/div/div/div/div/div[3]"
FRIEND_UPLOAD_TAG_CLASSNAME = "rek2kq2y"

FRIEND_CLASSNAME = "//*[contains(@class, 'bp9cbjyn ue3kfks5 pw54ja7n uo3d90p7 l82x9zwi n1f8r23x rq0escxv j83agx80 bi6gxh9e discj3wi hv4rvrfc ihqw7lf3 dati1w0a gfomwglr')]"

SHOW_PASSWORD_BUTTON_XPATH = "//*[contains(@id,'u_0_c_')]"

LOG_IN_BUTTON_XPATH = "//*[contains(@id,'u_0_d_')]"