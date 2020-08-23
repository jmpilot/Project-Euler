
not_prime_list = []
primes = []
n = 110000

for i in range(2,n+1):
	if i not in not_prime_list:
		primes.append(i)
		
		for j in range(i*i, n+1, i):
			not_prime_list.append(j)

print(primes[10000])






	








