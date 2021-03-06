import menu
import save
import cookie
import save
import time
import screen


#menu.getCurrent()

def mainMenuReset():
	"""
	Logic for the reset choice in the main nenu
	"""
	screen.clearScreen()
	print('1. Reset Cookies')
	print('2. Reset Upgrades')
	print('3. Exit')
	resetChoice = input('')
	
	if resetChoice == '1':
		save.file('cookiesData.pickle', 'wb', {'currentUser':0})
		print('\nSuccessfully reset cookies!')
		time.sleep(1)

	elif resetChoice == '2':
		current.resetUpgrades()

	elif resetChoice == '3':
		pass

	else:
		print('Unrecognized input!')
		mainMenuReset()


def upgradeCheckMoney(upgrade):
	"""
	This is the logic for the double upgrade
	"""

	cookiesDict = save.file('cookiesData.pickle', 'rb')
	upgradeDict = save.file(upgrade + '.pickle', 'rb')
	upgradeToCommand = {'doubleUpgrade':save.doubleUpgrade, 'goldenCookie':save.goldenCookieUpgrade}
		

	print('\nThe cost for this upgrade is ' + str(upgradeDict['cost']))
	upgradeChoice = input('Would you like to go ahead with buying this upgrade? yes/no\n')

	if upgradeChoice == 'yes':
		userCookies = cookiesDict['currentUser']

		#Checks if user has enough cookies to purchase the upgrade
		#Subtracts the cost of the upgrade from it
		#Only if their cookies is higher than or equal to the cost of the upgrade
		if cookiesDict['currentUser'] >= upgradeDict['cost']:
			#This upgrade logic should read and write everything to the file
			#But only if the user has enough money and they want to buy the upgrade
			upgradeToCommand[upgrade]()
			menu.upgradesMenu()

		else:
			print('You do not have enough cookies to purchase this upgrade!')
			menu.upgradesMenu()

	elif upgradeChoice == 'no':
		menu.upgradesMenu()
	
	else:
		print('Unrecognized input!')


def goldenCookie():
	"""
	This are the checkers for the double upgrade
	"""
	cookiesDict = save.file('cookiesData.pickle', 'rb')
	goldenCookieDict = save.file('goldenCookie.pickle', 'rb')

	print('The cost for the golden cookie')


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