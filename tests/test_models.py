import pytest
from src.models import Dev, User, Store


class TestDev:
	def test_sell_item(self):
		dev = Dev(id=1, name='Bob', balance=10.0)
		dev.sell_item(2.0)
		assert dev.balance == 12.0


class TestUser:
	def test_purchase_app(self):
		user = User(id=1, name='Larry', balance=6.20)
		user.purchase_app(2.0)
		assert user.balance == 4.20

	def test_purchase_app__no_founds(self):
		with pytest.raises(RuntimeError):
			user = User(id=1, name='Ted', balance=1.20)
			user.purchase_app(2.0)

	def test_get_reward(self):
		user = User(id=1, name='Bill', balance=5.40)
		user.get_reward(0.60)
		assert user.balance == 6.0


class TestStore:
	def test_sell_item(self):
		store = Store(id=1, name='Aptoide', balance=100.00)
		store.sell_item(4)
		assert store.balance == 104.00

	def test_give_reward(self):
		store = Store(id=1, name='Aptoide', balance=100.00)
		store.give_reward(1.50)
		assert store.balance == 98.50

	def test_give_reward__no_founds(self):
		with pytest.raises(RuntimeError):
			store = Store(id=1, name='Aptoide', balance=1.20)
			store.give_reward(2.0)
