def get_percentage(purchase_amount):
	"""
	Get percentage of prices with/without reward
	:param purchase_amount:
	:return: int
	"""
	if purchase_amount < 1:
		return 100

	# reward 5% discount
	elif purchase_amount < 10:
		return 95

	# reward 10% discount
	elif purchase_amount >= 10:
		return 90


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

	# find purchases of the user
	purchase_amount = get_app_purchases_by_userid(item.app_id, user_id, purchase_list)
	final_price = 0
	reward = 0
	percentage = get_percentage(purchase_amount)

	final_price = round(item.price * percentage/100, 2)
	dev_total_value = round(final_price * DEV_SHARE, 2)
	store_total_value = round(final_price * STORE_SHARE, 2)
	reward = percentage if percentage < 100 else None

	return {'price': final_price, 'dev': dev_total_value, 'store': store_total_value, 'rewards': reward}
