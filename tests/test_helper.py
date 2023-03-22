import pytest
from src.models import Item, Dev, User, App
from src.helper import get_item, get_user, get_dev_by_appid, search_app


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


class TestGetItem:
	def test_get_item(self, item_list):
		assert get_item(item_list[0].name, item_list) == item_list[0]
		assert get_item(item_list[1].name, item_list) == item_list[1]

	def test_get_item__empty_item_list(self, item_list):
		try:
			item = get_item('Chess', [])
			assert False
		except RuntimeError:
			assert True

	def test_get_item__item_name_not_found(self, item_list):
		try:
			item = get_item('Doom', item_list)
			assert False
		except RuntimeError:
			assert True

	def test_get_item__invalid_item_list(self):
		try:
			item = get_item('Chess', [1,2,3])
			assert False
		except AttributeError:
			assert True


class TestGetUser:
	def test_get_user(self, users_list):
		assert get_user(users_list[0].name, users_list) == users_list[0]
		assert get_user(users_list[1].name, users_list) == users_list[1]

	def test_get_user__invalid_user(self, users_list):
		try:
			user = get_user('', users_list)
			assert False
		except RuntimeError:
			assert True

	def test_get_user__user_doesnt_exist(self, users_list):
		try:
			user = get_user('Linus', users_list)
			assert False
		except RuntimeError:
			assert True

	def test_get_user__invalid_user_list(self, users_list):
		try:
			user = get_user('Linus', ['a','b'])
			assert False
		except AttributeError:
			assert True


class SearchApp:
	def test_search_app(self, app_list):
		assert search_app(app_list[0].name, app_list) == app_list[0]
		assert search_app(app_list[1].name, app_list) == app_list[1]

	def test_search_app__empty_app_list(self):
		try:
			dev = search_app('Chess', [])
			assert False
		except RuntimeError:
			assert True

	def test_search_app__invalid_app_list(self):
		try:
			dev = search_app('Chess', [1, 2, 3])
			assert False
		except AttributeError:
			assert True


class TestGetDevByAppid:
	def test_get_dev_by_appid(self, app_list, dev_list):
		assert get_dev_by_appid(app_list[0].id, app_list, dev_list) == dev_list[0]
		assert get_dev_by_appid(app_list[1].id, app_list, dev_list) == dev_list[0]
		assert get_dev_by_appid(app_list[2].id, app_list, dev_list) == dev_list[1]

	def test_get_dev_by_appid__empty_app_list(self, app_list, dev_list):
		try:
			dev = get_dev_by_appid(1, [], dev_list)
			assert False
		except RuntimeError:
			assert True

	def test_get_dev_by_appid__empty_dev_list(self, app_list, dev_list):
		try:
			dev = get_dev_by_appid(1, app_list, [])
			assert False
		except RuntimeError:
			assert True

	def test_get_dev_by_appid__app_not_found(self, app_list, dev_list):
		try:
			dev = get_dev_by_appid(5, app_list, [])
			assert False
		except RuntimeError:
			assert True

	def test_get_dev_by_appid__invalid_app_list(self, dev_list):
		try:
			dev = get_dev_by_appid(5, ['a', 'b'], dev_list)
			assert False
		except AttributeError:
			assert True

	def test_get_dev_by_appid__invalid_dev_list(self, app_list):
		try:
			dev = get_dev_by_appid(5, app_list, ['a', 'b'])
			assert False
		except AttributeError:
			assert True
