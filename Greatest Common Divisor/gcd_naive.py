# This is a naive way of finding the Greatest Common Divisor...
import sys

def gcd(m,n):
	fm = []
	for i in range(1, m+1):
		if(m % i) == 0:
			fm.append(i)

	fn=[]
	for j in range(1, n+1):
		if(n % j) == 0:
			fn.append(j)

	cf = []
	for f in fm:
		if f in fn:
			cf.append(f)

	return(cf[-1])

print("Welcome. Let's find the Greatest Common Divisor using a defintion based Algorithm")

m = int(input('please enter first value for the function : '))
n = int(input('please enter second value for the function : '))

j = gcd(m,n)
print('The gcd is :', j)

input('press any key to exit :')
sys.ex
