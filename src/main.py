from data import create_dummy_data
from logic import create_transaction, get_app, get_item, get_user, get_dev_by_appid, calculate_prices, \
	get_reward_in_euros
from helper import print_balance, print_reward_transaction, print_purchase_transaction, get_user_input


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

			purchase_values = calculate_prices(item, user.id, data_['transactions'])

			user.purchase_app(purchase_values['price'])
			store.sell_item(purchase_values['store'])
			dev.sell_item(purchase_values['dev'])

			transaction_info = {'purchase_values': purchase_values, 'purchase_total': len(data_['transactions']),
								'item_id': item.id,
								'app_id': app.id, 'user_id': user.id, 'store': store.name}

			transaction = create_transaction(transaction_info)

			# store the transaction
			data_['transactions'].append(transaction)

			print_purchase_transaction(transaction, app.name, item.name, dev.name, user.name, store.name, purchase_values)
			print_balance({'user': user, 'dev': dev, 'store': store})

			if purchase_values['rewards']:
				reward = get_reward_in_euros(purchase_values)
				user.get_reward(reward)
				store.give_reward(reward)
				purchase_values['price'] = reward
				transaction_info = {'purchase_values': purchase_values, 'purchase_total': len(data_['transactions']),
									'item_id': item.id, 'app_id': app.id, 'user_id': user.id, 'store': store.name}

				reward_transaction = create_transaction(transaction_info)
				# store the reward transaction
				data_['transactions'].append(reward_transaction)

				print_reward_transaction(reward_transaction=reward_transaction, user=user)
				print_balance({'user': user, 'store': store})

		except Exception as e:
			continue
