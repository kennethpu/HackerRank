# Computes the number of ways to fill the value N using the coin values specified in C
def giveChange(N,C):
	if N == 0:
		# Exactly one way to fill 0 value (no change)
		return 1
	if N < 0 or len(C) <= 0:
		# No ways to fill value if either value is negative or no coins can be used
		return 0

	# Number of ways to fill N using C is equal to the sum of two values:
	#   1. The number of ways to fill N without using the largest coin in C
	#   2. The number of ways to fill the remaining value after using the largest coin in C 
	cMax = max(C)
	C2 = [c for c in C if c != cMax]
	return giveChange(N, C2) + giveChange(N-cMax, C)

# ENTRY POINT
N,M = map(int, raw_input().split())
C = map(int, raw_input().split())

print giveChange(N,C)