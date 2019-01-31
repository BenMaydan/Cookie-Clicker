import menu
import pickle
import save


class User:
	"""
	All the user methods for the current user

	Does not communicate with a server (at the moment)
	All of this is done locally
	"""

	def clicker(self):
		"""
		The place the user goes to, to click cookies
		"""
		import save
		import time

		letterClicked = input()
		letterClicked = letterClicked.lower()
		
		if letterClicked == 'c':
			totalCookies = self.get('totalCookies')
			cookiesPerClick = self.get('cookiesPerClick')
			totalCookies += cookiesPerClick
			self.set('totalCookies', totalCookies)
			print('# of cookies is ' + str(self.get('totalCookies')) + '\n')
			goldenCookieTrueOrFalse = save.checkGoldenCookie()
			save.goldenCookieTrueOrFalse(goldenCookieTrueOrFalse)

		elif letterClicked == '1':
			totalCookies = self.get('totalCookies')
			self.set('totalCookies', totalCookies)
			menu.mainMenu.display()

		elif letterClicked == 'k':
			print('Cookies per click is', str(self.get('cookiesPerClick')), '\n')
			self.clicker()

		elif letterClicked == '#':
			print(str(self.get('totalCookies')), '\n')
			self.clicker()

		else:
			print('Unrecognized input!')
			self.clicker()


	def get(self, thingToGet):
		"""
		Gets the most current value of the 'instance attribute' in this user class
		"""
		currentData = save.file('userData.pickle', 'rb')
		return currentData[thingToGet]


	def set(self, thingToSet, setTo):
		"""
		Updates the current data to reflect changes made in a different file or function/method
		"""
		currentData = save.file('userData.pickle', 'rb')
		currentData[thingToSet] = setTo
		save.file('userData.pickle', 'wb', currentData)


	def resetCookies(self):
		"""
		Resets the cookies the user has to 0
		"""

		exit = False
		while not exit:

			choice = input('\nAre you sure you would like to reset your cookies? y/n\n')
		
			if choice == 'y':
				exit = True
				self.set('totalCookies', 0)
				print('\nSuccessfully reset cookies!')

			elif choice == 'n':
				exit = True

			else:
				print('Unrecognized input')


	def resetUpgrades(self):
		self.set('cookiesPerClick', 1)
		self.set('doubleUpgradeCost', 500)
		self.set('goldenCookieChance', 1)
		self.set('goldenCookieCost', 1000)
		print('\nUpgrades successfully reset!')





#boot
	#load save data
	#use ^ for v
	#use init method to keep up to date



#main loop#
	#options
	#does whatever


	#check: saved cookie total vs current cookie total
		#if its a big enough difference (up to you) then save




