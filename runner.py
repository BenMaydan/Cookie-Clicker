import menu
import cookie
import save
from developer import developer
import sys


#save.file('userData.pickle', 'wb', {'totalCookies':0, 'cookiesPerClick':1, 'doubleUpgradeCost':500, 'goldenCookieChance':1, 'goldenCookieCost':1000})
try:
    menu.mainMenu.display()
except KeyboardInterrupt:
    print('\nStopping running processes ->')
    sys.exit()
