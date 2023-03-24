import pytest
import io
import sys
import unittest
from contextlib import redirect_stdout
from io import StringIO
from datetime import datetime
from src.helper import get_user_input, print_balance, print_reward_transaction, print_purchase_transaction
from src.models import Transaction, User, Store, Dev


class TestGetUserInput:
	def test_get_user_input(self, mocker):
		mocker.patch("src.helper.get_input", return_value='Chess Premium Bob')
		assert get_user_input() == {'app': 'Chess', 'item': 'Premium', 'user': 'Bob'}

	def test_get_user_input__less_than_3_values(self, mocker):
		mocker.patch("src.helper.get_input", return_value='Chess Premium')
		with pytest.raises(RuntimeError):
			get_user_input()

	def test_get_user_input__more_than_3_values(self, mocker):
		mocker.patch("src.helper.get_input", return_value='Chess Premium Bob Aptoide')
		with pytest.raises(RuntimeError):
			get_user_input()

	def test_get_user_input__no_input(self, mocker):
		mocker.patch("src.helper.get_input", return_value='')
		with pytest.raises(RuntimeError):
			get_user_input()


class TestPrintRewardTransaction(unittest.TestCase):
	def test_print_reward_transaction(self):
		purchase_values = {'price': 0.10, 'dev': 1.50, 'store': 0.50, 'rewards': 0.10}
		transaction_info = {'purchase_values': purchase_values, 'purchase_total': 1,
							'item_id': 1, 'app_id': 1, 'user_id': 1, 'store': 'aptoide'}
		user = User(id=1, name='John', balance=10.0)
		transaction = Transaction(id=transaction_info['purchase_total'] + 1,
								  item_id=transaction_info['item_id'],
								  app_id=transaction_info['app_id'],
								  user_id=transaction_info['user_id'],
								  value=transaction_info['purchase_values']['price'],
								  date=datetime.now(),
								  reward=transaction_info['purchase_values'][
									  'rewards'],
								  store=transaction_info['store'])
		with redirect_stdout(StringIO()) as sout:
			print_reward_transaction(transaction, user)  # Call function.
		out = sout.getvalue().rstrip('\n')

		output = '''REWARD TRANSACTION => id: 2; amount: €0.10; sender: aptoide; receivers: {John: €0.10}'''
		assert out == output.replace('\n', '').replace('\t', '')


class TestPrintPurchaseTransaction(unittest.TestCase):
	def test_print_purchase_transaction(self):
		output = '''PURCHASE TRANSACTION => id: 2; app: Chess; item: Premium; amount: €2.00; sender: Bob; receivers: {
				Billy: €1.50; aptoide: €0.50}'''

		purchase_values = {'price': 2.0, 'dev': 1.50, 'store': 0.50, 'rewards': None}
		transaction_info = {'purchase_values': purchase_values, 'purchase_total': 1,
							'item_id': 1, 'app_id': 1, 'user_id': 1, 'store': 'aptoide'}
		transaction = Transaction(id=transaction_info['purchase_total'] + 1,
								  item_id=transaction_info['item_id'],
								  app_id=transaction_info['app_id'],
								  user_id=transaction_info['user_id'],
								  value=transaction_info['purchase_values']['price'],
								  date=datetime.now(),
								  reward=transaction_info['purchase_values'][
									  'rewards'],
								  store=transaction_info['store'])

		with redirect_stdout(StringIO()) as sout:
			print_purchase_transaction(transaction, 'Chess', 'Premium', 'Billy', 'Bob', 'aptoide', purchase_values)

		out = sout.getvalue().rstrip('\n')
		assert out == output.replace('\n', '').replace('\t', '')


class TestPrintBalance(unittest.TestCase):
	def test_print_balance__purchase_transaction(self):
		output = '''BALANCE => Bill: €6.00; Billy: €13.00; aptoide: €11.00'''
		user = User(id=1, name='Bill', balance=6.00)
		dev = Dev(id=1, name='Billy', balance=13.0)
		store = Store(id=1, name='aptoide', balance=11.00)
		with redirect_stdout(StringIO()) as sout:
			print_balance({'user': user, 'dev': dev, 'store': store})
		out = sout.getvalue().rstrip('\n')
		assert out == output.replace('\n', '').replace('\t', '')

	def test_print_balance__reward_transaction(self):
		output = '''BALANCE => John: €96.10; aptoide: €10.90'''
		user = User(id=1, name='John', balance=96.10)
		store = Store(id=1, name='aptoide', balance=10.90)
		with redirect_stdout(StringIO()) as sout:
			print_balance({'user': user, 'store': store})
		out = sout.getvalue().rstrip('\n')
		assert out == output.replace('\n', '').replace('\t', '')
