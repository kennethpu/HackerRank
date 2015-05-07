# Find minimum width within specified range
def minWidth(i, j, width):
    min_width = 3
    for x in xrange(i,j+1):
        min_width = min(width[x], min_width)
    return min_width

# ENTRY POINT
N, T = map(int, raw_input().split())
width = map(int,raw_input().split())
for x in xrange(T):
    i, j = map(int, raw_input().split())
    print minWidth(i,j,width)