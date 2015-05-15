# Read input from STDIN
N = input()
ratings = [input() for _ in xrange(N)]

# Initialize array of candies for each student
candies = [1]*N

# Iterate forward, if a student has a better rating and fewer candies
# than the previous student, set him to have one more than the previous
for i in xrange(1,N):
    if ratings[i] > ratings[i-1] and candies[i] <= candies[i-1]:
        candies[i] = candies[i-1] + 1

# Iterate backward, if a student has a better rating and fewer candies
# than the next student, set him to have one more than the next
for i in xrange(N-2, -1, -1):
    if ratings[i] > ratings[i+1] and candies[i] <= candies[i+1]:
        candies[i] = candies[i+1] + 1

# Output total number of candies needed
print sum(candies)