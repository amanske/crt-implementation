import sys

#Extended Euclidian Algorithm
#https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm
#takes positive integers a, b as input, and returns a triple (g, x, y), such that ax + by = g = gcd(a, b).
def egcd(b, n):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while n != 0:
        q, b, n = b // n, n, b % n
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return  b, x0, y0

#Theory fetched from https://rosettacode.org/wiki/Chinese_remainder_theorem
def crt(primes, values):
	N = 1
	for q in primes: 
		N *= q #Calculate the prime product (q1*q2*...*qk)
	i = 0
	by = []
	while i < k:
		n_i = N//primes[i] #Since N is a product of primes, n_i and N are co-prime
		(gcd, r_i, s_i) = egcd(primes[i], n_i) #gcd=1 since they are co-prime, value of r_i not needed to solve the problem
		by.append(s_i*n_i) # = s_i * N/prime[i]
		i += 1
	res = 0
	i = 0
	while i < k: #result is the sum ranging from i=0 to i = (k - 1) of value[i] * s_i * N/prime[i]
		res += values[i]*by[i]
		i += 1
	return res % N #Make sure that res is the smallest possible solution

for line in sys.stdin:
	line = line.strip("\n") #remove newline character from last element on line
	data = line.split(" ")
	k = int(data[0]); #store k value, aka index size of primes and values
	i = 1
	primes = []
	values = []
	while i < len(data):
		if i <= k:
			primes.append(int(data[i])) #store all prime integers on line in a list
			i+=1
		else:
			values.append(int(data[i])) #store all integers on line in a list
			i+=1
	print(crt(primes, values)) #Call function crt to solve 


