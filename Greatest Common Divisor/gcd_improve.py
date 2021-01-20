# This is a improved way of finding the Greatest Common Divisor but only in readbility...
import sys

def gcd(m,n):
	cf = []
	for i in range(1, min(m,n)+1):
		if(m % i) ==0 and (n % i) == 0:
			cf.append(i)

	return(cf[-1])


print("Welcome. Let's find the Greatest Common Divisor.")

j = int(input('please enter first value for the function : '))
k = int(input('please enter second value for the function : '))

o = gcd(j,k)

print('The gcd is :', o)

input('press any key to exit :')
sys.ex
