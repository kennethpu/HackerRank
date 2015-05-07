# Takes as input a number n and returns the left and right pieces resulting from 
# splitting the number string down the middle
def split_number(n):
	n_string = str(n)

	# Split into two strings, when number is odd length give extra digit to right piece
	r = n_string[len(n_string)//2:]
	l = n_string.replace(r,'')

	# If left piece has no digits convert to 0
	if l == '':
		l = '0'

	# Return pieces as integers
	return int(l), int(r)

# ENTRY POINT
p = int(raw_input())
q = int(raw_input())

# Check every integer between p and q inclusive if they satisfy conditions for kaprekar
kaprekar = []
for num in xrange(p,q+1):
	l,r = split_number(num*num)
	if l+r == num:
		kaprekar.append(str(num))

# Print kaprekar numbers if found otherwise print 'INVALID RANGE'
if len(kaprekar) > 0:
	print ' '.join(kaprekar)
else:
	print 'INVALID RANGE'