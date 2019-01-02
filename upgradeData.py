import cookie
import cookieDefaults

def doubleUpgrade():
	"""
	If the user decides to pay with cookies for a double upgrade, this function will double the amount of cookies the user gets per click
	"""

	numberOfCookies = cookie.numberOfCookies()

	doubleUpgradeFile = open("doubleUpgrade.pickle", "rb")
	doubleUpgradeDict = pickle.load(doubleUpgradeFile)
	doubleUpgradeFile.close()

	
	currentUpgrade = doubleUpgradeDict['currentClicks']
	doubleUpgradeFile = open("doubleUpgrade.pickle", "wb")
