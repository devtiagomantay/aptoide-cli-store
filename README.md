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

Data entry is done via the keyboard, in the format (separated by spaces)

```console
App Item User
```
Example:

Input:
```console
TrivialDrive Oil User#123
```

Return
```console
PURCHASE TRANSACTION => id: 1; app: TrivialDrive; item: Oil; amount: €1.00; sender: User#123; receivers: {TrivialDriveDeveloper#2: €0.75; AptoideStore#1: €0.25}  
BALANCE => User#123: €9.00; TrivialDriveDeveloper#2: €10.75 AptoideStore#1: €10.25
```

Input:
```console
TrivialDrive Oil User#123
```

Return
```console
PURCHASE TRANSACTION => id: 2; app: TrivialDrive; item: Antifreeze; amount: €1.20; sender: User#123; receivers: {TrivialDriveDeveloper#2: €0.90; AptoideStore#1: €0.30}
BALANCE => User#123: €7.80; TrivialDriveDeveloper#2: €11.65 AptoideStore#1: €10.55
#########
REWARD TRANSACTION => id: 3; amount: €0.06; sender: AptoideStore#1; receivers: {User#123: €0.06}
BALANCE => User#123: €7.86; AptoideStore#1: €10.49
```

## Unit tests
Run unit tests

> pytest

### Test coverage
 
> pip install pytest.cov 
> pytest --cov=.


## Class diagram