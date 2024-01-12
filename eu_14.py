def collatz(n):

	l = []
	s = n

	while n != 1:


		if n%2 == 0:
			n = n/2
			
			l.append(n)

		else:
			n = 3*n + 1
			
			l.append(n)
	
	return (s,len(l))





g = [collatz(i) for i in range(1,1000000)]
print(max(g, key=lambda k: k[1]))