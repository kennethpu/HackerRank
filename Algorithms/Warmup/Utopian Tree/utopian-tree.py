# As specified, double height on even cycles, increment height by one on odd cycles
def solveHeight(N):
    height = 1
    for i in xrange(N):
        if i % 2 == 0:
            height *= 2
        else:
            height += 1
    return height

# ENTRY POINT
T = int(raw_input())

for i in xrange(T):
    N = int(raw_input())
    print solveHeight(N)