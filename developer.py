import save
import menu
import pickle

def manuallyChangeCookies():
	"""
	Function in developer menu where the developer can manually change the amount of cookies the current user has
	"""

	exit = False

	while not exit:
		changeToString = input('\nWhat would you like to change the cookies to?\n')

		try:
			changeToInteger = int(changeToString)
		
			if changeToInteger >= 0:
				save.saveCookies(changeToInteger)
				print('\nSuccessfully changed number of cookies to ' + changeToString + '\n')
				menu.developerMenu()

			else:
				print("\nYou entered a negative number!")
		

		except:
			print('\nYou did not enter a number!')


def checkLogin():
	"""
	Checks if developer login is valid or not
	"""

	pickle_in = open("devs.pickle","rb")
	registeredDevelopers = pickle.load(pickle_in)

	username = input('\nWhat is your username?\n')
	password = input('\nWhat is your password?\n')

	#Checks if username and password is correct
	if username in registeredDevelopers:

		if registeredDevelopers[username] == password:
			print('\nSuccess! You are now in the developer menu!')
			loggedIn = True
			menu.developerMenu()
		else:
			print('Error: Wrong username or password')
			menu.mainMenu()

	else:
		print('Error: Wrong username or password')
		menu.mainMenu()