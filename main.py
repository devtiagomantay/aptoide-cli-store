import click


@click.command()
@click.option('--appname', default=None, help='App name')
@click.option('--item', default=None, help='Item from the app')
@click.option('--user', default=None, help='Username')
def purchase(appname, item, user):
	print('You want to buy the app: ', appname)
	print('You want to buy the item: ', item)
	print('You are the user: ', user)


if __name__ == '__main__':
	purchase()
