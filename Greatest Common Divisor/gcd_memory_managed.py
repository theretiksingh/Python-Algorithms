# This is a improved way of finding the Greatest Common Divisor...
import sys

def gcd(m,n):
	for i in range(1, min(m,n)+1):
		if(m % i) ==0 and (n % i) == 0:
			mrcf = i

	return(mrcf)


print("Welcome. Let's find the Greatest Common Divisor.")

j = int(input('please enter first value for the function : '))
k = int(input('please enter second value for the function : '))

o = gcd(j,k)

print('The gcd is :', o)

input('press any key to exit :')
sys.ex