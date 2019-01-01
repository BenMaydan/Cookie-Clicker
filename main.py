import menu
import pickle
#import config


def clicker(currentCookies):

	cookies = 0
	exit = False

	print("\nAt any time, press '1' to go back to the main menu. To click cookies type in 'c' and then press enter\n")

	while not exit:
		
		letterClicked = input()
		
		if letterClicked == 'c':
			currentCookies += 1
			print('# of cookies is ' + str(currentCookies))
			saveCookies(currentCookies)

		elif letterClicked == '1':
			saveCookies(currentCookies)
			menu.mainMenu()

		elif letterClicked == '#':
			print(currentCookies)

		else:
			print('Unrecognized input!')


def developer():

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


def loadSaveData():
	
	try:
		pickle_out = open("cookiesData.pickle","rb")
		cookieDict = pickle.load(pickle_out)
		totalCookies = cookieDict['currentUser']
		pickle_out.close()

		return totalCookies
	
	except EOFError:
		print("I'm afraid your cookie data has been corrupted. We know this won't compensate, but we have given you 1,500 cookies to make up for it.")
		corruptedData()



def saveCookies(cookiesClicked):

	clickedCookies = {}
	clickedCookies['currentUser'] = cookiesClicked

	pickle_out = open("cookiesData.pickle","wb")
	pickle.dump(clickedCookies, pickle_out)
	pickle_out.close()


def manuallyChangeCookies():

	exit = False

	while not exit:
		changeTo = input('\nWhat would you like to change the cookies to?\n')

		try:
			changeTo = int(changeTo)
			
			if changeTo >= 0:
				saveCookies(int(changeTo))
				print('\nSuccessfully changed number of cookies to ' + str(changeTo) + '\n')
				menu.developerMenu()

			else:
				print("\nYou entered a negative number!")
		

		except:
			print('\nYou did not enter a number!')


def corruptedData():

	cookieDict = {}
	cookieDict['currentUser'] = 1500

	pickle_out = open("cookiesData.pickle","wb")
	pickle.dump(cookieDict, pickle_out)
	pickle_out.close()


def resetCookies():
	
	choice = input('\nAre you sure you would like to reset your cookies? y/n\n')

	exit = False
	while not exit:
	
		if choice == 'y':
			exit = True
			saveCookies(0)
			menu.mainMenu()

		elif choice == 'n':
			exit = True
			menu.mainMenu()

		else:
			print('Unrecognized input')


def tempPicklingDev():

	registeredDevelopers = {'Ben':'default'}

	pickle_out = open("devs.pickle","wb")
	pickle.dump(registeredDevelopers, pickle_out)
	pickle_out.close()

def tempPicklingCookies():

	cookieDict = {'currentUser':0}

	pickle_out = open("cookiesData.pickle","wb")
	pickle.dump(cookieDict, pickle_out)
	pickle_out.close()



