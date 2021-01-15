# Although the last memory management was good. but, for large numbers this system is more efficient. Since the countdown is reversed
import sys

def gcd(m,n):
	i = min(m,n)
	while i > 0:
		if(m % i) ==0 and (n % i) == 0:
			return(i)
		else: i = i -1

print("Welcome. Let's find the Greatest Common Divisor.")

j = int(input('please enter first value for the function : '))
k = int(input('please enter second value for the function : '))

o = gcd(j,k)

print('The gcd is :', o)

input('press any key to exit :')
sys.ex