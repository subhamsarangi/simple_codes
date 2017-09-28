from fbchat import Client
from fbchat.models import *
from getpass import getpass

username = str(input("Username: "))
client = Client(username, getpass())

print("Loggin your ass in...")
print("....")
print("LOGGED IN")

name = str(input("Enter the name of your homie: "))
homies = client.searchForUsers(name)
homie = homies[0]

print("Details of your homie\n")
print (homie.url)
print (homie.uid)
print (homie.name)

msg = str(input("Message: "))
_confirm=str(input("type CONFIRM if you want to send the message.. "))
if _confirm == "CONFIRM":
	sent = client.sendMessage(msg, thread_id=homie.uid, thread_type=ThreadType.USER)
	client.reactToMessage(sent, MessageReaction.LOVE)
	if sent:
		print("Message was  sent successfully!")
		outlog=client.logout()
		if outlog:
			print("Loggin out...")
			print("....")
			print("LOGGED OUT")
		else:
			print("Can't log your ass out!  ERROR")
	else:
		print("What kinda shit is that? ERROR")
else:
	print("What kinda shit is that?  ERROR")