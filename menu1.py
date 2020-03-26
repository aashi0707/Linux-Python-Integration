import os

os.system("tput setaf 1")
print("\t\t\t Hey Welcome to my TUI that makes my life simple")
os.system("tput setaf 7")

print("\t\t\t ----------------------------------------------")


print("Where you would like to perform your job(local/remote): ", end = '')
location = input()
print(location)


if location == "remote":
	remoteIP = input("Enter your IP: ")


########### M E N U ###############
print(""" Press 1: to see date
          Press 2: to check calendar
          Press 3: Configure web server
          Press 4: To create user
          Press 5: Create a file
          Press 6: To setup network
          Press 7: To exit
     """)


print("Enter your choice ", end = " ")
ch = input()

print(ch)

if location == "local":
	if int(ch) == 1:
		os.system("date")
	elif int(ch) == 2:
        	os.system("cal")
	elif int(ch) == 3:
        	os.system("yum install httpd")
	elif int(ch) == 4:
        	print("Can you please enter the user name you want to create: ", end = '')
        	createUser = input()
        	os.system("useradd {}". format(createUser))


elif location == "remote":
        if int(ch) == 1:
                os.system("ssh 192.168.43.249 date")
        elif int(ch) == 2:
                os.system("ssh 192.168.43.249 cal")
        elif int(ch) == 3:
                os.system("ssh ip yum install httpd")
        elif int(ch) == 4:
                print("Can you please enter the user name you want to create: ", end = '')
                createUser = input()
                os.system("ssh {} useradd {}".format(remoteIP,createUser))

else: 
	print("Option not Supported")																							
