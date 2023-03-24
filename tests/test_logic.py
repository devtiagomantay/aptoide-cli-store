import pytest
from datetime import datetime
from src.logic import *
from src.models import *


@pytest.fixture()
def item_list():
	item_list = [
		Item(id=1, app_id=1, name='Premium', price=2.0),
		Item(id=3, app_id=2, name='Coin', price=1.0)]
	yield item_list


@pytest.fixture()
def purchase_list():
	# user1 = 1 purchase, user2 = 2 purchases, user3 = 10 purchases on app_id = 1
	purchase_list = [
		Transaction(id=1, item_id=1, app_id=1, user_id=1, value=2.0, date=datetime.now(), reward=None, store='aptoide'),
		Transaction(id=2, item_id=1, app_id=1, user_id=2, value=2.0, date=datetime.now(), reward=None, store='aptoide'),
		Transaction(id=3, item_id=1, app_id=1, user_id=2, value=1.9, date=datetime.now(), reward=95, store='aptoide'),
		Transaction(id=4, item_id=1, app_id=1, user_id=3, value=2.0, date=datetime.now(), reward=None, store='aptoide'),
		Transaction(id=5, item_id=1, app_id=1, user_id=3, value=1.9, date=datetime.now(), reward=95, store='aptoide'),
		Transaction(id=6, item_id=2, app_id=1, user_id=3, value=1.9, date=datetime.now(), reward=95, store='aptoide'),
		Transaction(id=7, item_id=1, app_id=1, user_id=3, value=1.9, date=datetime.now(), reward=95, store='aptoide'),
		Transaction(id=8, item_id=1, app_id=1, user_id=3, value=1.9, date=datetime.now(), reward=95, store='aptoide'),
		Transaction(id=9, item_id=1, app_id=1, user_id=3, value=1.9, date=datetime.now(), reward=95, store='aptoide'),
		Transaction(id=10, item_id=1, app_id=1, user_id=3, value=1.9, date=datetime.now(), reward=95, store='aptoide'),
		Transaction(id=11, item_id=1, app_id=1, user_id=3, value=1.9, date=datetime.now(), reward=95, store='aptoide'),
		Transaction(id=12, item_id=2, app_id=1, user_id=3, value=1.9, date=datetime.now(), reward=95, store='aptoide'),
		Transaction(id=13, item_id=3, app_id=2, user_id=3, value=2.0, date=datetime.now(), reward=None,
					store='aptoide'),
		Transaction(id=14, item_id=2, app_id=1, user_id=3, value=1.8, date=datetime.now(), reward=95, store='aptoide')]
	yield purchase_list


@pytest.fixture()
def item_list():
	item_list = [
		Item(id=1, app_id=1, name='Premium', price=2.0),
		Item(id=3, app_id=2, name='Coin', price=1.0)]
	yield item_list


@pytest.fixture()
def users_list():
	users_list = [
		User(id=1, name='Bob', balance=100.0),
		User(id=2, name='Bill', balance=10.0)]
	yield users_list


@pytest.fixture()
def dev_list():
	dev_list = [
		Dev(id=1, name='Billy', balance=10.0),
		Dev(id=2, name='Joe', balance=10.0)]
	yield dev_list


@pytest.fixture()
def app_list():
	app_list = [
		App(id=1, dev_id=1, name='Chess'),
		App(id=2, dev_id=1, name='Notepad'),
		App(id=3, dev_id=2, name='GTA')]
	yield app_list


class TestGetPercentage:
	def test_get_percentage(self, purchase_list):
		assert get_reward_percentage(purchase_amount=0) is None  # 0%
		assert get_reward_percentage(purchase_amount=1) == 0.05  # 5%
		assert get_reward_percentage(purchase_amount=2) == 0.05  # 5%
		assert get_reward_percentage(purchase_amount=3) == 0.05  # 5%
		assert get_reward_percentage(purchase_amount=4) == 0.05  # 5%
		assert get_reward_percentage(purchase_amount=10) == 0.10  # 10%
		assert get_reward_percentage(purchase_amount=24) == 0.10  # 10%


class TestGetAmountAppPurchasesByUserId:
	def test_get_app_purchases_by_userid(self, purchase_list):
		assert get_amount_app_purchases_by_userid(app_id=1, user_id=1, transaction_list=purchase_list) == 1
		assert get_amount_app_purchases_by_userid(app_id=1, user_id=2, transaction_list=purchase_list) == 2
		assert get_amount_app_purchases_by_userid(app_id=1, user_id=3, transaction_list=purchase_list) == 10
		assert get_amount_app_purchases_by_userid(app_id=2, user_id=1, transaction_list=purchase_list) == 0
		assert get_amount_app_purchases_by_userid(app_id=2, user_id=3, transaction_list=purchase_list) == 1


