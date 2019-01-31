import pickle
import menu
import random

#print(menu.getCurrent())


def file(fileName, readOrWrite, whatToDump = None):

	if readOrWrite == 'rb':
		file = open(fileName, readOrWrite)
		returnDict = pickle.load(file)
		file.close()
		return returnDict

	elif readOrWrite == 'wb':
		file = open(fileName, readOrWrite)
		pickle.dump(whatToDump, file)
		file.close()
		return file


def doubleUpgrade():
	"""
	Performs all of the logic if the double upgrade is successful
	"""
	######MAKE THIS BETTER
	######BE ABLE TO USE FOR EVERY UPGRADE

	#Grabbing variable values
	totalCookies = menu.current.get('totalCookies')
	cookiesPerClick = menu.current.get('cookiesPerClick')
	doubleUpgradeCost = menu.current.get('doubleUpgradeCost')

	#Writes new data to the file
	newAmountOfCookies = totalCookies - doubleUpgradeCost
	menu.current.set('totalCookies', newAmountOfCookies)
	menu.current.set('cookiesPerClick', cookiesPerClick * 2)
	menu.current.set('doubleUpgradeCost', doubleUpgradeCost * 3)
	print('\nUpgrade successful!')
	

	#Checks how many cookies the user has left
	#And prints to the user for clarity
	totalCookies = menu.current.get('totalCookies')
	print('You have ' + str(totalCookies) + ' cookies left!')


def goldenCookieUpgrade():
	"""
	If the golden cookie upgrade goes through,
	this function will do the logic for it
	"""
	totalCookies = menu.current.get('totalCookies')
	goldenCookieCost = menu.current.get('goldenCookieCost')
	goldenCookieChance = menu.current.get('goldenCookieChance')


	#Writes new data to the file
	newAmountOfCookies = totalCookies - goldenCookieCost
	menu.current.set('totalCookies', newAmountOfCookies)
	menu.current.set('goldenCookieChance', chance * 2)
	menu.current.set('goldenCookieCost', cost * 3)
	print('Upgrade successful!')


	#Checks how many cookies the user has left
	#Then it prints it to console
	totalCookies = menu.current.get('totalCookies')
	print('\nYou have ' + str(totalCookies) + ' cookies left!')


def checkGoldenCookie():
	"""
	Checks if the user just clicked on a golden cookie
	"""

	goldenCookieChance = menu.current.get('goldenCookieChance')
	chance = random.randrange(0, 101)

	
	if chance <= goldenCookieChance:
		print('\n\nYOU JUST FOUND A GOLDEN COOKIE!\n\n')
		return True

	else:
		return False


def goldenCookieTrueOrFalse(worked):
	"""
	Checks if the user received a golden cookie
	And performs relevant logic for the check
	"""
	#Adds 50 cookies (golden cookie) to user's current cookies
	totalCookies = menu.current.get('totalCookies')
	newCookiesToSave = totalCookies + 50

	#If the chance of getting a golden cookie worked:
	#Then the user will get a golden cookie
	#And the cookie he clicked will not be saved
	if worked == True:
		menu.current.set('totalCookies', newCookiesToSave)
		menu.current.clicker()

	#If the chance of getting a golden cookie failed:
	#Then this will just save the current cookies
	if worked == False:
		menu.current.clicker()