from datetime import datetime


def get_reward(purchase_amount):
	"""
	Get percentage of prices with/without reward
	:param purchase_amount:
	:return: int
	"""
	if purchase_amount < 1:
		return None

	# reward 5% discount
	elif purchase_amount < 10:
		return 0.05

	# reward 10% discount
	elif purchase_amount >= 10:
		return 0.10


def calculate_prices(item, user_id, purchase_list):
	"""
	Calculate the prices and rewards for the user, dev and store
	:param item: Item
	:param user_id: int
	:param purchase_list: list
	:return: dict
	"""
	DEV_SHARE = 0.75
	STORE_SHARE = 0.25
	purchase_amount = get_app_purchases_by_userid(item.app_id, user_id, purchase_list)
	reward = get_reward(purchase_amount)

	final_price = round(item.price, 2)
	dev_total_value = round(final_price * DEV_SHARE, 2)
	store_total_value = round(final_price * STORE_SHARE, 2)

	return {'price': final_price, 'dev': dev_total_value, 'store': store_total_value, 'rewards': reward}


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


def create_transaction(purchase_info):
	from models import Transaction
	"""
	Creates the purchase
	:param pi: dict
	:return: obj class Purchase
	"""
	try:
		# app = search_app(pi['app'], data['apps'])
		# item = get_item(pi['item'], data['items'])
		# user = get_user(pi['user'], data['users'])
		# dev = get_dev_by_appid(app.id, data['apps'], data['devs'])
		# store = data['store']
		# values = calculate_prices(item, dev.id, data['purchases'])
		#
		# user.purchase_app(values['price'])
		# store.sell_item(values['store'])
		# dev.sell_item(values['dev'])

		purchase = Transaction(id=purchase_info['purchase_total'] + 1,
							   item_id=purchase_info['item_id'],
							   app_id=purchase_info['app_id'],
							   user_id=purchase_info['user_id'],
							   value=purchase_info['purchase_values']['price'],
							   date=datetime.now(),
							   reward=purchase_info['purchase_values']['rewards'],
							   store=purchase_info['store'])
		return purchase

	except Exception as e:
		# log error
		pass


def create_reward_purchase(purchase_info):
	from models import Transaction
	"""
	Creates the reward purchase
	:param pi: dict
	:return: obj class Purchase
	"""
	try:
		# app = search_app(pi['app'], data['apps'])
		# item = get_item(pi['item'], data['items'])
		# user = get_user(pi['user'], data['users'])
		# dev = get_dev_by_appid(app.id, data['apps'], data['devs'])
		# store = data['store']
		# values = calculate_prices(item, dev.id, data['purchases'])
		#
		# user.purchase_app(values['price'])
		# store.sell_item(values['store'])
		# dev.sell_item(values['dev'])

		purchase = Transaction(id=purchase_info['purchase_total'] + 1,
							   item_id=purchase_info['item_id'],
							   app_id=purchase_info['app_id'],
							   user_id=purchase_info['user_id'],
							   value=purchase_info['purchase_values']['price'],
							   date=datetime.now(),
							   reward=purchase_info['purchase_values']['rewards'])
		return purchase

	except Exception as e:
		# log error
		pass


def get_item(item_name, item_list):
	"""
	Return the item given the item name
	:param item_name: str
	:param item_list: list
	:return: Object Item
	"""
	try:
		for i in item_list:
			if i.name == item_name:
				return i
	except Exception:
		print('A problem occur trying to get the item ', item_name)
		raise
	print('Item not found: ', item_name)
	raise


def get_user(username, users_list):
	"""
	Return the user given the username
	:param username: str
	:param users_list: list
	:return: Object User
	"""
	try:
		for i in users_list:
			if i.name == username:
				return i
	except Exception:
		print('A problem occur trying to get the user ', username)
		raise
	print('User not found: ', username)
	raise


def get_app(appname, apps_list):
	"""
	Return the app object given the appname
	:param appname: str
	:param apps_list: list
	:return: Object App
	"""
	try:
		for i in apps_list:
			if i.name == appname:
				return i
	except Exception:
		print('A problem occur trying to search the app ', appname)
		raise
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
	try:
		dev_id = 0
		for each_app in app_list:
			if each_app.id == app_id:
				dev_id = each_app.dev_id
		for each_dev in dev_list:
			if each_dev.id == dev_id:
				return each_dev
	except Exception:
		print('A problem occur trying to get the dev with the appid ', app_id)
		raise
	print('Dev not found for app_id ', app_id)
	raise

