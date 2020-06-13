x=int(input('Enter a number'))
def isprime(x):
	for i in range(2,x):
		if x%i==0:
			print(0)
			break
		else:
			print(1)
			break
		
isprime(x)

