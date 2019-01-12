import cookie
import save
import random

def doubleUpgrade():
	"""
	Performs all of the logic if the double upgrade is successful
	"""

	#Initializing variables
	cookiesDict = save.file('cookiesData.pickle', 'rb')
	doubleUpgradeDict = save.file('doubleUpgrade.pickle', 'rb')
	userCookies = cookiesDict['currentUser']


	#The block of code below subtracts the cost of the upgrade from the user's total cookies
	newAmountOfCookies = userCookies - doubleUpgradeDict['cost']
	newDictToSave = {'currentUser':newAmountOfCookies}
	save.file('cookiesData.pickle', 'wb', newDictToSave)
	print('Upgrade successful!')


	#Checks current doubleUpgrade file data
	cookiesPerClick = doubleUpgradeDict['cookiesPerClick']
	cost = doubleUpgradeDict['cost']


	#This should actually upgrade the data for the cookies per click
	newDoubleUpgradeDict = doubleUpgradeDict
	newDoubleUpgradeDict['cookiesPerClick'] = cookiesPerClick * 2
	newDoubleUpgradeDict['cost'] = cost * 3
	save.file('doubleUpgrade.pickle', 'wb', newDoubleUpgradeDict)
	

	#Checks how many cookies the user has left
	cookiesDict = save.file('cookiesData.pickle', 'rb')
	userCookies = cookiesDict['currentUser']
	print('\nYou have ' + str(userCookies) + ' cookies left!')


def goldenCookieUpgrade():
	"""
	If the golden cookie upgrade goes through,
	this function will do the logic for it
	"""
	cookiesDict = save.file('cookiesData.pickle', 'rb')
	goldenCookieDict = save.file('goldenCookie.pickle', 'rb')
	userCookies = cookiesDict['currentUser']

	#Subtracts cost from user's total cookies
	newAmountOfCookies = userCookies - goldenCookieDict['cost']
	newDictToSave = {'currentUser':newAmountOfCookies}
	save.file('cookiesData.pickle', 'wb', newDictToSave)
	print('Upgrade successful!')

	#Checks current doubleUpgrade file data
	chance = goldenCookieDict['goldenCookieChance']
	cost = goldenCookieDict['cost']

	#This should actually upgrade the data for the cookies per click
	newGoldenCookieDict = goldenCookieDict
	newGoldenCookieDict['goldenCookieChance'] = chance * 2
	newGoldenCookieDict['cost'] = cost * 3
	save.file('goldenCookie.pickle', 'wb', newGoldenCookieDict)

	#Checks how many cookies the user has left
	#Then it prints it to console
	cookiesDict = save.file('cookiesData.pickle', 'rb')
	userCookies = cookiesDict['currentUser']
	print('\nYou have ' + str(userCookies) + ' cookies left!')


def checkGoldenCookie():
	"""
	Checks if the user just clicked on a golden cookie
	"""

	goldenCookieDict = save.file('goldenCookie.pickle', 'rb')
	goldenCookieChance = goldenCookieDict['goldenCookieChance']
	chance = random.randrange(0, 101)

	
	if chance <= goldenCookieChance:
		print('\n\n\n\nWERE YOU MINING FOR GOLDEN COOKIES?')
		print('BECAUSE YOU JUST FOUND ONE,')
		print("THAT IS WORTH 50 NORMAL COOKIES!\n\n\n\n")
		return True

	else:
		return False


def goldenCookieTrueOrFalse(worked, currentCookies):
	"""
	Checks if the user received a golden cookie
	And performs relevant logic for the check
	"""
	#Adds 50 cookies (golden cookie) to user's current cookies
	newCookiesToSave = currentCookies + 50

	#If the chance of getting a golden cookie worked:
	#Then the user will get a golden cookie
	#And the cookie he clicked will not be saved
	if worked == True:
		save.file('cookiesData.pickle', 'wb', {'currentUser': newCookiesToSave})
		cookie.clicker()

	#If the chance of getting a golden cookie failed:
	#Then this will just save the current cookies
	if worked == False:
		save.file('cookiesData.pickle', 'wb', {'currentUser': currentCookies})
		cookie.clicker()


