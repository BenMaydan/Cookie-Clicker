import cookie
import upgradeLogic
import save
import developer
import menuChoices



def mainMenu():
	"""
	The menu for when the program is run. This is the menu to go to other places
	"""

	print('\n1. Clicker')
	print('2. Upgrades')
	print('3. Reset')
	print('4. Developer login')
	print('5. Data corrrupt')
	print('6. Exit')
	choice = input('Please choose one of the above:\n')

	if choice == '1':
		print("\nTo click cookies type in 'c' and then press enter. At any time, press '1' to go back to the main menu.\n")
		cookie.clicker()

	elif choice == '2':
		upgradesMenu()

	elif choice == '3':
		menuChoices.mainMenuReset()

	elif choice == '4':
		developer.checkLogin()

	elif choice == '5':
		print("\nI don't get paid enough for this...")
		cookie.corrupt()

	elif choice == 'more':
		save.file('cookiesData.pickle', 'wb', {'currentUser':10000000000})

	elif choice == '6':
		return True

	else:
		print('Unrecognized input!')


def upgradesMenu():
	"""
	This is the menu to buy upgrades
	"""

	print('\n1. Doubles the cookies per manual click. Cost = ')
	print('2. Chance of golden cookie (Gives 50 cookies if golden). Cost = ')
	print('3. Auto clicker. It starts by clicking 0.1 cookie per second. Cost = ')
	print('4. VIP auto clicker permanently clicks every second while the program is running. Cost = 100,000,000,000')
	print('5. VIP golden cookie upgrade makes every cookie golden. Cost = 1,000,000,000,000')
	print('6. Return to main menu')
	choiceOfUpgrade = input('Please choose one of the above:\n')


	if choiceOfUpgrade == '1':
		menuChoices.upgradeCheckMoney('doubleUpgrade')
	
	elif choiceOfUpgrade == '2':
		menuChoices.upgradeCheckMoney('goldenCookie')

	elif choiceOfUpgrade == '3':
		menuChoices.autoClickerUpgrade()

	elif choiceOfUpgrade == '4':
		print('\nNot available yet!')

	elif choiceOfUpgrade == '5':
		print('\nNot available yet!')

	elif choiceOfUpgrade == '6':
		mainMenu()

	else:
		print('Unrecognized input!')
		upgradesMenu()


def developerMenu():
	"""
	The menu for all things related to developers
	"""

	exit = False
	while not exit:

		print('1. Change number of cookies for current user')
		print('2. Change upgrades for current user')
		print('3. Back to main menu')
		choice = input('Please choose one of the above:\n')

		if choice == '1':
			developer.manuallyChangeCookies()

		elif choice == '2':
			print('\nCurrently being worked on!\n')

		elif choice == '3':
			exit = True
			mainMenu()

		else:
			print('Unrecognized input!')


