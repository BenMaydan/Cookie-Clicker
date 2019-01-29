import cookie
import save
import logic
from developer import developer


current = cookie.User()

def getCurrent():
	return current


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
		current.clicker()

	elif choice == '2':
		upgradesMenu()

	elif choice == '3':
		logic.mainMenuReset()

	elif choice == '4':
		#developer.checkLogin()
		print('')

	elif choice == '5':
		print("\nI don't get paid enough for this...")
		#cookie.corrupt()

	elif choice == 'more':
		current.set('totalCookies', 10000000000000000000)

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
		logic.upgradeCheckMoney('doubleUpgrade', 'doubleUpgradeCost')
	
	elif choiceOfUpgrade == '2':
		logic.upgradeCheckMoney('goldenCookie', 'goldenCookieCost')

	elif choiceOfUpgrade == '3':
		autoClickerMenu()

	elif choiceOfUpgrade == '4':
		print('\nNot available yet!')

	elif choiceOfUpgrade == '5':
		print('\nNot available yet!')

	elif choiceOfUpgrade == '6':
		mainMenu()

	else:
		print('Unrecognized input!')
		upgradesMenu()


def autoClickerMenu():

	print('\nThere are 2 choices for this upgrade')
	print('1. Increase speed')
	print('2. Increase cookie per autoclick')
	print('3. Both upgrades above at once')
	print('4. Go back to upgrade menu')
	choice = input('Which one would you like?\n')


	if choice == '1':
		print('\nNot available yet!')

	elif choice == '2':
		print('\nNot available yet!')

	elif choice == '3':
		print('\nNot available yet')

	elif choice == '4':
		upgradesMenu()

	else:
		print('Unrecognized input!')



def developerMenu():
	"""
	The menu for all things related to developers
	"""

	exit = False
	while not exit:

		print('\n1. Change number of cookies for current user')
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


