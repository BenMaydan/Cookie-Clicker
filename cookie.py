import menu
import pickle
import save


def clicker():
	"""
	The place the user goes to, to click cookies
	"""
	#The parameter currentCookies is the number of cookies the user has in the 'vault'
	doubleUpgrade = save.file('doubleUpgrade.pickle', 'rb')
	cookiesPerClick = doubleUpgrade['cookiesPerClick']

	print("\nAt any time, press '1' to go back to the main menu. To click cookies type in 'c' and then press enter\n")
	
	cookieExit = False

	while not cookieExit:
		
		currentCookies = numberOfCookies()
		letterClicked = input()
		
		if letterClicked == 'c':
			currentCookies += cookiesPerClick
			print('# of cookies is ' + str(currentCookies) + '\n')
			save.file('cookiesData.pickle', 'wb', {'currentUser': currentCookies})

		elif letterClicked == '1':
			cookieExit = True
			save.file('cookiesData.pickle', 'wb', {'currentUser':currentCookies})
			menu.mainMenu()

		elif letterClicked == '#':
			print(currentCookies)

		else:
			print('Unrecognized input!')


def resetCookies():
	"""
	Resets the cookies the user has to 0
	"""

	exit = False
	while not exit:

		choice = input('\nAre you sure you would like to reset your cookies? y/n\n')
	
		if choice == 'y':
			exit = True
			save.file('cookiesData.pickle', 'wb', {'currentUser':0})
			print('\nSuccessfully reset cookies!')
			menu.mainMenu()

		if choice == 'n':
			exit = True
			menu.mainMenu()

		else:
			print('Unrecognized input')


def resetUpgrades():
	save.file('doubleUpgrade.pickle', 'wb', {'cookiesPerClick':1, 'cost':500})


def numberOfCookies():
	"""
	Determines current number of cookies the user has
	"""

	try:
		cookieDict = save.file('cookiesData.pickle', 'rb')
		numberOfCookies = cookieDict['currentUser']
		return numberOfCookies
	except:
		print("Your cookie data is corrupted just like Donald Trump. Here is 1500 cookies for compensation")
		save.file('cookiesData.pickle', 'wb', {'currentUser':1500})

