n = int(raw_input())

# Copy depths into a 2D array
map = []
for i in xrange(n):
    map.append([c for c in raw_input()])

# For each inner cell, check if it's depth is greater than all 4 of it's neighbors
for i in xrange(1,n-1):
    for j in xrange(1,n-1):
        cur = map[i][j]
        if (cur > map[i-1][j]) and (cur > map[i+1][j]) and (cur > map[i][j-1]) and (cur > map[i][j+1]):
            map[i][j] = 'X'

for line in map:
    print ''.join(line)