import pytest
from src.logic import calculate_prices
from datetime import datetime
from src.models import Purchase
from src.models import Item


@pytest.fixture()
def item_list():
	item_list = [
		Item(id=1, app_id=1, name='Premium', price=2.0),
		Item(id=3, app_id=2, name='Premium', price=1.0)]
	yield item_list


@pytest.fixture()
def purchase_list():
	# user1 = 1 purchase, user2 = 2 purchases, user3 = 10 purchases in the same app
	purchase_list = [
		Purchase(id=1, item_id=1, app_id=1, user_id=1, value=2.0, date=datetime.now(), reward=None),
		Purchase(id=2, item_id=1, app_id=1, user_id=2, value=2.0, date=datetime.now(), reward=None),
		Purchase(id=3, item_id=1, app_id=1, user_id=2, value=1.9, date=datetime.now(), reward=95),
		Purchase(id=4, item_id=1, app_id=1, user_id=3, value=2.0, date=datetime.now(), reward=None),
		Purchase(id=5, item_id=1, app_id=1, user_id=3, value=1.9, date=datetime.now(), reward=95),
		Purchase(id=6, item_id=2, app_id=1, user_id=3, value=1.9, date=datetime.now(), reward=95),
		Purchase(id=7, item_id=1, app_id=1, user_id=3, value=1.9, date=datetime.now(), reward=95),
		Purchase(id=8, item_id=1, app_id=1, user_id=3, value=1.9, date=datetime.now(), reward=95),
		Purchase(id=9, item_id=1, app_id=1, user_id=3, value=1.9, date=datetime.now(), reward=95),
		Purchase(id=10, item_id=1, app_id=1, user_id=3, value=1.9, date=datetime.now(), reward=95),
		Purchase(id=11, item_id=1, app_id=1, user_id=3, value=1.9, date=datetime.now(), reward=95),
		Purchase(id=12, item_id=2, app_id=1, user_id=3, value=1.9, date=datetime.now(), reward=95),
		Purchase(id=13, item_id=3, app_id=2, user_id=3, value=2.0, date=datetime.now(), reward=None),
		Purchase(id=14, item_id=2, app_id=1, user_id=3, value=1.8, date=datetime.now(), reward=90)]
	yield purchase_list


class TestLogic:
	def test_calculate_prices_without_discount(self, mocker, item_list, purchase_list):
		mocker.patch("src.logic.get_app_purchases_by_userid", return_value=1)
		mocker.patch("src.logic.get_percentage", return_value=100)
		user_id = 1
		assert calculate_prices(item_list[0], user_id, purchase_list) == {'price': 2.0, 'dev': 1.50, 'store': 0.50,
																  'rewards': None}, \
			"Value should be mocked"

	def test_calculate_prices_without_discount_app2(self, mocker, item_list, purchase_list):
		mocker.patch("src.logic.get_app_purchases_by_userid", return_value=1)
		mocker.patch("src.logic.get_percentage", return_value=100)
		user_id = 3
		assert calculate_prices(item_list[1], user_id, purchase_list) == {'price': 1.0, 'dev': 0.75, 'store': 0.25,
																  'rewards': None}, \
			"Value should be mocked"

	def test_calculate_prices_with_5_percent_reward(self, mocker, item_list, purchase_list):
		mocker.patch("src.logic.get_app_purchases_by_userid", return_value=2)
		mocker.patch("src.logic.get_percentage", return_value=95)
		user_id = 2
		assert calculate_prices(item_list[0], user_id, purchase_list) == {'price': 1.9, 'dev': 1.42, 'store': 0.47,
																  'rewards': 95}, "Value should be mocked"

	def test_calculate_prices_with_10_percent_reward(self, mocker, item_list, purchase_list):
		mocker.patch("src.logic.get_app_purchases_by_userid", return_value=10)
		mocker.patch("src.logic.get_percentage", return_value=90)
		user_id = 3
		assert calculate_prices(item_list[0], user_id, purchase_list) == {'price': 1.8, 'dev': 1.35, 'store': 0.45,
																  'rewards': 90}, "Value should be mocked"

	def teardown_method(cls):
		pass
