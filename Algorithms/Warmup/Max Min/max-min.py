N = int(raw_input())
K = int(raw_input())

# Construct sorted list of integers
lists = [int(raw_input()) for _ in xrange(N)]
lists.sort()

# Construct list of differences between integers at K-1 index offsets from each other
diffs = [lists[i+K-1] - lists[i] for i in xrange(N-(K-1))]

# Minimum difference is the minimum possible value of 'unfairness'
min_diff = min(diffs)
print min_diff
