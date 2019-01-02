import menu
import cookie
import cookieDefaults


exit = False
while not exit:
	runBefore = input('\nHave you run this program before? If you have and you say no all of your data will be lost. y/n\n')

	if runBefore == 'y':
		menu.mainMenu()

	elif runBefore == 'n':
		cookieDefaults.picklingCookies('wb')
		cookieDefaults.picklingDev('wb')
		cookieDefaults.picklingDoubleUpgrade('wb')
		menu.mainMenu()

	else:
		print('Unrecognized input!')