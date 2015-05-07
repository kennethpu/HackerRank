N = int(raw_input())
lengths = map(int, raw_input().split())

# For each loop remove all minimum length sticks until no sticks remain
while len(lengths) > 0:
    print len(lengths)
    rem = min(lengths)
    lengths = [x for x in lengths if x!=rem]