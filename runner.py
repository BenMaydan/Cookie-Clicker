import menu
import cookie
import save


#save.file('cookiesData', 'wb', {'currentUser':0})
#save.file('doubleUpgrade.pickle', 'wb', {'cookiesPerClick':1, 'costDoubleUpgrade':500})
#save.file('goldenCookie.pickle', 'wb', {'goldenCookieChance':1, 'costGoldenCookie':1000})
#doubleUpgradeDict = save.file('doubleUpgrade.pickle', 'rb')
#print(doubleUpgradeDict)

exit = False
while not exit:
	exit = menu.mainMenu()