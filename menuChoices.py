import menu
import upgradeLogic
import cookie
import save


def mainMenuReset():
	"""
	Logic for the reset choice in the main nenu
	"""

	print('\n\n1. Reset Cookies')
	print('2. Reset Upgrades')
	print('3. Exit')
	resetChoice = input('')
	
	if resetChoice == '1':
		save.file('cookiesData.pickle', 'wb', {'currentUser':0})
		print('\nSuccessfully reset cookies!')

	elif resetChoice == '2':
		cookie.resetUpgrades()

	elif resetChoice == '3':
		pass

	else:
		print('Unrecognized input!')
		mainMenuReset()


def doubleUpgrade():
	"""
	This is the logic for the double upgrade
	"""

	cookiesDict = save.file('cookiesData.pickle', 'rb')
	doubleUpgradeDict = save.file('doubleUpgrade.pickle', 'rb')
		

	print('\nThe cost for this upgrade is ' + str(doubleUpgradeDict['cost']))
	doubleUpgradeChoice = input('Would you like to go ahead with buying this upgrade? yes/no\n')

	if doubleUpgradeChoice == 'yes':
		userCookies = cookiesDict['currentUser']

		#Checks if user has enough cookies to purchase the upgrade
		#Subtracts the cost of the upgrade from it
		#Only if their cookies is higher than or equal to the cost of the upgrade
		if cookiesDict['currentUser'] >= doubleUpgradeDict['cost']:
			#This upgrade logic should read and write everything to the file
			#But only if the user has enough money and they want to buy the upgrade
			upgradeLogic.doubleUpgrade()

		else:
			print('You do not have enough cookies to purchase this upgrade!')
			menu.upgradesMenu()

	elif doubleUpgradeChoice == 'no':
		exit3 = True
		menu.upgradesMenu()
	else:
		print('Unrecognized input!')


def autoClickerUpgrade():

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
		menu.upgradesMenu()

	else:
		print('Unrecognized input!')