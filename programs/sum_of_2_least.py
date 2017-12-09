import copy
def sum_of_2_least(numbers):
	num=copy.copy(numbers)
	num.remove(min(num))
	print (min(numbers),min(num))

sum_of_2_least([0,63,77,31,92])
sum_of_2_least([121,100,602,99,104])
sum_of_2_least([3126,1996,2017,2008,3333,2222])