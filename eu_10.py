
def sieve_of_Sundaram(n):
   
    k = (n - 2) // 2 #only check up to the upper limit number as divided by 2
    primes = 2
    integers_list = [True] * (k + 1) #initialize a a membership list to the above limit, defaulting to true
    for i in range(1, k + 1): #sets up a loop to from i and j (as equal) to to incrementing j against i
        j = i
        while i + j + 2 * i * j <= k: #start the loop that will end at condition here
            integers_list[i + j + 2 * i * j] = False #mark it 
            j += 1 #increment j against i (so i remains the same untill the loop restarts)
    if n > 2:
        print(2, end=' ')
    for i in range(1, k + 1):
        if integers_list[i]:
        	primes = primes + (2 * i + 1) #find prime by double and increment by 1, and add the running sum
        	print(2 * i + 1, end=' ')
    print(primes)




sieve_of_Sundaram(2000000)
	