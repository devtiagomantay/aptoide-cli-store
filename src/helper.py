def get_item(item_name, item_list):
	"""
	Return the item given the item name
	:param item_name: str
	:param item_list: list
	:return: Object Item
	"""
	for i in item_list:
		if i.name == item_name:
			return i
	print('Item not found: ', item_name)
	raise


def get_user(username, users_list):
	"""
	Return the user given the username
	:param username: str
	:param users_list: list
	:return: Object User
	"""
	for i in users_list:
		if i.name == username:
			return i
	print('User not found: ', username)
	raise


def search_app(appname, apps_list):
	"""
	Return the user given the username
	:param appname: str
	:param apps_list: list
	:return: Object App
	"""
	for i in apps_list:
		if i.name == appname:
			return i
	print('App not found: ', appname)
	raise


def get_dev_by_appid(app_id, app_list, dev_list):
	"""
	Return the user given the app_id
	:param app_id: int
	:param app_list: list[App]
	:param dev_list: list[Dev]
	:return: Object Dev
	"""
	dev_id = 0
	for each_app in app_list:
		if each_app.id == app_id:
			dev_id = each_app.dev_id
	for each_dev in dev_list:
		if each_dev.id == dev_id:
			return each_dev

	print('Dev not found for app_id ', app_id)
	raise

