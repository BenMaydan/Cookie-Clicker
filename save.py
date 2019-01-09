import pickle
import cookie


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
