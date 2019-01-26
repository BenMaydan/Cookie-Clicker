import menu
import pickle
import save


class User:
	"""
	All the user methods for the current user

	Does not communicate with a server
	All of this is done locally
	"""
	#Ask in class if variables defined under this line
	#For example:
	#var = 1
	#Are mutable or immutable
	#Because I need to know why currentCookies does not update the second time I press c


	def __init__(self, cookiesPerClick, doubleUpgradeCost, goldenCookieChance, goldenCookieCost, currentCookies):
		self.cookiesPerClick = cookiesPerClick
		self.doubleUpgradeCost = doubleUpgradeCost
		self.goldenCookieChance = goldenCookieChance
		self.goldenCookieCost = goldenCookieCost
		self.currentCookies = currentCookies


	def clicker(self):
		"""
		The place the user goes to, to click cookies
		"""
		import save
		import time

		time.sleep(0.01)
		letterClicked = input()
		letterClicked = letterClicked.lower()
		
		if letterClicked == 'c':
			self.inc()

			
			save.file('cookiesData.pickle', 'wb', {'currentUser': self.currentCookies})
			print('# of cookies is ' + str(self.currentCookies) + '\n')
			goldenCookieTrueOrFalse = save.checkGoldenCookie()
			save.goldenCookieTrueOrFalse(goldenCookieTrueOrFalse, self.currentCookies)

		elif letterClicked == '1':
			save.file('cookiesData.pickle', 'wb', {'currentUser':self.currentCookies})
			menu.mainMenu()

		elif letterClicked == 'k':
			print('Cookies per click is', self.cookiesPerClick, '\n')
			self.clicker()

		elif letterClicked == '#':
			print(self.currentCookies, '\n')
			self.clicker()

		else:
			print('Unrecognized input!')
			self.clicker()


	def inc(self):
		print(self.currentCookies, "cc")
		self.currentCookies += self.cookiesPerClick
		print(self.currentCookies, "cc")



	def resetCookies(self):
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


	def resetUpgrades(self):
		save.file('doubleUpgrade.pickle', 'wb', {'cookiesPerClick':1, 'cost':500})
		save.file('goldenCookie.pickle', 'wb', {'goldenCookieChance':1, 'cost':1000})
		print('\nUpgrades successfully reset!')




