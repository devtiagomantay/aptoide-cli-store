from datetime import datetime
from models import *
from helper import *
from logic import calculate_prices


# global variables
users_list_ = []
app_list_ = []
item_list_ = []
dev_list = []
purchase_list_ = []
store = None


# Data creation
def create_data():
	global store
	global users_list_
	global dev_list
	global app_list_
	global item_list_
	global purchase_list_

	store = Store(id=1, name='Aptoide', balance=10.0)
	user1 = User(id=1, name='Bob', balance=10.0)
	user2 = User(id=2, name='Bill', balance=10.0)
	dev1 = Dev(id=1, name='Billy', balance=10.0)
	dev2 = Dev(id=2, name='Joe', balance=10.0)
	app1 = App(id=1, dev_id=1, name='Chess')
	app2 = App(id=2, dev_id=1, name='Notepad')
	item1 = Item(id=1, app_id=1, name='Premium', price=2.0)
	item2 = Item(id=2, app_id=2, name='Basic', price=1.0)

	users_list_ = [user1, user2]
	app_list_ = [app1, app2]
	item_list_.append(item1)
	item_list_.append(item2)
	dev_list = [dev1, dev2]


def purchase(purchase_info):
	pass


if __name__ == '__main__':
	create_data()
	while 1:
		try:
			user_input = input('Enter the app, item and user: ')
			a = user_input.split()
			# TODO: input validation
			purchase_info = {'app': a[0], 'item': a[1], 'user': a[2]}
			purchase(purchase_info)
			print('\n purchase_list_: ', len(purchase_list_))
			print('Developers:', dev_list)
			print('Store: ', store)
			print('Users:', users_list_)
			print('Purchases: ', purchase_list_)
			print('\n ------------- Press ctrl + C to exit -------------\n\n')
		except Exception as e:
			continue
