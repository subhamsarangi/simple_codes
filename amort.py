import sys
from time import time
def sizeavg(n):
	data=[]
	start=time()
	for i in range(n):
	        a,b=len(data),sys.getsizeof(data)
        	# print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a,b))
        	data.append(None)
	end=time()
	elapsed=(end-start)/n
	print ('DATASIZE ',n)
	print('AVG: {:3.13f}'.format(elapsed))
	print('TOT: {:3.13f}'.format(end-start))


if __name__ == "__main__":
	#num=int(input('Enter a numero: '))
	for k in range (100000,1100000,100000):
		sizeavg(k)