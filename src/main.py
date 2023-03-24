from data import create_dummy_data
from logic import create_transaction, get_app, get_item, get_user, get_dev_by_appid, calculate_prices


def get_user_input():
	"""
	Function to get the user input and validate
	:return: dict
	"""
	input_ = input('Enter the app, item and user: ')
	input_list = input_.split()
	if len(input_list) != 3:
		print('Invalid values')
		raise

	return {'app': input_list[0], 'item': input_list[1], 'user': input_list[2]}


def float_formatter(x):
	return "%.2f" % x


def print_purchase_transaction(purchase, app, item, dev, user, purchase_values):
	brackets = '{'
	brackets_end = '}'
	print(f'PURCHASE TRANSACTION => id: {purchase.id}; app: {app.name}; item: {item.name}; '
		  f'amount: €{float_formatter(purchase_values["price"])}; '
		  f'sender: {user.name}; '
		  f'receivers: {brackets}{dev.name}: €{float_formatter(purchase_values["dev"])}; '
		  f'{store.name}: €{float_formatter(purchase_values["store"])}{brackets_end}')


def print_balance(info):
	output = f'BALANCE => {info["user"].name}: €{float_formatter(info["user"].balance)}; '
	if 'dev' in info.keys():
		output += f'{info["dev"].name}: €{float_formatter(info["dev"].balance)}; '
	output += f'{info["store"].name}: €{float_formatter(info["store"].balance)}'
	print(output)


def print_reward_transaction(info):
	brackets = '{'
	brackets_end = '}'
	print(f'REWARD TRANSACTION => id: {info["reward_transaction"].id}; '
		  f'amount: €{float_formatter(info["reward_transaction"].value)}; '
		  f'sender: {info["reward_transaction"].store}; '
		  f'receivers: {brackets}{info["user"].name}: €{float_formatter(info["reward_transaction"].value)}{brackets_end}')


if __name__ == '__main__':
	data_ = create_dummy_data()
	while 1:
		try:
			user_input = get_user_input()

			app = get_app(user_input['app'], data_['apps'])
			item = get_item(user_input['item'], data_['items'])
			user = get_user(user_input['user'], data_['users'])
			dev = get_dev_by_appid(app.id, data_['apps'], data_['devs'])
			store = data_['store']

			purchase_values = calculate_prices(item, dev.id, data_['transactions'])

			user.purchase_app(purchase_values['price'])
			store.sell_item(purchase_values['store'])
			dev.sell_item(purchase_values['dev'])

			pi = {'purchase_values': purchase_values, 'purchase_total': len(data_['transactions']), 'item_id': item.id,
				  'app_id': app.id, 'user_id': user.id, 'store': store.name}

			purchase = create_transaction(pi)
			data_['transactions'].append(purchase)

			print_purchase_transaction(purchase, app, item, dev, user, purchase_values)
			print_balance({'user': user, 'dev': dev, 'store': store})

			if purchase_values['rewards']:
				discount = purchase_values['price'] * purchase_values['rewards']
				user.get_reward(discount)
				store.give_reward(discount)
				purchase_values['price'] = discount
				pi = {'purchase_values': purchase_values, 'purchase_total': len(data_['transactions']),
					  'item_id': item.id,
					  'app_id': app.id, 'user_id': user.id, 'store': store.name}

				reward_transaction = create_transaction(pi)
				data_['transactions'].append(reward_transaction)

			if purchase_values['rewards']:
				print('#########')
				print_reward_transaction({'transaction': reward_transaction, 'user': user})
				print_balance({'user': user, 'store': store})

		except Exception as e:
			print(e)
			continue
