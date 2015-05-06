N,M = map(int, raw_input().split())

# For each step, we add k candies to b-a+1 jars, so add (b-a+1)*k to total
avg = 0
for _ in xrange(M):
    a,b,k = map(int, raw_input().split())
    avg += (b-a+1)*k

# Divide by N to find average (python automatically rounds down)
avg /= N

print avg