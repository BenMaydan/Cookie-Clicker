import pickle
import cookie


def saveCookies(cookiesClicked):
	"""
	Saves the number of cookies the user has clicked this session in a file
	"""

	clickedCookies = {}
	clickedCookies['currentUser'] = cookiesClicked

	pickle_out = open("cookiesData.pickle","wb")
	pickle.dump(clickedCookies, pickle_out)
	pickle_out.close()


def loadSaveData():
	"""
	When the user opens the program, this function will proceed to load in how many cookies the user has
	"""
	
	try:
		pickle_out = open("cookiesData.pickle","rb")
		cookieDict = pickle.load(pickle_out)
		totalCookies = cookieDict['currentUser']
		pickle_out.close()

		return totalCookies
	
	except EOFError:
		print("I'm afraid your cookie data has been corrupted. We know this won't compensate, but we have given you 1,500 cookies to make up for it.")
		cookie.corruptedData()