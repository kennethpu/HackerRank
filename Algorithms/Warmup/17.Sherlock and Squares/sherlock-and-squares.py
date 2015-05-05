from math import floor, ceil, sqrt

# ENTRY POINT
T = int(raw_input())

for i in xrange(T):
    A,B = map(int, raw_input().split())
    # To find the number of squares between two numbers, find the minimum 
    # difference of the square roots of the two numbers
    numSquares = int(floor(sqrt(B)) - ceil(sqrt(A)) + 1)
    print numSquares