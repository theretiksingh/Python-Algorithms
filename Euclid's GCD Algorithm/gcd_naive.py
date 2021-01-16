# Using Euclid's Divison Theorem to solve the Greatest Common Divisor problem!!!
import sys

def gcd(m,n):
	# Assumption : m >= n
	if m < n:
		(m,n) = (n,m)

	if (m % n) == 0:
		return(n)
	else:
		diff = m - n
		# Possibilty that diff > n.
		return(gcd(max(n,diff),min(n,diff)))

print("Welcome. Let's find the Greatest Common Divisor.")

j = int(input('please enter first value for the function : '))
k = int(input('please enter second value for the function : '))

o = gcd(j,k)

print('The gcd is :', o)

input('press any key to exit :')
sys.ex