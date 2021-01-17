# Using Euclid's Divison Theorem to solve the Greatest Common Divisor problem!!! Euclid solves it in a easier way with less Time and Space Complexity thus saving tome
import sys

def gcd(m,n):
	# Assumption : m >= n
	if m < n:
		(m,n) = (n,m)

	while (m%n) !=0:
		diff = m - n
		# It's possible that diff > n.
		(m,n) = (max(n,diff),min(n,diff))
		
	return(n)

print("Welcome. Let's find the Greatest Common Divisor.")

j = int(input('please enter first value for the function : '))
k = int(input('please enter second value for the function : '))

o = gcd(j,k)

print('The gcd is :', o)

input('press any key to exit :')
sys.ex

# Done!!!