def get_item(item, item_list):
	"""
	Return the item given the item name
	:param item: str
	:param item_list: list
	:return: float
	"""
	for i in item_list:
		if i.name == item:
			return i
	print('Item not found: ', item)
	raise


def get_user(username, users_list):
	"""
	Return the user given the username
	:param username: str
	:param users_list: list
	:return: float
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
	:return: float
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
	:return: float
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


def get_app_purchases_by_userid(app_id, user_id, purchase_list):
	"""
	Return the user given the app_id
	:param app_id: int
	:param user_id: int
	:param purchase_list: list
	:return: float
	"""
	count = 0
	for i in purchase_list:
		if i.app_id == app_id and i.user_id == user_id:
			count += 1

	return count
