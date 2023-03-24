# aptoide-cli-store
Simple assignment to simulate purchases in the aptoide store

> using python 3.10

## Installing the dependencies
pip install -r requirements.txt

## How to run?
Run the file run.py

### How it works?
The application allows you to make purchases of app items, using a user.

The app will record the balance of each entity: user, developer and store.

The user can get a special discount from the store if he buys:
- more than 1 app: 5% discount
- more than 10 apps: 10% discount

## Unit tests
Run unit tests

> pytest

### Test coverage
 
> pip install pytest.cov 
> pytest --cov=.


## Class diagram