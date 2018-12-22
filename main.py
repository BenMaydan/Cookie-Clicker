import menu

def clicker():
	pass


def developer():

	exit = False

	while not exit:
		registeredDevelopers = open('registeredDevelopers.txt', 'w')
		registeredDevelopers.write("{'Ben':'root'}")
		registeredDevelopers.close()

		
		registeredDevelopers = open('registeredDevelopers.txt', 'r')
		registeredDevelopers.read()
		registeredDevelopers = dict()
		#Current error:
		#Does not actually make registered developers a dict with the appropriate usernames
		print(registeredDevelopers)

		username = input('\nWhat is your username?\n')
		password = input('\nWhat is your password?\n')

		print(username in registeredDevelopers)

		#Checks if username and password is correct
		if username in registeredDevelopers:

			if registeredDevelopers[username] == password:
				print('Success! You are now in the developer menu!')
				print('This is a test')
				exit = True
				print('This is a test')
				menu.developer()
			else:
				print('Error: Wrong username or password')
				exit = True
				print('This is a test')
				menu.mainMenu()

		else:
			print('Error: Wrong username or password')
			exit = True
			menu.mainMenu()