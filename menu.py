import cookie
import save
import developer

def mainMenu():
	"""
	The menu for when the program is run. This is the menu to go to other places
	"""

	exit = False

	while not exit:
		print('\n1. Clicker')
		print('2. Upgrades')
		print('3. Reset cookies')
		print('4. Developer login')
		print('5. Change username or password')
		print('6. Exit')
		choice = input('Please choose one of the above:\n')

		if choice == '1':
			cookies = save.loadSaveData()
			cookie.clicker(cookies)

		elif choice == '2':
			upgradesMenu()

		elif choice == '3':
			cookie.resetCookies()

		elif choice == '4':
			developer.checkLogin()

		elif choice == '5':
			print('\nNot available just yet')
			#password = input('\nWhat is the password to change developer account info?\n')
			#cookie.checkAdminPassword()
			#cookie.forgotUsernameOrPassword()

		elif choice == 'more':
			save.saveCookies(100000)

		elif choice == '6':
			exit = True

		else:
			print('Unrecognized input!')


def upgradesMenu():
	"""
	This is the menu to buy upgrades
	"""

	exit = False
	while not exit:

		print('\n1. Doubles the cookies per manual click. Cost = ')
		print('2. Chance of golden cookie (Gives 50 cookies if golden). Cost = ')
		print('3. Auto clicker. It starts by clicking 0.1 cookie per second. Cost = ')
		print('4. VIP auto clicker permanently clicks every second while the program is running. Cost = 100,000,000,000')
		print('5. VIP golden cookie upgrade makes every cookie golden. Cost = 1,000,000,000,000')
		print('6. Return to main menu')
		choiceOfUpgrade = input('Please choose one of the above:\n')

		
		if choiceOfUpgrade == '1':
			print('\nNot available yet!')

		
		elif choiceOfUpgrade == '2':
			print('\nNot available yet!')

		
		elif choiceOfUpgrade == '3':
			print('\nThere are 2 choices for this upgrade')
			print('1. Increase speed')
			print('2. Increase cookie per autoclick')
			print('3. Both upgrades above at once')
			print('4. Go back to upgrade menu')
			
			exit2 = False
			while not exit2:
				choice = input('Which one would you like?\n')

				if choice == '1':
					print('\nNot available yet!')

				elif choice == '2':
					print('\nNot available yet!')

				elif choice == '3':
					print('\nNot available yet')

				elif choice == '4':
					exit2 = True

				else:
					print('Unrecognized input!')

		
		elif choiceOfUpgrade == '4':
			print('\nNot available yet!')

		
		elif choiceOfUpgrade == '5':
			print('\nNot available yet!')


		elif choice == '6':
			exit = True

		
		else:
			print('Unrecognized input!')


def developerMenu():
	"""
	The menu for all things related to developers
	"""

	exit = False
	while not exit:

		print('1. Change number of cookies for current user')
		print('2. Change upgrades for current user')
		print('3. Back to main menu')
		print('4. Exit')
		choice = input('Please choose one of the above:\n')

		if choice == '1':
			developer.manuallyChangeCookies()

		elif choice == '2':
			print('\nCurrently being worked on!\n')

		elif choice == '3':
			exit = True
			mainMenu()

		elif choice == '4':
			exit = True

		else:
			print('Unrecognized input!')