class TestCalculatePrices:
	def test_calculate_prices_without_discount_app1(self, mocker, item_list, purchase_list):
		mocker.patch("src.logic.get_amount_app_purchases_by_userid", return_value=1)
		mocker.patch("src.logic.get_reward_percentage", return_value=None)
		user_id = 1
		result = {'price': 2.0, 'dev': 1.50, 'store': 0.50, 'rewards': None}
		assert calculate_prices(item_list[0], user_id, purchase_list) == result, "Value should be mocked"

	def test_calculate_prices_without_discount_app2(self, mocker, item_list, purchase_list):
		mocker.patch("src.logic.get_amount_app_purchases_by_userid", return_value=1)
		mocker.patch("src.logic.get_reward_percentage", return_value=None)
		user_id = 3
		result = {'price': 1.0, 'dev': 0.75, 'store': 0.25, 'rewards': None}
		assert calculate_prices(item_list[1], user_id, purchase_list) == result, "Value should be mocked"

	def test_calculate_prices_with_5_percent_reward(self, mocker, item_list, purchase_list):
		mocker.patch("src.logic.get_amount_app_purchases_by_userid", return_value=2)
		mocker.patch("src.logic.get_reward_percentage", return_value=0.05)
		user_id = 2
		result = {'price': 2, 'dev': 1.50, 'store': 0.50, 'rewards': 0.05}
		print(calculate_prices(item_list[0], user_id, purchase_list))
		assert calculate_prices(item_list[0], user_id, purchase_list) == result, "Value should be mocked"

	def test_calculate_prices_with_10_percent_reward(self, mocker, item_list, purchase_list):
		mocker.patch("src.logic.get_amount_app_purchases_by_userid", return_value=10)
		mocker.patch("src.logic.get_reward_percentage", return_value=0.10)
		user_id = 3
		result = {'price': 2, 'dev': 1.50, 'store': 0.50, 'rewards': 0.10}
		assert calculate_prices(item_list[0], user_id, purchase_list) == result, "Value should be mocked"

class TestGetItem:
	def test_get_item(self, item_list):
		assert get_item(item_list[0].name, item_list) == item_list[0]
		assert get_item(item_list[1].name, item_list) == item_list[1]

	def test_get_item__empty_item_list(self, item_list):
		with pytest.raises(RuntimeError):
			item = get_item('Chess', [])

	def test_get_item__item_name_not_found(self, item_list):
		with pytest.raises(RuntimeError):
			item = get_item('Doom', item_list)

	def test_get_item__invalid_item_list(self):
		with pytest.raises(AttributeError):
			item = get_item('Chess', [1, 2, 3])


class TestGetUser:
	def test_get_user(self, users_list):
		assert get_user(users_list[0].name, users_list) == users_list[0]
		assert get_user(users_list[1].name, users_list) == users_list[1]

	def test_get_user__invalid_user(self, users_list):
		with pytest.raises(RuntimeError):
			user = get_user('', users_list)

	def test_get_user__user_doesnt_exist(self, users_list):
		with pytest.raises(RuntimeError):
			user = get_user('Linus', users_list)

	def test_get_user__invalid_user_list(self, users_list):
		with pytest.raises(AttributeError):
			user = get_user('Linus', ['a', 'b'])


class TestSearchApp:
	def test_search_app(self, app_list):
		assert get_app(app_list[0].name, app_list) == app_list[0]
		assert get_app(app_list[1].name, app_list) == app_list[1]

	def test_search_app__empty_app_list(self):
		with pytest.raises(RuntimeError):
			app = get_app('Chess', [])

	def test_search_app__invalid_app_list(self):
		with pytest.raises(AttributeError):
			app = get_app('Chess', [1, 2, 3])

	def test_search_app__app_not_found(self, app_list):
		with pytest.raises(RuntimeError):
			app = get_app('Chezz', app_list)


class TestGetDevByAppid:
	def test_get_dev_by_appid(self, app_list, dev_list):
		assert get_dev_by_appid(app_list[0].id, app_list, dev_list) == dev_list[0]
		assert get_dev_by_appid(app_list[1].id, app_list, dev_list) == dev_list[0]
		assert get_dev_by_appid(app_list[2].id, app_list, dev_list) == dev_list[1]

	def test_get_dev_by_appid__empty_app_list(self, app_list, dev_list):
		with pytest.raises(RuntimeError):
			dev = get_dev_by_appid(1, [], dev_list)

	def test_get_dev_by_appid__empty_dev_list(self, app_list, dev_list):
		with pytest.raises(RuntimeError):
			dev = get_dev_by_appid(1, app_list, [])

	def test_get_dev_by_appid__app_not_found(self, app_list, dev_list):
		with pytest.raises(RuntimeError):
			dev = get_dev_by_appid(5, app_list, [])

	def test_get_dev_by_appid__invalid_app_list(self, dev_list):
		with pytest.raises(AttributeError):
			dev = get_dev_by_appid(5, ['a', 'b'], dev_list)

	def test_get_dev_by_appid__invalid_dev_list(self, app_list):
		with pytest.raises(AttributeError):
			dev = get_dev_by_appid(5, app_list, ['a', 'b'])


class TestReward:
	def test_create_transaction(self):
		purchase_values = {'price': 2.0, 'dev': 1.50, 'store': 0.50, 'rewards': None}
		transaction_info = {'purchase_values': purchase_values, 'purchase_total': 1,
							'item_id': 1, 'app_id': 1, 'user_id': 1, 'store': 'aptoide'}
		transaction_test = create_transaction(transaction_info)
		assert transaction_test == Transaction(id=transaction_info['purchase_total'] + 1,
																   item_id=transaction_info['item_id'],
																   app_id=transaction_info['app_id'],
																   user_id=transaction_info['user_id'],
																   value=transaction_info['purchase_values']['price'],
																   date=transaction_test.date,
																   reward=transaction_info['purchase_values'][
																	   'rewards'],
																   store=transaction_info['store'])

	def test_create_transaction__exception(self):
		with pytest.raises(KeyError):
			transaction_test = create_transaction({})


class TestGetRewardInEuros:
	def test_get_reward_in_euros(self):
		assert get_reward_in_euros({'price': 10.0, 'rewards': 0.10}) == 1.0

	def teardown_method(cls):
		pass

# mocker.patch("src.logic.search_app", return_value=app_list[0])
# mocker.patch("src.logic.get_item", return_value=item_list[0])
# mocker.patch("src.logic.get_user", return_value=users_list[0])
# mocker.patch("src.logic.search_app", return_value=app_list[0])
# mocker.patch("src.logic.calculate_prices",
# 			 return_value={'price': 2.0, 'dev': 1.5, 'store': 0.5, 'rewards': None})
