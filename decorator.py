def deco_msg(val):
	def hey(username):
		return 'hey '+ val(username)

	return hey

@deco_msg
def user(username):
	return username

print (user('Subham'))