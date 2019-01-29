import menu
import cookie
import save
from developer import developer


#save.file('userData.pickle', 'wb', {'totalCookies':0, 'cookiesPerClick':1, 'doubleUpgradeCost':500, 'goldenCookieChance':1, 'goldenCookieCost':1000})
exit = False
while not exit:
	exit = menu.mainMenu()