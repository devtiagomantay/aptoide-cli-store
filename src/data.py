from src.models import *


def create_dummy_data():
	store = Store(id=1, name='Aptoide', balance=10.00)
	users_list_ = [User(id=1, name='Bob', balance=100.00), User(id=2, name='Bill', balance=10.00)]
	app_list_ = [App(id=1, dev_id=1, name='Chess'), App(id=2, dev_id=1, name='Notepad')]
	item_list_ = [Item(id=1, app_id=1, name='Premium', price=2.00), Item(id=2, app_id=2, name='Basic', price=1.00)]
	dev_list_ = [Dev(id=1, name='Billy', balance=10.00), Dev(id=2, name='Joe', balance=10.00)]

	return {'users': users_list_, 'apps': app_list_, 'items': item_list_, 'devs': dev_list_, 'store': store,
			'transactions': []}
