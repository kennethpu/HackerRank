import fractions

# Find the GCD of a provided list of integers
def listGCD(lst):
    gcd = lst[0]
    for i in xrange(1,len(lst)):
        gcd = fractions.gcd(gcd,lst[i])
    return gcd

# ENTRY POINT
T = int(raw_input())

for i in xrange(T):
    N = int(raw_input())
    A = map(int, raw_input().split())

    # If GCD of entire list is 1, there exists a subset for which GCD is 1
    gcd = listGCD(A)
    if gcd == 1:
        print "YES"
    else:
        print "NO"