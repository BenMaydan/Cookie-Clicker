import menu
import pickle
import save
#import config


def clicker(currentCookies, cookiesPerClick = 1):
	"""
	The place the user goes to, to click cookies
	"""
	#The parameter currentCookies is the number of cookies the user has in the 'vault'

	cookies = 0
	exit = False

	print("\nAt any time, press '1' to go back to the main menu. To click cookies type in 'c' and then press enter\n")

	while not exit:
		
		letterClicked = input()
		
		if letterClicked == 'c':
			currentCookies += cookiesPerClick
			print('# of cookies is ' + str(currentCookies) + '\n')
			save.saveCookies(currentCookies)

		elif letterClicked == '1':
			save.saveCookies(currentCookies)
			menu.mainMenu()

		elif letterClicked == '#':
			print(currentCookies)

		else:
			print('Unrecognized input!')


def corruptedData():
	"""
	If the file for how many cookies the user has is empty, this function compensates by giving 1500 cookies
	"""

	cookieDict = {}
	cookieDict['currentUser'] = 1500

	pickle_out = open("cookiesData.pickle","wb")
	pickle.dump(cookieDict, pickle_out)
	pickle_out.close()


def resetCookies():
	"""
	Resets the cookies the user has to 0
	"""

	exit = False
	while not exit:

		choice = input('\nAre you sure you would like to reset your cookies? y/n\n')
	
		if choice == 'y':
			exit = True
			save.saveCookies(0)
			print('\nSuccessfully reset cookies!')
			menu.mainMenu()

		if choice == 'n':
			exit = True
			menu.mainMenu()

		else:
			print('Unrecognized input')


def numberOfCookies():
	"""
	Determines current number of cookies the user has
	"""

	cookiesDataFile = open('cookiesData.pickle', 'rb')
	cookieDict = pickle.load(cookiesDataFile)
	numberOfCookies = cookieDict['currentUser']
	cookiesDataFile.close()

	return numberOfCookies

