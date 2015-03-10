#Test
import math
it = 0
u = 0.5
while it <=50:
	it += 1
	num = 0
	denum  = 0
	for k in range(0,100):
		num += pow(k+1,-1.5)*pow(u,k)
		if k>0: denum += pow(k,-1.5)
	unew = num / denum
	print unew
	u = unew
