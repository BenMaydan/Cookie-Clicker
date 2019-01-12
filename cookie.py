import menu
import pickle
import save
import upgradeLogic


def clicker():
	"""
	The place the user goes to, to click cookies
	"""
	doubleUpgrade = save.file('doubleUpgrade.pickle', 'rb')
	cookiesPerClick = doubleUpgrade['cookiesPerClick']
	#The variable currentCookies is the number of cookies the user has in the 'vault'
	currentCookies = numberOfCookies()

	letterClicked = input()
	letterClicked = letterClicked.lower()
	
	if letterClicked == 'c':
		currentCookies += cookiesPerClick
		print('# of cookies is ' + str(currentCookies) + '\n')
		goldenCookieTrueOrFalse = upgradeLogic.checkGoldenCookie()
		upgradeLogic.goldenCookieTrueOrFalse(goldenCookieTrueOrFalse, currentCookies)

	elif letterClicked == '1':
		save.file('cookiesData.pickle', 'wb', {'currentUser':currentCookies})
		menu.mainMenu()

	elif letterClicked == 'k':
		print('Cookies per click is', cookiesPerClick, '\n')

	elif letterClicked == '#':
		print(currentCookies)

	else:
		print('Unrecognized input!')
		clicker()


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

		elif choice == 'n':
			exit = True

		else:
			print('Unrecognized input')


def resetUpgrades():
	save.file('doubleUpgrade.pickle', 'wb', {'cookiesPerClick':1, 'costDoubleUpgrade':500})
	save.file('goldenCookie.pickle', 'wb', {'goldenCookieChance':1, 'costGoldenCookie':1000})
	print('\nUpgrades successfully reset!')


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

