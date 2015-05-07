# Iterate through all combinations of integers between l and r to find maximum xor value
def maxXor(l, r):
    xorMax = 0
    for i in xrange(l, r+1):
        for j in xrange(i, r+1):
            xorMax = max(xorMax, i^j)
    return xorMax

# ENTRY POINT
L = int(raw_input());
R = int(raw_input());
res = maxXor(L,R);
print(res)
