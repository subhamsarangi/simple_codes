print ('{:-^50}'.format('\nHello & Welcome!\n'))
def list_of_dicts(seq,opt):
	if opt=='1':
		l1=sorted(dict(zip(seq,range(1,len(seq)+1))).items())
		l3=zip(seq,range(1,len(seq)+1))
		print ('{:#^85}'.format('\nOrdered, Lexicographically\n'))
		for l2 in l1:
			print (l2,'\n')
		
		print ('{:#^45}'.format('\nOrdered, As is\n'))
		for l4 in l3:
			print (l4)

	elif opt=='2':	
		d=dict(zip(seq,range(1,len(seq)+1)))
		t=d.items()
		print ('{:24}'.format('\nDictonary'),d,'{:24}'.format('\nList of Tuples, sorted'), sorted(t))

	else:
		print ('{:!^50}'.format('You are dumber than you type'))

sequence=input('\nEnter a string: \n')
option=input('\nStructured or Haphazard?? Enter 1 or 2: ')
list_of_dicts(sequence, option)