T = int(raw_input())

for _ in xrange(T):
    B,W = map(int, raw_input().split())
    X,Y,Z = map(int, raw_input().split())
    
    # For each gift type simply check if it is cheaper to buy directly or 
    # buy the alternative and convert. Use the cheaper price
    cost = B*min(X,Y+Z) + W*min(Y,X+Z)
    print cost