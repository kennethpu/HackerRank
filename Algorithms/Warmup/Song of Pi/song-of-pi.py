# Digits of PI for reference
PI = '31415926535897932384626433833'

# ENTRY POINT
T = int(raw_input())

for _ in xrange(T):
    words = raw_input().split()

    # Check that each word is the same length as the corresponding digit in Pi
    isPI = True
    for i in xrange(len(words)):
        isPI = isPI and (len(words[i]) == int(PI[i]))
    
    if isPI:
        print "It's a pi song."
    else:
        print "It's not a pi song."
            