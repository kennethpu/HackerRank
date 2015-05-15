# Data structure to help us keep track of connected components in a graph
# This is accomplished by representing connected components as trees. Each
# node points to a parent node, and all nodes pointing to the same parent
# belong to the same connected component
class UnionFind:
    def __init__(self, N):
        self.nodes = [x for x in xrange(N)]
        self.sizes = [1 for x in xrange(N)]
    
    # Return root node corresponding to x
    def Find(self, x):
        # Attach child nodes directly to root of tree for flatter tree structure
        if not self.nodes[x] == x:
            self.nodes[x] = self.Find(self.nodes[x])
        return self.nodes[x]

    # Join nodes x and y into a connected component 
    def Union(self, x, y):
        # Find root nodes corresponding to x and y, return if they are the same (already connected)
        xRoot = self.Find(x)
        yRoot = self.Find(y)
        if xRoot == yRoot:
            return

        # Attach smaller tree to root of larger tree for a more balanced tree
        if (self.sizes[xRoot] < self.sizes[yRoot]):
            self.nodes[xRoot] = yRoot
            self.sizes[yRoot] += self.sizes[xRoot]
        else:
            self.nodes[yRoot] = xRoot
            self.sizes[xRoot] += self.sizes[yRoot]

    # Returns a list of the sizes of all connected components consisting of 
    # more than one node (for our purposes size is all we need)
    def ccCounts(self):
        cc = []
        for i in xrange(len(self.nodes)):
            if (self.nodes[i] == i and self.sizes[i] > 1):
                cc.append(self.sizes[i])
        return cc

# Helper function to calculate the total number of edges between N nodes
def numEdges(N):
    return N*(N-1)/2

# ENTRY POINT
N,l = map(int,raw_input().split())

# Initialize result to be the total number of pairings possible
result = numEdges(N)

# Initialize union find data structure
uf = UnionFind(N)
    
# Join specified nodes into connected components
for i in xrange(l):
    a,b = map(int,raw_input().split())
    uf.Union(a,b)
    
# Subtract all edges in connected components as they represent illegal pairings
for count in uf.ccCounts():
	result -= numEdges(count)

print result
