from math import sqrt

def sqrz(n):

	l = [x**2 for x in range(n//2)]
	
	combo = [(x,y) for x in l for y in l if x != y]

	for i in combo:

		p,q = i

		if l.count(sum(i)) != 0:
			
			if (sqrt(p)+sqrt(q)+sqrt(sum(i))) == n:
				print(sqrt(p)*sqrt(q)*sqrt(sum(i)))
			


sqrz(1000)



	












	

	
		
	

		




			












