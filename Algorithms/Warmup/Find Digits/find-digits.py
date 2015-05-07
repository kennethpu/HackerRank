T = int(raw_input())

# Iterate through digits in each number, counting the ones that exactly divide the number
for i in xrange(T):
    num = raw_input()
    a = int(num)
    count = 0
    for x in num:
        b = int(x)
        if b != 0 and a%b == 0:
            count += 1
    print count