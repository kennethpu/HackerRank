T = int(raw_input())

# Find the maximum product a*b where a+b = K. This is maximized when a=K/2
for i in xrange(T):
    K = int(raw_input())
    a = K/2
    b = K-a
    print a*b