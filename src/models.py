from datetime import datetime
from pydantic import BaseModel


class Transaction(BaseModel):
	id: int
	item_id: int
	user_id: int
	app_id: int
	value: float
	date: datetime
	reward: float = None
	store: str


class Item(BaseModel):
	id: int
	app_id: int
	name: str
	price: float


class App(BaseModel):
	id: int
	dev_id: int
	name: str


class Dev(BaseModel):
	id: int
	name: str
	balance: float

	def sell_item(self, value):
		self.balance = round(self.balance + value, 2)


class User(BaseModel):
	id: int
	name: str
	balance: float

	def purchase_app(self, value):
		if self.balance >= value:
			self.balance = round(self.balance - value, 2)
		else:
			print('User have no founds. Balance: ', self.balance)
			raise

	def get_reward(self, reward_value):
		self.balance = round(self.balance + reward_value, 2)


class Store(BaseModel):
	id: int
	name: str
	balance: float

	def sell_item(self, value):
		self.balance = round(self.balance + value, 2)

	def give_reward(self, reward_value):
		if self.balance >= reward_value:
			self.balance = round(self.balance - reward_value, 2)
		else:
			print('The store have no founds. Balance: ', self.balance)
			raise
