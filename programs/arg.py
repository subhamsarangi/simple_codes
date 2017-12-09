def x(arg1,arg2,arg3):
	print('arg1',arg1)
	print('arg2',arg2)
	print('arg3',arg3)

a= ('s','a','m')
b={'arg1':'yes','arg2':'no','arg3':'whatever'}

x(*a)
x(**b)