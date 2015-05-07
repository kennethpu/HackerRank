# Append numbers to a new array and remove them as a duplicate is found.
# The remaining number is the one that only occurs once
def lonelyinteger(a):
    seen = []
    for i in a:
        if i in seen:
            seen.remove(i)
        else:
            seen.append(i)
    return seen.pop()

# ENTRY POINT
a = input()
b = map(int, raw_input().strip().split(" "))
print lonelyinteger(b)