# Find all possible values of final stone by adding fewer numbers of the
# smaller number and increasing numbers of the larger number
def findLast(n,a,b):
    lil = a
    big = b
    if a > b:
        lil = b
        big = a
        
    values = []
    for i in xrange(n+1):
        newVal = (n-i)*lil + i*big
        if newVal not in values:
            values.append(newVal)
    return [str(x) for x in values]

# ENTRY POINT
T = int(raw_input())

for i in xrange(T):
    n = int(raw_input())
    a = int(raw_input())
    b = int(raw_input())
    
    values = findLast(n-1,a,b)

    # Print array of values as a space separated list
    print ' '.join(values)