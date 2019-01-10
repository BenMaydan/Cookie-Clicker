import cookie
import upgradeLogic
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
		print('3. Reset')
		print('4. Developer login')
		print('5. Change username or password')
		print('6. Exit')
		choice = input('Please choose one of the above:\n')

		if choice == '1':
			cookie.clicker()

		elif choice == '2':
			upgradesMenu()


		elif choice == '3':

			exit2 = False
			while not exit2:

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
					exit2 = True

				else:
					print('Unrecognized input!')


		elif choice == '4':
			developer.checkLogin()

		elif choice == '5':
			print('\nNot available just yet')
			#password = input('\nWhat is the password to change developer account info?\n')
			#cookie.checkAdminPassword()
			#cookie.forgotUsernameOrPassword()

		elif choice == 'more':
			save.file('cookiesData.pickle', 'wb', {'currentUser':10000000000})

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

			cookiesDict = save.file('cookiesData.pickle', 'rb')
			doubleUpgradeDict = save.file('doubleUpgrade.pickle', 'rb')
			
			exit3 = False
			while not exit3:
				
				print('\nThe cost for this upgrade is ' + str(doubleUpgradeDict['cost']))
				doubleUpgradeChoice = input('Would you like to go ahead with buying this upgrade? yes/no\n')

				if doubleUpgradeChoice == 'yes':
					userCookies = cookiesDict['currentUser']

					#Checks if user has enough cookies to purchase the upgrade
					#Subtracts the cost of the upgrade from it
					#Only if their cookies is higher than or equal to the cost of the upgrade
					if cookiesDict['currentUser'] >= doubleUpgradeDict['cost']:
						exit3 = True
						upgradeLogic.doubleUpgrade()

					else:
						exit3 = True
						print('You do not have enough cookies to purchase this upgrade!')
						
						#Checks to make sure recursive calling has not exceeded the limit
						try:
							upgradesMenu()
						except:
							exit3 = True
							exit = True
							print('An Error Occurred!')
							mainMenu()

				elif doubleUpgradeChoice == 'no':
					exit3 = True
					#Checks to make sure recursive calling has not exceeded the limit
					try:
						upgradesMenu()
					except:
						print('An Error Occurred!')
						mainMenu
				else:
					print('Unrecognized input!')

		
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


		elif choiceOfUpgrade == '6':
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


