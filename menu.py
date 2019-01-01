import main

def mainMenu():

	exit = False

	while not exit:
		print('\n1. Clicker')
		print('2. Reset cookies')
		print('3. Developer login')
		print('4. Change username or password')
		print('5. Exit')
		choice = input('Please choose one of the above:\n')

		if choice == '1':
			cookies = main.loadSaveData()
			main.clicker(cookies)

		elif choice == '2':
			main.resetCookies()

		elif choice == '3':
			main.developer()

		elif choice == '4':
			print('\nNot available just yet')
			#password = input('\nWhat is the password to change developer account info?\n')
			#main.checkAdminPassword()
			#main.forgotUsernameOrPassword()

		elif choice == '5':
			exit = True

		else:
			print('Unrecognized input!')


def developerMenu():

	exit = False
	while not exit:

		print('1. Change number of cookies for current user')
		print('2. Back to main menu')
		print('3. Exit')
		choice = input('Please choose one of the above:\n')

		if choice == '1':
			main.manuallyChangeCookies()

		if choice == '2':
			exit = True
			mainMenu()

		if choice == '3':
			exit = True

		else:
			print('Unrecognized input!')


