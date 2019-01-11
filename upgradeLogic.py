import save

def doubleUpgrade():
	"""
	Performs all of the logic if the double upgrade is successful
	"""

	#Initializing variables
	cookiesDict = save.file('cookiesData.pickle', 'rb')
	doubleUpgradeDict = save.file('doubleUpgrade.pickle', 'rb')
	userCookies = cookiesDict['currentUser']

	print('\nThe cost for this upgrade is ' + str(doubleUpgradeDict['cost']))


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