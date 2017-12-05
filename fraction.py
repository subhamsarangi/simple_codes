import math
pi=math.pi
print('pi = ',pi)
print('truncated pi = ',math.trunc(pi))
print('floored pi = ',math.floor(pi))
print('ceiling pi = ',math.ceil(pi))
print("Precision pi using percentage = %.3f" % pi)
print('Precision pi using .format() = {0:.4f}'.format(pi))
print('Precision pi using round(x,n) = ',round(pi,5))