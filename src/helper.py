def formatter(x):
	return "%.2f" % x


def print_purchase_transaction(transaction, appname, item_name, dev_name, username, store_name, purchase_values):
	print(f'PURCHASE TRANSACTION => id: {transaction.id}; app: {appname}; item: {item_name}; '
		  f'amount: €{formatter(purchase_values["price"])}; '
		  f'sender: {username}; '
		  f'receivers: {{{dev_name}: €{formatter(purchase_values["dev"])}; '
		  f'{store_name}: €{formatter(purchase_values["store"])}}}')


def print_balance(info):
	output = f'BALANCE => {info["user"].name}: €{formatter(info["user"].balance)}; '
	if 'dev' in info.keys():
		output += f'{info["dev"].name}: €{formatter(info["dev"].balance)}; '
	output += f'{info["store"].name}: €{formatter(info["store"].balance)}\n'
	print(output)


def print_reward_transaction(reward_transaction, user):
	print('#########')
	print(f'REWARD TRANSACTION => id: {reward_transaction.id}; '
		  f'amount: €{formatter(reward_transaction.value)}; '
		  f'sender: {reward_transaction.store}; '
		  f'receivers: {{{user.name}: €{formatter(reward_transaction.value)}}}')


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