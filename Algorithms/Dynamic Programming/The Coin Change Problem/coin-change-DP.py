# Computes the number of ways to fill the value N using the coin values specified in C
def giveChange(N,C):
	# Initialize table for DP
	change = [[0]*len(C) for _ in xrange(N+1)]
	change[0] = [1]*len(C)

	# Fill in solutions
	for i in xrange(1,N+1):
		for j in xrange(len(C)):
			a = 0 # Number of ways to fill remaining value after subtracting current coin value
			b = 0 # Number of ways to fill current value only using coin values up to current coin value
			
			if i-C[j] >= 0:
				a = change[i-C[j]][j] # 0 ways unless current coin value is smaller than current value
			if j >= 1:
				b = change[i][j-1] # 0 ways unless there are other coin values before current coin value
			
			# Number of ways to fill current value is sum of a and b (see above)
			change[i][j] = a + b
	
	return change[N][len(C)-1];

# ENTRY POINT
N,M = map(int, raw_input().split())
C = map(int, raw_input().split())

print giveChange(N,C)