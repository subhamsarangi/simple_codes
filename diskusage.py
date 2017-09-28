import os
def disk_usage(path):
	total=os.path.getsize(path)

p=input('Enter a path: ')
print(disk_usage(p))