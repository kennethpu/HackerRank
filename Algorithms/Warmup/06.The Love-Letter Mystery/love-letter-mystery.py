# Count the number of times we must decrement to convert a 'word' into a palindrome
def toPalindrome(word):
    revWord = word[::-1]
    changes = 0
    for i in xrange(len(word)/2):
        a = ord(word[i])
        b = ord(revWord[i])
        changes += abs(a-b)
    return changes

# ENTRY POINT
T = int(raw_input())
for i in xrange(T):
    word = raw_input()
    print toPalindrome(word)