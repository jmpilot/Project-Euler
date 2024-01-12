
not_primes = []
primes = []
n = 100

for i in range(2,n+1):
	if i not in not_primes:
		primes.append(i)
		
		for j in range(i*i, n+1, i):
			not_primes.append(j)

print(primes)






	








