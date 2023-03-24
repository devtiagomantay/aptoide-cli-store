import pytest
from src.data import create_dummy_data
from src.models import *


class TestData:
	def test_create_dummy_data(self):
		store = Store(id=1, name='Aptoide', balance=10.00)
		users_list_ = [User(id=1, name='Bob', balance=100.00), User(id=2, name='Bill', balance=10.00)]
		app_list_ = [App(id=1, dev_id=1, name='Chess'), App(id=2, dev_id=1, name='Notepad')]
		item_list_ = [Item(id=1, app_id=1, name='Premium', price=2.00), Item(id=2, app_id=2, name='Basic', price=1.00)]
		dev_list_ = [Dev(id=1, name='Billy', balance=10.00), Dev(id=2, name='Joe', balance=10.00)]
		mock = {'users': users_list_, 'apps': app_list_, 'items': item_list_, 'devs': dev_list_, 'store': store,
			'transactions': []}
		output = create_dummy_data()

		assert mock == output

