import save
import menu
import pickle


class developer(object):

	username = 'Ben'
	password = 'default'

	def __init__(self, loggedIn):
		self.loggedIn = loggedIn


	def manuallyChangeCookies(self):
		"""
		Function in developer menu where the developer can manually change the amount of cookies the current user has
		"""

		exit = False

		while not exit:
			changeToString = input('\nWhat would you like to change the cookies to?\n')

			try:
				changeToInteger = int(changeToString)
		
				if changeToInteger >= 0:
					save.file('cookiesData.pickle', 'wb', {'currentUser':changeToInteger})
					print('\nSuccessfully changed number of cookies to ' + changeToString + '\n')

				else:
					print("\nYou entered a negative number!")
			

			except:
				print('\nYou did not enter a number!')

			finally:
				menu.developerMenu()


	def checkLogin(self):
		"""
		Checks if developer login is valid or not
		"""
		print(username)
		print(password)

		usernameInput = input('\nWhat is your username?\n')
		passwordInput = input('\nWhat is your password?\n')

		#Checks if username and password is correct
		if usernameInput == developer.username:

			if passwordInput == developer.password:
				print('\nSuccess! You are now in the developer menu!')
				self.loggedIn = True
				user = developer()
				menu.developerMenu()
			else:
				print('Error: Wrong username or password')
				menu.mainMenu()

		else:
			print('Error: Wrong username or password')
			menu.mainMenu()


	def developerLoginCheck(self, function):
		"""
		Checks if the user is already logged in as a developer
		"""

		functions = {'checkLogin':checkLogin, 'changeCookies':changeCookies}

		if self.loggedIn == True:
			functions[function]()
		else:
			pass





