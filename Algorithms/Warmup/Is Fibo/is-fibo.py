T = int(raw_input())

# Initialize a list to hold fibonacci numbers 
fibo = [0,1]

for _ in xrange(T):
    N = int(raw_input())
    
    # Grow fibonacci list while the last (aka largest) element is smaller than current number
    while fibo[-1] < N:
        fibo.append(fibo[-2]+fibo[-1])
    
    # Check if current number is in fibonacci list
    if N in fibo:
        print 'IsFibo'
    else:
        print 'IsNotFibo'