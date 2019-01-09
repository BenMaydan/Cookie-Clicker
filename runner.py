import menu
import cookie
import save


save.file('cookiesData', 'wb', {'currentUser':0})
save.file('doubleUpgrade.pickle', 'wb', {'cookiesPerClick':1, 'cost':500})
#doubleUpgradeDict = save.file('doubleUpgrade.pickle', 'rb')
#print(doubleUpgradeDict)


#menu.mainMenu()