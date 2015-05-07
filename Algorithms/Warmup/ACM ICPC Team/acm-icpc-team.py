N,M = map(int, raw_input().split())

# Convert binary strings into corresponding integers
knowledge = []
for i in xrange(N):
    knowledge.append(int(raw_input(),2))
    
# OR together the previously stored integers, count the resulting 1's to find
# the number of known topics for every possible 2-person team
pairTopics = [bin(knowledge[a] | knowledge[b]).count('1') for a in xrange(N) for b in xrange(a+1,N)]
     
# Find the largest number of topics known as well as the number of teams that
# achieve this number of topics
maxTopics = max(pairTopics)
numTeams = pairTopics.count(maxTopics)

print maxTopics
print numTeams