import itertools



m = []
a = []
c = []

f =[(i) for i in range (1,10)]
s = [(i) for i in range (0,10)]

##initial two digits
b =[e for e in itertools.product(f,s)]

##middle digits to list m from 
for x in s:
	m.append((x,x))


##incorporate the middle digits (from m), and reverse of initial two digits
for o in m:
	for d in b:
		t = d + o + d[::-1]
		q,r,s,t,u,v = [e for e in t[0:6]]
		sum = (q*100000) + (r*10000) + (s*1000) + (t*100) + (u*10) + (v*1)
		a.append(sum)

a.sort(reverse=True)


for x in a:
	for y in range(100,999):
		if x%y == 0:
			z = x//y
			s =	'{} is {} times {}'.format(x,y,z)
			print(s)
			
									




	

		









		



	
	