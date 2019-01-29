import menu
import cookie
import save
import time
from pynput.keyboard import Key, Controller


#Upgrade Logic
def upgradeCheckMoney(upgrade, upgradeCost):
	"""
	This is the logic for the double upgrade
	"""

	userDict = save.file('userData.pickle', 'rb')
	print(userDict)
	upgradeToFunctionCall = {'doubleUpgrade':save.doubleUpgrade, 'goldenCookie':save.goldenCookieUpgrade}
		

	print('\nThe cost for this upgrade is ' + str(userDict[upgradeCost]))
	upgradeChoice = input('Would you like to go ahead with buying this upgrade? yes/no\n')

	if upgradeChoice == 'yes':
		userCookies = userDict['totalCookies']

		#Checks if user has enough cookies to purchase the upgrade
		#Subtracts the cost of the upgrade from it
		#Only if their cookies is higher than or equal to the cost of the upgrade
		if userDict['totalCookies'] >= userDict[upgradeCost]:
			#Should read and write everything to the file
			#But only if the user has enough money(cookies) and they want to buy the upgrade
			upgradeToFunctionCall[upgrade]()
			menu.upgradesMenu()

		else:
			print('You do not have enough cookies to purchase this upgrade!')
			menu.upgradesMenu()

	elif upgradeChoice == 'no':
		menu.upgradesMenu()
	
	else:
		print('Unrecognized input!')




#Menu logic
def mainMenuReset():
	"""
	Logic for the reset choice in the main nenu
	"""
	print('\n1. Reset Cookies')
	print('2. Reset Upgrades')
	print('3. Exit')
	resetChoice = input('')
	
	if resetChoice == '1':
		menu.current.set('totalCookies', 0)
		print('\nSuccessfully reset cookies!')

	elif resetChoice == '2':
		menu.current.resetUpgrades()

	elif resetChoice == '3':
		pass

	else:
		print('Unrecognized input!')
		mainMenuReset()