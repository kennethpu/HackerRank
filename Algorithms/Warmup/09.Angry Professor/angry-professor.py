T = int(raw_input())

for i in xrange(T):
    N, K = map(int, raw_input().split())
    arrivals = map(int, raw_input().split())
    onTime = 0

    # Count the number of students arriving "on-time"
    for j in xrange(N):
        if arrivals[j] <= 0:
            onTime += 1

    # If at least K students arrive on time class is not cancelled
    if onTime >= K:
        print 'NO'
    else:
        print 'YES'