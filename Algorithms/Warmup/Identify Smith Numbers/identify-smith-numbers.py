# Takes as input an integer as a string and outputs the sum of its digits
def sum_digits(nString):
	digitSum = 0
	for i in xrange(len(nString)):
		digitSum += int(nString[i])
	return digitSum

# Takes as input an integer and returns a list of prime factors as strings
def prime_factors(n):
	i = 2
	factors = []

	while i*i <= n:
		if n % i:
			i += 1
		else:
			n //= i
			factors.append(i)
	if n > 1:
		factors.append(n)
	return [str(x) for x in factors]

# ENTRY POINT
N = raw_input()

# If the sum of an integer's digits are the same as the sum of the digits 
# of it's prime factors, the integer is a Smith Number
if sum_digits(N) == sum(sum_digits(x) for x in prime_factors(int(N))):
	print '1'
else:
	print '0'


