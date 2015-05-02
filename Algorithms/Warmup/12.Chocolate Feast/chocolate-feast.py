T = int(raw_input())

for _ in xrange (T):
    N,C,M = [int(x) for x in raw_input().split()]
    chocolates = N/C
    wrappers = chocolates
    # Keep adding chocolates while there are still enough wrappers to redeem more
    while (wrappers >= M):
        redeemed = wrappers/M
        chocolates += redeemed
        wrappers = redeemed + wrappers%M
    print chocolates