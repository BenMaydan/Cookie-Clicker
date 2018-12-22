import main

def mainMenu():

	exit = False

	while not exit:
		print('1. Clicker')
		print('2. Developer')
		print('3. Exit')
		choice = input('Please choose one of the above:\n')

		if choice == '1':
			main.clicker()

		if choice == '2':
			main.developer()

		else:
			exit = True


def developerMenu():

	print('This is a test. Delete me later')

	exit = False

	while not exit:
		print('1. TBA')
		print('2. Exit')

		if choice == '1':
			pass
		
		else:
			exit = True