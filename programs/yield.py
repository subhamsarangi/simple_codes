def gen():
	x=1
	while x<10:
		print(x)
		yield x*x
		x+=1

for i in gen():
	print(i)