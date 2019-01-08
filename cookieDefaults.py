import pickle

def picklingDev(mode):
	"""
	Defaults for the developer login details
	"""

	registeredDevelopers = {'Ben':'default'}

	pickle_out = open("devs.pickle", mode)
	pickle.dump(registeredDevelopers, pickle_out)
	pickle_out.close()


def picklingCookies(mode):
	"""
	Defaults for the number of cookies the user has when first starting, 0
	"""

	cookieDict = {'currentUser':0}

	pickle_out = open("cookiesData.pickle", mode)
	pickle.dump(cookieDict, pickle_out)
	pickle_out.close()


def picklingDoubleUpgrade(mode, cookiesPerClick = 1):
	"""
	Defaults for which upgrade the user is on for the double upgrade
	"""

	doubleUpgrade = {'cookiesPerClick':cookiesPerClick}

	doubleUpgradeFile = open("doubleUpgrade.pickle", mode)
	pickle.dump(doubleUpgrade, doubleUpgradeFile)
	doubleUpgradeFile.close()