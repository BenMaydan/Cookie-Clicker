import cookie
import save
import logic
import sys
from developer import developer


current = cookie.User()


def notAvailable():
	print('This feature is not available')


def clickerPrint():
	print('\nTo click cookies, press c and to exit to menu press 1.\n')
	current.clicker()


def upgradesMenu():
	"""
	This is the menu to buy upgrades
	"""

	print('\n1. Doubles the cookies per manual click. Cost =', current.get('doubleUpgradeCost'))
	print('-----')
	print('2. Chance of golden cookie (Gives 50 cookies if golden). Cost =', current.get('goldenCookieCost'))
	print('-----')
	print('3. Auto clicker. It starts by clicking 0.1 cookie per second. Cost = ')
	print('-----')
	print('4. VIP auto clicker permanently clicks every second while the program is running. Cost = 100,000,000,000')
	print('-----')
	print('5. VIP golden cookie upgrade makes every cookie golden. Cost = 1,000,000,000,000')
	print('-----')
	print('6. Return to main menu')
	print('-----')
	choiceOfUpgrade = input('Please choose one of the above: ')


	if choiceOfUpgrade == '1':
		logic.upgradeCheckMoney('doubleUpgrade', 'doubleUpgradeCost')

	elif choiceOfUpgrade == '2':
		logic.upgradeCheckMoney('goldenCookie', 'goldenCookieCost')

	elif choiceOfUpgrade == '3':
		autoClickerMenu.display()

	elif choiceOfUpgrade == '4':
		print('\nNot available yet!')

	elif choiceOfUpgrade == '5':
		print('\nNot available yet!')

	elif choiceOfUpgrade == '6':
		mainMenu.display()

	else:
		print('Unrecognized input!')
		upgradesMenu()


class Menu:
	"""
	Creates lots of sub-menus
	"""
	def __init__(self, optionMap, name, exitTitle):
		self.name = name
		self.optionMap = optionMap
		self.exitTitle = exitTitle
		self.options = list(optionMap.keys())

	def display(self, switch = True):
		"""
		Starts a loop which will display the menu given with a dictionary
		"""
		selectionValuePairs = {}
		current = 1
		loop = switch

		while loop:
			print('\nOptions:')
			current = 1
			selectionValuePairs = {}

			#Creates a selection and value pair map
			#Each number (user input) is mapped to the string
			for i in self.options:
				selectionValuePairs[current] = i
				current += 1
			selectionValuePairs[current] = self.exitTitle

			#For each string it prints it and adds the number for selection
			for key in selectionValuePairs:
				print(str(key) + ". " + str(selectionValuePairs[key]))


			try:
				selection = input()
				selection = int(selection)

				#If the user selects exit it stops the program
				if selectionValuePairs[selection] == self.exitTitle:
					print('\nStopping running processes ->')
					sys.exit()

				#Does a function call based off of the user input
				else:
					itemSelected = selectionValuePairs[selection]
					functionToCall = self.optionMap[itemSelected][0]
					parameters = (self.optionMap[itemSelected][1:])

					#In the function call, using the * allows it to have multiple parameters
					functionToCall(*parameters)
			#Validates user input
			except (KeyError, ValueError):
				print('Please make a proper selection.\n')


#Dictionaries of option for menu objects
autoClickerOptions = {'Increase speed':[notAvailable], 'Increase cookie per autoclick':[notAvailable], 'Both upgrades above at once':[notAvailable], 'Go back to upgrade menu':[upgradesMenu]}
mainMenuOptions = {'Clicker':[clickerPrint], 'Upgrades':[upgradesMenu], 'Reset':[logic.mainMenuReset], 'Developer login':[notAvailable], 'Data corrupt':[notAvailable]}

#Creates the menu objects
mainMenu = Menu(mainMenuOptions, 'Main Menu', 'Exit')
autoClickerMenu = Menu(autoClickerOptions, 'Auto Clicker Menu', 'Exit')

developerMenuOptions = {'Change number of cookies for current user':[developer.manuallyChangeCookies], 'Change upgrades for current user':[notAvailable], 'Back to main menu':[mainMenu.display]}
developerMenu = Menu(developerMenuOptions, 'Developer Menu', 'Exit')
#mainMenu.display()
