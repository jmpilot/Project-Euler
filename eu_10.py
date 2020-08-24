
not_prime_list = []
primes = 0
n = 10000

for i in range(2,n+1):
	if i not in not_prime_list:
		primes = primes + i
		
		for j in range(i*i, n+1, i):
			not_prime_list.append(j)

print(primes)
