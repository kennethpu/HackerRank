T = int(raw_input())

for _ in xrange(T):
    N = int(raw_input())
    
    # Subtract increasing multiples of 5 from the specified number of digits.
    # If at any point the remainder is divisible by 3, we have found the largest
    # possible 'decent number'. Otherwise no such number exists and return -1
    num = '-1'
    for a in xrange(0,N+1,5):
        b = N - a
        if b % 3 == 0:
            num = '5'*b + '3'*a
            break
    print num