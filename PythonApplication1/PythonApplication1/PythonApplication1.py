
import time
from numba import jit
#@jit

def foo(x,y):
	tt=time.time()
	s=1
	for i in range (x,y):
		s+=i
	print('Time used: {} sec'.format(time.time()-tt))
	return s

print(foo(1,5000000 ))