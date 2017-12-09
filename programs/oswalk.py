# listdir,path.join, path.Isdir
def oswalk(path):
	from os import listdir
	from os.path import isdir,join
	for c in listdir(path):
		cp = join(path,c)
		if isdir(cp):
			oswalk(cp)
		else:
			print(cp)

p=input('Enter a valid path: ')
oswalk(p)